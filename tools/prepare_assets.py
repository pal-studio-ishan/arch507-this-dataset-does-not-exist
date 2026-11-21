"""Copy each student's final images and dataset samples out of Dropbox into web-sized files.

Writes:
  assets/<slug>/final/NN.jpg      full view (max 2000 px)
  assets/<slug>/final/NN_t.jpg    grid thumbnail (max 800 px)
  assets/<slug>/<dataset>/NN.jpg  dataset thumbnail (max 240 px), unless thumbs are off
  assets/<slug>/<dataset>-captions.txt  every caption, numbered
  data/assets.json                what was written, read by build.py

The originals in Dropbox are only read, never changed.
Run:  python -I tools/prepare_assets.py
"""
import io, json, os, re, sys, zipfile
from pathlib import Path
from PIL import Image

SRC = Path(r"C:\Users\ishanpal\University of Michigan Dropbox\Ishan Pal Singh\TEACHING\ARCH 507 - GenAI\Assignments\Student Work")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")

# finals: folder, zip, or ("pdf", path, [image names in order])
# datasets: (key, zip-or-folder, show_thumbs)
STUDENTS = {
    "angelica-facey": {
        "finals": "Angelica Facey/FINAL_REVIEW_Angelica Facey/1_Final Images",
        "datasets": [("forest", "Angelica Facey/FINAL_REVIEW_Angelica Facey/dataset_1", True),
                     ("mountain", "Angelica Facey/FINAL_REVIEW_Angelica Facey/dataset_2", True)],
    },
    "arushi-chopra": {
        "finals": "Arushi Chopra/ArushiChopra_ThisDatasetDoesNotExist/12 Final Images",
        "datasets": [("bamboo", "Arushi Chopra/ArushiChopra_ThisDatasetDoesNotExist/bamboo details dataset.zip", True)],
    },
    "emily-naumann": {
        "finals": "Emily Naumann/final assignment",
        "datasets": [("hoos", "Emily Naumann/final assignment/Lora 1/dataset1.zip", True),
                     ("disasterpiece", "Emily Naumann/final assignment/Lora 2/dataset2.zip", True),
                     ("minm", "Emily Naumann/final assignment/Lora 3/dataset3.zip", True)],
    },
    "frank-michel": {
        "finals": "Frank Michel/Final Photos",
        "datasets": [("soviet-interiors", "Frank Michel/LORA1.zip", True)],
    },
    "hua-lin": {
        "finals": "Hua Lin (Dylan)/Final-Dylan/images",
        "datasets": [("dogma", "Hua Lin (Dylan)/Final-Dylan/aatraining.zip", True)],
    },
    "itamar-yahav": {
        "finals": "Itamar Yahav/ASSIGNMENT_5/12_Final_Images",
        "datasets": [("pencil-drawing", "Itamar Yahav/ASSIGNMENT_5/pencil_drawing_LoRAs_dataset", True),
                     ("renders-first-try", "Itamar Yahav/Image_Dataset_IY.zip", True)],
    },
    "jack-barbour": {
        "finals": "Jack Barbour/Barbour_FinalWork/FinalImages.zip",
        "datasets": [("facade-closeups", "Jack Barbour/Barbour_FinalWork/DataSet_Barb1.zip", True),
                     ("brick-buildings", "Jack Barbour/Barbour_FinalWork/DataSet_Barb2.zip", True)],
    },
    "jack-smith": {
        "finals": "Jack Smith/FINAL/original presentation images",
        "datasets": [],
    },
    "leo-georges": {
        "finals": ("pdf", "Leo Georges/This Dataset Does Not Exist/ARCH 507 GENAI FINAL LEO GEORGES.pdf",
                   [(9, "Image25.jpg"), (10, "Image26.jpg"), (11, "Image27.jpg"), (13, "Image28.jpg"), (14, "Image29.jpg"),
                    (15, "Image30.jpg"), (17, "Image31.jpg"), (18, "Image32.jpg"), (19, "Image33.jpg"), (21, "Image34.jpg"),
                    (22, "Image20.jpg"), (23, "Image35.jpg")]),
        "datasets": [("mullions", "Leo Georges/This Dataset Does Not Exist/Molean Dataset.zip", True),
                     ("dunes", "Leo Georges/This Dataset Does Not Exist/Sand Dataset.zip", True)],
    },
    "michael-natinsky": {
        "finals": "Michael Natinsky/Final Project/Output.zip",
        "datasets": [("patelski", "Michael Natinsky/Final Project/Sander Patelski Elevation.zip", True),
                     ("elevations", "Michael Natinsky/Final Project/Elevation.zip", True)],
    },
    "ravi-kumar": {
        "finals": "Ravi Kumar/Final/Final Images",
        "datasets": [("lineart-elevations", "Ravi Kumar/Final/katropalop.zip", True),
                     ("elevation-photos", "Ravi Kumar/Final/wikiwikiwoo.zip", True)],
    },
    "riley-montgomery": {
        "finals": "Riley Montgomery/RileyMontgomery_Final/final images",
        "datasets": [],
    },
    "shuyang-zhang": {
        "finals": "Shuyang Zhang/Final_Review/Final_Outcomes",
        "datasets": [("contrasts", "Shuyang Zhang/Final_Review/Dataset/10pictures.zip", False)],
    },
    "tamer-tubishat": {
        "finals": "Tamer Tubishat/Tamer_Final Assignment's Materials/Tamer Tubishat_12 Images",
        "datasets": [("as-salt", "Tamer Tubishat/Tamer_Final Assignment's Materials/Tamer Tubishat_As-Salt city dataset.zip", True)],
    },
    "yewon-seo": {
        "finals": "Yewon Seo/Final Images",
        "datasets": [("style-sanaa", "Yewon Seo/LoRA.zip", True),
                     ("form-lamp", "Yewon Seo/LoRA 2.zip", True)],
    },
}


