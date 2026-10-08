#!/usr/bin/env python3
"""Generate the teaching images used by the AI Digital Imaging lectures.

Every image here is made from scratch or from scikit-image's bundled sample photos
(public domain or permissively licensed test images), so nothing copyrighted is
reproduced. Real generator output (hands, lettering, "sheen") is NOT faked here:
those slides carry an image slot for the instructor's own generated examples.

Run from the repo root:  python3 "AI Digital Imaging/build_decks/gen_images.py"
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from skimage import data, color, feature, transform, restoration, util

OUT = "AI Digital Imaging/images"
os.makedirs(OUT, exist_ok=True)
RNG = np.random.default_rng(7)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
INK = (43, 43, 43)
MUTE = (120, 120, 120)
ACCENT = (192, 80, 77)


def font(size, path=SANS):
    return ImageFont.truetype(path, size)


def to_img(a):
    a = np.clip(a, 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8))


def save(im, name):
    im.save(os.path.join(OUT, name))
    print("wrote", name, im.size)


def caption_strip(panels, labels, pad=24, lab_h=60, bg=(255, 255, 255), size=30):
    w = sum(p.width for p in panels) + pad * (len(panels) + 1)
    h = max(p.height for p in panels) + lab_h + pad * 2
    sheet = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(sheet)
    x = pad
    for p, lab in zip(panels, labels):
        sheet.paste(p.convert("RGB"), (x, pad))
        tw = d.textlength(lab, font=font(size))
        d.text((x + (p.width - tw) / 2, pad + p.height + 12), lab, fill=INK, font=font(size))
        x += p.width + pad
    return sheet


# ------------------------------------------------------------ 1. diffusion strip
def diffusion_strip():
    img = data.astronaut().astype(float) / 255
    img = transform.resize(img, (320, 320), anti_aliasing=True)
    noise = RNG.normal(0, 1, img.shape)
    steps = [0.0, 0.2, 0.45, 0.7, 0.88, 1.0]  # fraction of signal
    panels, labels = [], []
    for i, s in enumerate(steps):
        a = np.sqrt(s) * img + np.sqrt(1 - s) * (0.5 + 0.35 * noise)
        panels.append(to_img(a))
        labels.append(["pure noise", "step 10", "step 20", "step 30", "step 40", "step 50"][i])
    save(caption_strip(panels, labels), "diffusion_strip.png")


# ------------------------------------------------------------ 2. lit spheres
def shade_sphere(size, light, key_rgb, amb_rgb, bg_top, bg_bot, spec=0.35, soft=False, rim=False):
    h = w = size
    yy, xx = np.mgrid[0:h, 0:w]
    bg = np.zeros((h, w, 3))
    t = (yy / h)[..., None]
    bg = np.array(bg_top) * (1 - t) + np.array(bg_bot) * t
    cx, cy, r = w / 2, h * 0.47, size * 0.32
    nx = (xx - cx) / r
    ny = (yy - cy) / r
    inside = nx ** 2 + ny ** 2 <= 1
    nz = np.sqrt(np.clip(1 - nx ** 2 - ny ** 2, 0, 1))
    L = np.array(light, float)
    L /= np.linalg.norm(L)
    lam = np.clip(nx * L[0] + (-ny) * L[1] + nz * L[2], 0, 1)
    if soft:
        lam = 0.5 + 0.5 * (nx * L[0] + (-ny) * L[1] + nz * L[2])
        lam = np.clip(lam, 0, 1) ** 1.3
    H = L + np.array([0, 0, 1.0])
    H /= np.linalg.norm(H)
    sp = np.clip(nx * H[0] + (-ny) * H[1] + nz * H[2], 0, 1) ** 40 * spec
    base = np.array([0.82, 0.80, 0.78])
    col = base * (np.array(amb_rgb) + lam[..., None] * np.array(key_rgb)) + sp[..., None] * np.array(key_rgb)
    if rim:
        fres = (1 - nz) ** 3
        col = col + fres[..., None] * np.array(key_rgb) * 0.9
    # ground shadow (ellipse offset away from light)
    out = bg.copy()
    sx = cx - L[0] * r * 0.9
    sy = cy + r * 1.02
    sh = ((xx - sx) / (r * 1.1)) ** 2 + ((yy - sy) / (r * 0.22)) ** 2
    shadow = np.clip(1 - sh, 0, 1) ** 0.8 * (0.55 if not soft else 0.3)
    out = out * (1 - shadow[..., None])
    out[inside] = col[inside]
    # anti-alias edge
    im = to_img(out).filter(ImageFilter.SMOOTH)
    return im


def light_spheres():
    S = 300
    cases = [
        ("noon, overhead", [0.1, 0.95, 0.35], [1.0, 0.98, 0.95], [0.18, 0.2, 0.24], (0.75, 0.85, 0.95), (0.62, 0.6, 0.55), False, False),
        ("golden hour, low left", [-0.95, 0.15, 0.3], [1.0, 0.72, 0.42], [0.12, 0.14, 0.25], (0.98, 0.78, 0.55), (0.45, 0.35, 0.3), False, False),
        ("overcast, soft", [0.0, 0.8, 0.6], [0.78, 0.8, 0.82], [0.3, 0.32, 0.34], (0.8, 0.82, 0.84), (0.6, 0.6, 0.6), True, False),
        ("rim light, from behind", [0.2, 0.3, -0.9], [0.9, 0.95, 1.0], [0.05, 0.05, 0.08], (0.12, 0.13, 0.18), (0.05, 0.05, 0.07), False, True),
        ("night, warm practical", [0.9, -0.1, 0.4], [1.0, 0.62, 0.3], [0.05, 0.08, 0.2], (0.05, 0.07, 0.16), (0.08, 0.08, 0.12), False, False),
    ]
    panels, labels = [], []
    for lab, L, key, amb, top, bot, soft, rim in cases:
        panels.append(shade_sphere(S, L, key, amb, top, bot, soft=soft, rim=rim))
        labels.append(lab)
    save(caption_strip(panels, labels, size=24), "light_spheres.png")


# ------------------------------------------------------------ 3. lens compare
def lens_compare():
    def render(f, dist):
        W, H = 620, 380
        im = Image.new("RGB", (W, H), (245, 243, 238))
        d = ImageDraw.Draw(im)
        # floor line
        horizon = H * 0.42
        d.line([(0, horizon), (W, horizon)], fill=(200, 196, 188), width=2)
        pillars = []
        for i in range(6):
            z = dist + i * 3.0
            for side in (-1, 1):
                x = side * 2.2
                pillars.append((z, x))
        pillars.sort(reverse=True)
        cam_h = 1.0
        for z, x in pillars:
            def P(X, Y, Z):
                return (W / 2 + f * X / Z, horizon - f * (Y - cam_h) / Z)
            top = P(x, 3.2, z)
            bot = P(x, 0, z)
            half = f * 0.35 / z
            shade = int(90 + 120 * min(1, (z - dist) / 18))
            d.rectangle([bot[0] - half, top[1], bot[0] + half, bot[1]], fill=(shade, shade - 6, shade - 14), outline=(60, 60, 60))
        # figure at the front centre
        z = dist
        def P(X, Y, Z):
            return (W / 2 + f * X / Z, horizon - f * (Y - cam_h) / Z)
        head = P(0, 1.75, z)
        foot = P(0, 0, z)
        r = f * 0.12 / z
        d.ellipse([head[0] - r, head[1] - r, head[0] + r, head[1] + r], fill=ACCENT)
        d.line([head[0], head[1] + r, foot[0], foot[1]], fill=ACCENT, width=max(3, int(r * 0.6)))
        return im
    wide = render(260, 3.0)
    long = render(260 * 3.2, 3.0 * 3.2)
    save(caption_strip([wide, long], ["wide lens, close: depth stretches", "long lens, far back: depth compresses"], size=24), "lens_compare.png")


# ------------------------------------------------------------ 4. selection drives the result
def dashed_rect(d, box, dash=10, fill=(255, 255, 255), w=3):
    x0, y0, x1, y1 = box
    for x in range(int(x0), int(x1), dash * 2):
        d.line([(x, y0), (min(x + dash, x1), y0)], fill=fill, width=w)
        d.line([(x, y1), (min(x + dash, x1), y1)], fill=fill, width=w)
    for y in range(int(y0), int(y1), dash * 2):
        d.line([(x0, y), (x0, min(y + dash, y1))], fill=fill, width=w)
        d.line([(x1, y), (x1, min(y + dash, y1))], fill=fill, width=w)


def selection_panels():
    base = Image.fromarray(data.coffee()).resize((420, 280))
    boxes = [(150, 95, 270, 190), (95, 50, 330, 240), (10, 10, 410, 270)]
    labs = ["tight: it fills a small gap", "loose: it gets room to invent", "everything: you asked for a new picture"]
    panels = []
    for b in boxes:
        p = base.copy()
        d = ImageDraw.Draw(p)
        dashed_rect(d, (b[0] - 1, b[1] - 1, b[2] + 1, b[3] + 1), fill=(0, 0, 0), w=5)
        dashed_rect(d, b, fill=(255, 255, 255), w=3)
        panels.append(p)
    save(caption_strip(panels, labs, size=21), "selection_panels.png")


# ------------------------------------------------------------ 5. expand diagram
def expand_diagram():
    src = Image.fromarray(data.coffee()).resize((360, 240))
    W, H = 760, 428  # roughly 16:9
    im = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(im)
    for y in range(0, H, 20):
        for x in range(0, W, 20):
            if (x // 20 + y // 20) % 2 == 0:
                d.rectangle([x, y, x + 19, y + 19], fill=(225, 225, 225))
    ox, oy = (W - 360) // 2, (H - 240) // 2
    im.paste(src, (ox, oy))
    d.rectangle([ox, oy, ox + 359, oy + 239], outline=ACCENT, width=4)
    d.text((ox + 8, oy + 246), "the original photo (3:2)", fill=INK, font=font(20))
    d.text((14, 12), "16:9 canvas: everything grey gets invented", fill=INK, font=font(22))
    save(im, "expand_diagram.png")


# ------------------------------------------------------------ 6. checklist error plates
def error_light():
    W, H = 640, 400
    yy, xx = np.mgrid[0:H, 0:W]
    bg = np.ones((H, W, 3))
    t = (yy / H)[..., None]
    bg = np.array([0.86, 0.88, 0.9]) * (1 - t) + np.array([0.58, 0.55, 0.5]) * t
    bg[yy > H * 0.55] = (np.array([0.62, 0.58, 0.52]) * np.ones_like(bg))[yy > H * 0.55]
    out = bg.copy()
    def sphere(cx, cy, r, L):
        L = np.array(L, float); L /= np.linalg.norm(L)
        nx = (xx - cx) / r; ny = (yy - cy) / r
        ins = nx ** 2 + ny ** 2 <= 1
        nz = np.sqrt(np.clip(1 - nx ** 2 - ny ** 2, 0, 1))
        lam = np.clip(nx * L[0] - ny * L[1] + nz * L[2], 0, 1)
        col = np.array([0.8, 0.78, 0.75]) * (0.15 + 0.95 * lam[..., None])
        sx = cx - L[0] * r * 1.4; sy = cy + r * 0.95
        sh = ((xx - sx) / (r * 1.3)) ** 2 + ((yy - sy) / (r * 0.25)) ** 2
        s = np.clip(1 - sh, 0, 1) ** 0.7 * 0.55
        return ins, col, s
    for cx, L in ((190, [-0.9, 0.4, 0.3]), (450, [0.9, 0.4, 0.3])):
        ins, col, s = sphere(cx, 230, 70, L)
        out = out * (1 - s[..., None])
        out[ins] = col[ins]
    im = to_img(out).filter(ImageFilter.SMOOTH)
    d = ImageDraw.Draw(im)
    d.text((70, 330), "light from the left", fill=INK, font=font(20))
    d.text((360, 330), "light from the right", fill=ACCENT, font=font(20))
    d.text((150, 22), "same scene, two suns", fill=INK, font=font(24))
    save(im, "error_light.png")


def error_perspective():
    W, H = 640, 400
    im = Image.new("RGB", (W, H), (246, 244, 239))
    d = ImageDraw.Draw(im)
    vp = (320, 120)
    d.line([(0, 120), (W, 120)], fill=(180, 175, 165), width=2)
    for x in range(-600, 1300, 80):
        d.line([vp, (x, H)], fill=(200, 196, 188), width=1)
    for k in range(1, 9):
        y = 120 + (H - 120) * (k / 8) ** 1.8
        d.line([(0, y), (W, y)], fill=(200, 196, 188), width=1)
    # correct box on the left
    def box(front, w, h, vp, col):
        x0, y0 = front
        fl = [(x0, y0), (x0 + w, y0), (x0 + w, y0 - h), (x0, y0 - h)]
        k = 0.22
        back = [(px + (vp[0] - px) * k, py + (vp[1] - py) * k) for px, py in fl]
        for a, b in zip(fl, fl[1:] + fl[:1]):
            d.line([a, b], fill=col, width=3)
        for a, b in zip(back, back[1:] + back[:1]):
            d.line([a, b], fill=col, width=2)
        for a, b in zip(fl, back):
            d.line([a, b], fill=col, width=2)
    box((90, 330), 110, 90, vp, INK)
    box((420, 330), 110, 90, (560, 60), ACCENT)
    d.line([(420 + 110, 330 - 90), (560, 60)], fill=ACCENT, width=1)
    d.ellipse([vp[0] - 6, vp[1] - 6, vp[0] + 6, vp[1] + 6], fill=INK)
    d.ellipse([554, 54, 566, 66], fill=ACCENT)
    d.text((70, 350), "agrees with the floor", fill=INK, font=font(19))
    d.text((395, 350), "its own private horizon", fill=ACCENT, font=font(19))
    save(im, "error_perspective.png")


def error_repeat():
    g = data.grass().astype(float) / 255
    g = np.stack([g * 0.75, g * 0.95, g * 0.55], -1)
    g = transform.resize(g, (400, 640), anti_aliasing=True)
    patch = g[60:160, 80:200].copy()
    # mark the patch with a distinctive bright clump so the repeat is readable
    yy, xx = np.mgrid[0:100, 0:120]
    blob = np.exp(-(((xx - 60) / 18) ** 2 + ((yy - 50) / 12) ** 2))
    patch = patch + blob[..., None] * np.array([0.35, 0.3, 0.05])
    for (y, x) in ((40, 60), (40, 330), (230, 190), (230, 470), (150, 30)):
        g[y:y + 100, x:x + 120] = patch
    im = to_img(g)
    d = ImageDraw.Draw(im)
    for (y, x) in ((40, 60), (40, 330), (230, 190), (230, 470), (150, 30)):
        d.ellipse([x + 30, y + 22, x + 90, y + 78], outline=(255, 255, 255), width=3)
    save(im, "error_repeat.png")


def error_lettering():
    W, H = 640, 400
    im = Image.new("RGB", (W, H), (70, 60, 52))
    d = ImageDraw.Draw(im)
    d.rectangle([60, 90, 580, 300], fill=(232, 222, 198), outline=(40, 30, 25), width=6)
    f = font(78, SANS_B)
    # what the brief asked for
    d.text((60, 22), 'asked for: "OPEN DAILY"', fill=(240, 235, 225), font=font(24))
    # what came back: letter-shaped, not letters
    glyphs = ["O", "P", "Ǝ", "И", " ", "D", "A", "I", "Ļ", "Y"]
    x = 92
    for gch in glyphs:
        layer = Image.new("RGBA", (90, 110), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        ld.text((6, 4), gch, fill=(150, 40, 35, 255), font=f)
        layer = layer.rotate(RNG.uniform(-9, 9), resample=Image.BICUBIC)
        im.paste(layer, (x, int(140 + RNG.uniform(-10, 10))), layer)
        x += 48 if gch == " " else int(RNG.uniform(44, 56))
    d.text((60, 330), "letter-shaped marks, not letters", fill=(240, 235, 225), font=font(24))
    save(im, "error_lettering.png")


# ------------------------------------------------------------ 7. heal before / after
def heal_demo():
    img = data.coffee().astype(float) / 255
    img = transform.resize(img, (300, 450), anti_aliasing=True)
    yy, xx = np.mgrid[0:300, 0:450]
    # generator "mush": the spoon and saucer rim melt into the table
    bad = transform.swirl(img, center=(330, 225), strength=7, radius=60)
    # patched by hand: clone clean wood from above, feathered, then a second
    # pass restoring the original saucer rim from reference (the source photo)
    region = (((xx - 330) / 62) ** 2 + ((yy - 225) / 62) ** 2) <= 1
    soft = np.array(Image.fromarray((region * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))) / 255.0
    fixed = bad * (1 - soft[..., None]) + img * soft[..., None]
    marked = to_img(bad)
    d = ImageDraw.Draw(marked)
    d.ellipse([262, 160, 398, 292], outline=(230, 40, 40), width=4)
    d.text((262, 128), "1. rim melts", fill=(230, 40, 40), font=font(20, SANS_B))
    save(caption_strip([to_img(bad), marked, to_img(fixed)],
                       ["as generated", "callout layer", "patched by hand"], size=24), "heal_demo.png")


# ------------------------------------------------------------ 8. compositing: the four matches
def composite_demo():
    H, W = 360, 480
    g = data.brick().astype(float) / 255
    g = transform.resize(g, (H, W), anti_aliasing=True)
    xx = np.linspace(1.15, 0.65, W)[None, :]  # warm light from the left
    bgc = np.stack([g * 0.95, g * 0.78, g * 0.6], -1) * xx[..., None]
    grain = RNG.normal(0, 0.035, (H, W, 1))
    bgc = np.clip(bgc + grain, 0, 1)
    yy, xg = np.mgrid[0:H, 0:W]

    def put_sphere(img, L, tint, add_grain, soft_edge, contact):
        out = img.copy()
        cx, cy, r = 250, 210, 80
        L = np.array(L, float); L /= np.linalg.norm(L)
        nx = (xg - cx) / r; ny = (yy - cy) / r
        d2 = nx ** 2 + ny ** 2
        nz = np.sqrt(np.clip(1 - d2, 0, 1))
        lam = np.clip(nx * L[0] - ny * L[1] + nz * L[2], 0, 1)
        col = np.array([0.85, 0.85, 0.85]) * (0.12 + lam[..., None] * np.array(tint))
        if add_grain:
            col = col + RNG.normal(0, 0.035, (H, W, 1))
        if contact:
            sh = ((xg - (cx + 40)) / (r * 1.25)) ** 2 + ((yy - (cy + r * 0.95)) / (r * 0.2)) ** 2
            s = np.clip(1 - sh, 0, 1) ** 0.6 * 0.6
            out = out * (1 - s[..., None])
        if soft_edge:
            alpha = np.clip((1 - np.sqrt(d2)) * r / 2.0, 0, 1)
        else:
            alpha = (d2 <= 1).astype(float)
        return out * (1 - alpha[..., None]) + col * alpha[..., None]

    pasted = put_sphere(bgc, [0.8, 0.5, 0.4], [0.75, 0.85, 1.05], False, False, False)
    matched = put_sphere(bgc, [-0.85, 0.35, 0.4], [1.05, 0.85, 0.62], True, True, True)
    a, b = to_img(pasted), to_img(matched)
    save(caption_strip([a, b], ["pasted on", "sitting in"], size=26), "composite_demo.png")
    # grain + edge zoom
    za = a.crop((300, 160, 360, 220)).resize((300, 300), Image.NEAREST)
    zb = b.crop((300, 160, 360, 220)).resize((300, 300), Image.NEAREST)
    save(caption_strip([za, zb], ["clean, hard edge", "grain + soft edge"], size=24), "composite_zoom.png")


# ------------------------------------------------------------ 9. control inputs
def control_inputs():
    S = 300
    # rough sketch
    sk = Image.new("RGB", (S, S), (250, 249, 245))
    d = ImageDraw.Draw(sk)
    for j in range(3):
        o = RNG.uniform(-3, 3, 8)
        d.ellipse([125 + o[0], 40 + o[1], 175 + o[2], 92 + o[3]], outline=(60, 60, 60), width=2)
        d.line([(150 + o[4], 92), (145 + o[5], 190)], fill=(60, 60, 60), width=2)
        d.line([(148, 120), (95 + o[6], 160)], fill=(60, 60, 60), width=2)
        d.line([(148, 118), (210 + o[7], 85)], fill=(60, 60, 60), width=2)
        d.line([(145, 190), (110 + o[0], 270)], fill=(60, 60, 60), width=2)
        d.line([(145, 190), (190 + o[1], 268)], fill=(60, 60, 60), width=2)
    d.line([(20, 272), (280, 272)], fill=(120, 120, 120), width=2)
    # pose skeleton
    ps = Image.new("RGB", (S, S), (0, 0, 0))
    d = ImageDraw.Draw(ps)
    J = {"head": (150, 62), "neck": (150, 100), "rs": (122, 104), "re": (100, 140), "rh": (95, 160),
         "ls": (178, 104), "le": (196, 90), "lh": (210, 85), "hip": (146, 190), "rk": (125, 230),
         "ra": (110, 270), "lk": (170, 232), "la": (190, 268)}
    bones = [("head", "neck", (255, 0, 0)), ("neck", "rs", (255, 120, 0)), ("rs", "re", (255, 200, 0)),
             ("re", "rh", (200, 255, 0)), ("neck", "ls", (0, 255, 0)), ("ls", "le", (0, 255, 150)),
             ("le", "lh", (0, 220, 255)), ("neck", "hip", (0, 120, 255)), ("hip", "rk", (60, 0, 255)),
             ("rk", "ra", (150, 0, 255)), ("hip", "lk", (255, 0, 200)), ("lk", "la", (255, 0, 100))]
    for a, b, c in bones:
        d.line([J[a], J[b]], fill=c, width=7)
    for p in J.values():
        d.ellipse([p[0] - 5, p[1] - 5, p[0] + 5, p[1] + 5], fill=(255, 255, 255))
    # depth map of primitives
    yy, xx = np.mgrid[0:S, 0:S]
    depth = np.clip(0.15 + 0.65 * (yy / S), 0, 1)  # floor nearer at bottom
    depth[yy < S * 0.45] = 0.12
    for cx, cy, r, near in ((95, 190, 55, 0.8), (205, 160, 40, 0.55)):
        nx = (xx - cx) / r; ny = (yy - cy) / r
        ins = nx ** 2 + ny ** 2 <= 1
        nz = np.sqrt(np.clip(1 - nx ** 2 - ny ** 2, 0, 1))
        depth[ins] = (near + 0.18 * nz)[ins]
    dp = to_img(np.stack([depth] * 3, -1))
    # edge map from a photo
    gray = color.rgb2gray(data.astronaut())
    gray = transform.resize(gray, (S, S), anti_aliasing=True)
    ed = feature.canny(gray, sigma=2.0)
    em = to_img(np.stack([ed.astype(float)] * 3, -1))
    save(caption_strip([sk, ps, dp, em], ["a sketch", "a pose", "a depth map", "an edge map"], size=24),
         "control_inputs.png")


# ------------------------------------------------------------ 10. value check
def value_check():
    img = data.coffee().astype(float) / 255
    img = transform.resize(img, (280, 420), anti_aliasing=True)
    gray = color.rgb2gray(img)
    three = np.digitize(gray, [0.33, 0.62])
    three = np.array([0.15, 0.5, 0.88])[three]
    save(caption_strip([to_img(img), to_img(np.stack([gray] * 3, -1)), to_img(np.stack([three] * 3, -1))],
                       ["color", "gray (the check layer)", "three values"], size=24), "value_check.png")


# ------------------------------------------------------------ 11. GDC survey chart
def gdc_chart():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "DejaVu Serif"
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
    years = ["2024 report", "2025 report", "2026 report"]
    vals = [18, 30, 52]
    bars = ax.bar(years, vals, color=["#bdb6a8", "#a99f8c", "#c0504d"], width=0.55)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v}%", ha="center", fontsize=18, color="#2b2b2b")
    ax.set_ylim(0, 65)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="x", labelsize=15, colors="#2b2b2b")
    ax.set_title("Game developers who say generative AI is having\na negative impact on the industry", fontsize=16, color="#2b2b2b")
    fig.text(0.01, 0.01, "Source: GDC State of the Game Industry reports (2026 report: 2,300+ respondents)", fontsize=10, color="#777")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(os.path.join(OUT, "gdc_chart.png"), facecolor="white")
    print("wrote gdc_chart.png")


# ------------------------------------------------------------ 12. one-word sweep (light) for prompt session
def one_variable_sweep():
    # same sphere, only the light word changes: reuse light_spheres; here make a 3-up "seed" idea
    S = 260
    panels = []
    for L in ([-0.9, 0.3, 0.4], [-0.6, 0.6, 0.5], [-0.95, 0.1, 0.25]):
        panels.append(shade_sphere(S, L, [1.0, 0.72, 0.42], [0.12, 0.14, 0.25], (0.98, 0.78, 0.55), (0.45, 0.35, 0.3)))
    save(caption_strip(panels, ["try 1", "try 2", "try 3"], size=22), "same_prompt_three_tries.png")


# ------------------------------------------------------------ 13. type on images
def _poster_base(w=420, h=600):
    img = data.rocket().astype(float) / 255  # NASA photo, public domain
    img = transform.resize(img, (h, int(img.shape[1] * h / img.shape[0])), anti_aliasing=True)
    x0 = (img.shape[1] - w) // 2 + 40
    return to_img(img[:, x0:x0 + w])


def type_hierarchy():
    bad = _poster_base()
    d = ImageDraw.Draw(bad)
    d.text((140, 300), "LAUNCH WEEK", fill=(200, 200, 200), font=font(26, SERIF))
    d.text((120, 335), "a festival of small films", fill=(230, 210, 120), font=font(22, SANS_B))
    d.text((150, 365), "Oct 3 to 9  |  Main Hall", fill=(255, 255, 255), font=font(20, SANS))
    d.text((60, 560), "tickets at the door", fill=(255, 120, 120), font=font(22, SERIF))
    good = _poster_base()
    ov = Image.new("RGBA", good.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for y in range(0, 230):
        od.line([(0, y), (good.width, y)], fill=(10, 14, 30, int(170 * (1 - y / 230))))
    good = Image.alpha_composite(good.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(good)
    d.text((28, 30), "LAUNCH", fill=(255, 255, 255), font=font(72, SANS_B))
    d.text((30, 110), "WEEK", fill=(255, 255, 255), font=font(72, SANS_B))
    d.text((32, 196), "a festival of small films", fill=(235, 235, 235), font=font(22, SERIF))
    d.rectangle([0, 548, good.width, 600], fill=(15, 15, 20))
    d.text((24, 562), "OCT 3 TO 9   MAIN HALL   TICKETS AT THE DOOR", fill=(220, 220, 220), font=font(15, SANS))
    save(caption_strip([bad, good], ["four sizes, no order", "one thing first"], size=26), "type_hierarchy.png")


def type_on_busy():
    base = data.brick().astype(float) / 255
    base = transform.resize(base, (240, 360), anti_aliasing=True)
    base = to_img(np.stack([base * 0.95, base * 0.8, base * 0.62], -1))
    panels, labels = [], []
    word = "CHAPTER III"
    f = font(40, SANS_B)
    # 1 nothing
    p = base.copy(); d = ImageDraw.Draw(p)
    d.text((40, 95), word, fill=(235, 225, 210), font=f)
    panels.append(p); labels.append("as is")
    # 2 gradient
    p = base.convert("RGBA"); ov = Image.new("RGBA", p.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    for y in range(240):
        a = int(200 * max(0, 1 - abs(y - 115) / 90))
        od.line([(0, y), (360, y)], fill=(15, 10, 8, a))
    p = Image.alpha_composite(p, ov).convert("RGB"); d = ImageDraw.Draw(p)
    d.text((40, 95), word, fill=(245, 238, 225), font=f)
    panels.append(p); labels.append("darken behind")
    # 3 blur
    p = base.copy(); band = p.crop((0, 75, 360, 160)).filter(ImageFilter.GaussianBlur(7))
    p.paste(band, (0, 75)); d = ImageDraw.Draw(p)
    d.text((40, 95), word, fill=(255, 250, 240), font=f)
    panels.append(p); labels.append("soften the area")
    # 4 band
    p = base.copy(); d = ImageDraw.Draw(p)
    d.rectangle([0, 82, 360, 152], fill=(30, 24, 20))
    d.text((40, 95), word, fill=(240, 232, 218), font=f)
    panels.append(p); labels.append("a solid band")
    save(caption_strip(panels, labels, size=22), "type_on_busy.png")


# ------------------------------------------------------------ 14. presentation sheet mockup
def presentation_sheet():
    W, H = 1600, 1000
    im = Image.new("RGB", (W, H), (248, 247, 243))
    d = ImageDraw.Draw(im)
    d.text((60, 40), "CHAPTER HEADERS FOR A BOOK", fill=INK, font=font(34, SANS_B))
    d.text((60, 86), "Final series  |  student name  |  date", fill=MUTE, font=font(20))
    # three finals
    cases = [([-0.95, 0.15, 0.3], [1.0, 0.72, 0.42], [0.12, 0.14, 0.25], (0.98, 0.78, 0.55), (0.45, 0.35, 0.3)),
             ([0.1, 0.95, 0.35], [1.0, 0.98, 0.95], [0.18, 0.2, 0.24], (0.75, 0.85, 0.95), (0.62, 0.6, 0.55)),
             ([0.9, -0.1, 0.4], [1.0, 0.62, 0.3], [0.05, 0.08, 0.2], (0.05, 0.07, 0.16), (0.08, 0.08, 0.12))]
    x = 60
    for L, key, amb, top, bot in cases:
        sph = shade_sphere(440, L, key, amb, top, bot).crop((0, 60, 440, 360))
        im.paste(sph, (x, 140))
        x += 470
    d.text((60, 452), "FINAL IMAGES", fill=ACCENT, font=font(18, SANS_B))
    # process strip
    d.text((60, 510), "PROCESS: CHAPTER I", fill=ACCENT, font=font(18, SANS_B))
    stages = ["brief", "generated", "callouts", "fixed", "final + type"]
    x = 60
    for i, st in enumerate(stages):
        L, key, amb, top, bot = cases[0]
        tile = shade_sphere(180, L, key, amb, top, bot).crop((0, 25, 180, 145))
        if st == "brief":
            tile = Image.new("RGB", (180, 120), (235, 232, 225)); td = ImageDraw.Draw(tile)
            for k in range(6):
                td.line([(14, 18 + k * 16), (166 - (k % 3) * 30, 18 + k * 16)], fill=MUTE, width=3)
        if st == "final + type":
            td = ImageDraw.Draw(tile); td.text((12, 6), "CHAPTER I", fill=(255, 255, 255), font=font(18, SANS_B))
        if st == "callouts":
            td = ImageDraw.Draw(tile); td.ellipse([55, 25, 125, 95], outline=(230, 40, 40), width=3)
        im.paste(tile, (x, 545))
        d.text((x, 670), st, fill=INK, font=font(18))
        if i < len(stages) - 1:
            d.text((x + 186, 590), ">", fill=MUTE, font=font(28, SANS_B))
        x += 215
    # log excerpt + disclosure
    d.rectangle([1150, 510, 1540, 700], outline=(200, 196, 188), width=2)
    d.text((1166, 522), "PROMPT LOG, EXCERPT", fill=ACCENT, font=font(16, SANS_B))
    for k, line in enumerate(["v3: light low left, warm", "  kept: matches board", "v4: added fog", "  rejected: hides the scarf"]):
        d.text((1166, 556 + k * 30), line, fill=INK, font=font(17))
    d.rectangle([60, 740, 1540, 940], outline=(200, 196, 188), width=2)
    d.text((76, 752), "DISCLOSURE", fill=ACCENT, font=font(16, SANS_B))
    for k in range(4):
        d.line([(76, 800 + k * 32), (1500 - (k % 2) * 220, 800 + k * 32)], fill=(190, 186, 178), width=4)
    save(im, "presentation_sheet.png")


if __name__ == "__main__":
    diffusion_strip()
    light_spheres()
    lens_compare()
    selection_panels()
    expand_diagram()
    error_light()
    error_perspective()
    error_repeat()
    error_lettering()
    heal_demo()
    composite_demo()
    control_inputs()
    value_check()
    gdc_chart()
    one_variable_sweep()
    type_hierarchy()
    type_on_busy()
    presentation_sheet()
