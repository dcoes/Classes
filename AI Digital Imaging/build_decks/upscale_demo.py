"""Real-ESRGAN x4plus (RRDBNet) in plain PyTorch, to make the upscaling slides.

Usage, from the repo root (needs torch and scikit-image):
  curl -L -o RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
  python3 "AI Digital Imaging/build_decks/upscale_demo.py" RealESRGAN_x4plus.pth "AI Digital Imaging/images/"

Writes upscale_compare.png (a face, where it invents) and upscale_texture.png
(a cup and spoon, where it shines). Both start from scikit-image sample photos.
"""
import sys, numpy as np, torch, torch.nn as nn, torch.nn.functional as F
from PIL import Image, ImageDraw, ImageFont
from skimage import data, transform

class RDB(nn.Module):
    def __init__(self, nf=64, gc=32):
        super().__init__()
        self.conv1 = nn.Conv2d(nf, gc, 3, 1, 1); self.conv2 = nn.Conv2d(nf + gc, gc, 3, 1, 1)
        self.conv3 = nn.Conv2d(nf + 2 * gc, gc, 3, 1, 1); self.conv4 = nn.Conv2d(nf + 3 * gc, gc, 3, 1, 1)
        self.conv5 = nn.Conv2d(nf + 4 * gc, nf, 3, 1, 1); self.lrelu = nn.LeakyReLU(0.2, True)
    def forward(self, x):
        x1 = self.lrelu(self.conv1(x)); x2 = self.lrelu(self.conv2(torch.cat((x, x1), 1)))
        x3 = self.lrelu(self.conv3(torch.cat((x, x1, x2), 1))); x4 = self.lrelu(self.conv4(torch.cat((x, x1, x2, x3), 1)))
        x5 = self.conv5(torch.cat((x, x1, x2, x3, x4), 1)); return x5 * 0.2 + x

class RRDB(nn.Module):
    def __init__(self, nf, gc=32):
        super().__init__(); self.rdb1 = RDB(nf, gc); self.rdb2 = RDB(nf, gc); self.rdb3 = RDB(nf, gc)
    def forward(self, x):
        return self.rdb3(self.rdb2(self.rdb1(x))) * 0.2 + x

class RRDBNet(nn.Module):
    def __init__(self, nf=64, nb=23, gc=32):
        super().__init__()
        self.conv_first = nn.Conv2d(3, nf, 3, 1, 1)
        self.body = nn.Sequential(*[RRDB(nf, gc) for _ in range(nb)])
        self.conv_body = nn.Conv2d(nf, nf, 3, 1, 1)
        self.conv_up1 = nn.Conv2d(nf, nf, 3, 1, 1); self.conv_up2 = nn.Conv2d(nf, nf, 3, 1, 1)
        self.conv_hr = nn.Conv2d(nf, nf, 3, 1, 1); self.conv_last = nn.Conv2d(nf, 3, 3, 1, 1)
        self.lrelu = nn.LeakyReLU(0.2, True)
    def forward(self, x):
        feat = self.conv_first(x); feat = feat + self.conv_body(self.body(feat))
        feat = self.lrelu(self.conv_up1(F.interpolate(feat, scale_factor=2, mode='nearest')))
        feat = self.lrelu(self.conv_up2(F.interpolate(feat, scale_factor=2, mode='nearest')))
        return self.conv_last(self.lrelu(self.conv_hr(feat)))

weights, outdir = sys.argv[1], sys.argv[2]
net = RRDBNet()
sd = torch.load(weights, map_location='cpu', weights_only=True)
sd = sd.get('params_ema', sd.get('params', sd))
net.load_state_dict(sd, strict=True); net.eval()
torch.set_num_threads(2)

import os
S = 520
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)


def sheet_for(crop, out):
    x = torch.from_numpy(np.ascontiguousarray(crop.transpose(2, 0, 1))).float().unsqueeze(0)
    with torch.no_grad():
        y = net(x).clamp(0, 1)[0].numpy().transpose(1, 2, 0)
    low = Image.fromarray((crop * 255).astype(np.uint8))
    plain = low.resize((S, S), Image.BICUBIC)
    ai = Image.fromarray((y * 255).astype(np.uint8)).resize((S, S), Image.LANCZOS)
    W = S * 2 + 24 * 3
    sheet = Image.new("RGB", (W, S + 70), "white")
    d = ImageDraw.Draw(sheet)
    sheet.paste(plain, (24, 0))
    d.text((24, S + 16), "plain resampling, 4x", fill=(43, 43, 43), font=font)
    sheet.paste(ai, (48 + S, 0))
    d.text((48 + S, S + 16), "AI upscaler (Real-ESRGAN), 4x", fill=(43, 43, 43), font=font)
    # the 64 px original, inset at true scale x2 in the corner of the left panel
    inset = low.resize((128, 128), Image.NEAREST)
    sheet.paste(inset, (24 + 12, S - 128 - 12))
    d.rectangle([24 + 12, S - 128 - 12, 24 + 12 + 127, S - 13], outline=(255, 255, 255), width=3)
    d.text((24 + 16, S - 128 - 50), "original", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    sheet.save(out)
    print("wrote", out)


face = transform.resize(data.astronaut(), (128, 128), anti_aliasing=True)[18:82, 30:94]
sheet_for(face, os.path.join(outdir, "upscale_compare.png"))
cup = transform.resize(data.coffee(), (100, 150), anti_aliasing=True)[30:94, 70:134]
sheet_for(cup, os.path.join(outdir, "upscale_texture.png"))