def natural(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def strip_rtf(text):
    if not text.lstrip().startswith("{\\rtf"):
        return text
    text = re.sub(r"\\'[0-9a-f]{2}", "", text)
    text = re.sub(r"\{\\\*[^{}]*\}", "", text)
    text = re.sub(r"\{\\(fonttbl|colortbl|stylesheet|info)[^{}]*(\{[^{}]*\}[^{}]*)*\}", "", text)
    text = re.sub(r"\\[a-zA-Z]+-?\d* ?", "", text)
    text = text.replace("{", "").replace("}", "").replace("\\", "")
    return re.sub(r"\s+", " ", text).strip()


def items_from(path):
    """Return sorted [(name, bytes_loader)] for images, and {stem: caption} for captions."""
    p = SRC / path
    imgs, caps = [], {}
    if p.suffix.lower() == ".zip":
        zf = zipfile.ZipFile(p)
        for n in zf.namelist():
            if n.endswith("/") or "__MACOSX" in n or os.path.basename(n).startswith("."):
                continue
            stem, ext = os.path.splitext(os.path.basename(n))
            if ext.lower() in IMG_EXT:
                imgs.append((os.path.basename(n), (lambda n=n: zf.read(n))))
            elif ext.lower() in (".txt", ".rtf"):
                caps[stem] = strip_rtf(zf.read(n).decode("utf-8", "replace")).strip()
    else:
        for f in p.iterdir():
            if f.suffix.lower() in IMG_EXT:
                imgs.append((f.name, (lambda f=f: f.read_bytes())))
            elif f.suffix.lower() in (".txt", ".rtf"):
                caps[f.stem] = strip_rtf(f.read_text("utf-8", "replace")).strip()
    imgs.sort(key=lambda t: natural(t[0]))
    return imgs, caps


def save(img_bytes_or_img, dest, max_px, quality):
    im = img_bytes_or_img if isinstance(img_bytes_or_img, Image.Image) else Image.open(io.BytesIO(img_bytes_or_img))
    im = im.convert("RGB")
    im.thumbnail((max_px, max_px), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)
    return im.size


def main(only=None):
    manifest_path = ROOT / "data" / "assets.json"
    manifest = json.loads(manifest_path.read_text("utf-8")) if manifest_path.exists() else {}
    for slug, cfg in STUDENTS.items():
        if only and slug not in only:
            continue
        entry = {"finals": [], "datasets": {}}
        # finals
        f = cfg["finals"]
        if isinstance(f, tuple) and f[0] == "pdf":
            import pypdf
            reader = pypdf.PdfReader(SRC / f[1])
            sources = []
            for page_no, name in f[2]:
                im = next(i for i in reader.pages[page_no - 1].images if i.name == name)
                sources.append((name, (lambda im=im: im.data)))
        else:
            sources, _ = items_from(f)
        for i, (name, load) in enumerate(sources, 1):
            data = load()
            big = OUT / slug / "final" / f"{i:02d}.jpg"
            w, h = save(data, big, 2000, 86)
            save(data, OUT / slug / "final" / f"{i:02d}_t.jpg", 800, 80)
            entry["finals"].append({"file": f"{i:02d}", "w": w, "h": h, "source": name})
        # datasets
        for key, path, show in cfg["datasets"]:
            imgs, caps = items_from(path)
            d = {"count": len(imgs), "thumbs": [], "captions": [], "show_thumbs": show}
            lines = []
            for i, (name, load) in enumerate(imgs, 1):
                cap = caps.get(os.path.splitext(name)[0], "")
                d["captions"].append(cap)
                lines.append(f"{i:02d}  {cap if cap else '(no caption)'}")
                if show and i <= 12:
                    save(load(), OUT / slug / key / f"{i:02d}.jpg", 240, 78)
                    d["thumbs"].append(f"{i:02d}")
            (OUT / slug).mkdir(parents=True, exist_ok=True)
            (OUT / slug / f"{key}-captions.txt").write_text("\n\n".join(lines) + "\n", "utf-8")
            entry["datasets"][key] = d
        manifest[slug] = entry
        print(f"{slug}: {len(entry['finals'])} finals, " + ", ".join(f"{k}={v['count']}" for k, v in entry["datasets"].items()), flush=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=1), "utf-8")


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
