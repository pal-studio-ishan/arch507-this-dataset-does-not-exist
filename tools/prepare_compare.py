"""Turn the 'one prompt, every LoRA' renders into site images, contact sheets and data/compare.json.

The renders come from ComfyUI (output/ARCH507_portland): base FLUX.1 [dev] plus every LoRA, same prompt,
seed and settings, with each LoRA's trigger word added.
  compare/NN_<lora>_*.png       every LoRA at strength 1.0
  compare_rec/NN_<lora>_*.png   LoRAs whose recommended strength isn't 1.0, at that strength

  python -I tools/prepare_compare.py            publish the 1.0 set
  python -I tools/prepare_compare.py --rec      also publish the recommended-strength set
"""
import json, re, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import parse, CONTENT, ROOT  # noqa: E402
from upload_hf import FILES  # noqa: E402

OUT = Path(r"C:\Users\ishanpal\Documents\ComfyUI\output\ARCH507_portland")
DEST = ROOT / "assets" / "compare"
PROMPT = ("an architecture magazine photo of an apartment inside the ruins of a park in central portland, designed in the style of "
          "peter zumthor and kengo kuma, with lots of concrete walls and cut-throughs to weathered stone structures. people are "
          "sitting at tables on an outdoor terrace overlooking the ocean.")
SETTINGS = "FLUX.1 [dev] fp8 · seed 507507 · 28 steps · guidance 3.5 · euler / simple · 1344×768"


def rec_strength(text):
    """Strength the student recommended; for a range, the middle of it (rounded to 0.05). No figure given: 1.0."""
    m = re.search(r"(\d+(?:\.\d+)?)(?:\s*[–-]\s*(\d+(?:\.\d+)?))?", text or "")
    if not m:
        return 1.0
    a = float(m.group(1))
    v = (a + float(m.group(2))) / 2 if m.group(2) else a
    return round(v * 20) / 20


def latest(prefix):
    files = sorted((OUT / prefix).parent.glob(Path(prefix).name + "_*.png"), key=lambda p: p.stat().st_mtime)
    if not files:
        raise SystemExit(f"missing render: {prefix}")
    return files[-1]


def items(rec):
    out = [{"src": latest("compare/00_base"), "slug": "", "name": "FLUX.1 [dev]", "lora": "no LoRA", "strength": None}]
    n = 0
    for p in sorted((CONTENT / "students").glob("*.md")):
        meta, _ = parse(p)
        for l in meta["lora"]:
            n += 1
            l = l + [""] * (5 - len(l))
            stem = FILES[l[0]][1][:-len(".safetensors")]
            s = rec_strength(l[4]) if rec else 1.0
            src = latest(f"compare_rec/{n:02d}_{stem}") if s != 1.0 else latest(f"compare/{n:02d}_{stem}")
            out.append({"src": src, "slug": p.stem, "name": meta["name"], "lora": l[1], "strength": s, "range": l[4]})
    return out


def sheet(its, path, title, sub):
    F = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 22)
    FS = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 17)
    cols, tw = 4, 620
    th = round(tw * 768 / 1344)
    pad, lab, headh = 14, 34, 86
    rows = -(-len(its) // cols)
    im = Image.new("RGB", (cols * tw + (cols + 1) * pad, headh + rows * (th + lab + pad) + pad), (12, 12, 12))
    d = ImageDraw.Draw(im)
    d.text((pad, 18), title, font=F, fill=(236, 236, 236))
    d.text((pad, 50), sub, font=FS, fill=(150, 150, 150))
    for i, it in enumerate(its):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + pad), headh + r * (th + lab + pad)
        im.paste(Image.open(it["src"]).convert("RGB").resize((tw, th), Image.LANCZOS), (x, y))
        s = "" if it["strength"] is None else f" · {it['strength']:g}"
        d.text((x, y + th + 7), f"{it['name']} · {it['lora']}{s}", font=FS, fill=(236, 236, 236))
    im.save(path, quality=88)


def publish(key, title, its, sub):
    d = DEST / key
    d.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, it in enumerate(its):
        im = Image.open(it["src"]).convert("RGB")
        f = f"{i:02d}"
        im.save(d / f"{f}.jpg", quality=88)
        im.resize((672, 384), Image.LANCZOS).save(d / f"{f}_t.jpg", quality=84)
        rows.append({"file": f, "slug": it["slug"], "name": it["name"], "lora": it["lora"], "strength": it["strength"]})
    sheet(its, d / "sheet.jpg", f"One prompt, every LoRA · {title}", sub)
    return {"key": key, "title": title, "settings": sub, "items": rows}


def main():
    sets = [publish("strength-1", "every LoRA at 1.0", items(False), SETTINGS + " · every LoRA at 1.0")]
    if "--rec" in sys.argv:
        sets.append(publish("recommended", "at each student's strength", items(True),
                            SETTINGS + " · each LoRA at its student's recommended strength (middle of their range)"))
    data = {"prompt": PROMPT, "sets": sets}
    (ROOT / "data" / "compare.json").write_text(json.dumps(data, indent=1, ensure_ascii=False), "utf-8")
    print("published sets:", [s["key"] for s in sets])


if __name__ == "__main__":
    main()
