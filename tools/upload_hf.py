"""Publish each project's LoRAs to Hugging Face: one model repo per project, with a model card and example images.

Uploads straight from the course Dropbox (no copies) and gives each file a clear name.
Repos are created PRIVATE; flip them public once students have agreed (see --public).
Writes data/downloads.json so the site's Download buttons point at the files.

  python -I tools/upload_hf.py --dry-run     write model cards to data/hf_cards/ only
  python -I tools/upload_hf.py               create/update repos and upload
  python -I tools/upload_hf.py --public      make every repo public
Needs a one-time `hf auth login` with a write token.
"""
import io, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import parse, CONTENT, ROOT, ASSETS  # noqa: E402

USER = "pal13"
COLLECTION_TITLE = "ARCH 507 — This Dataset Does Not Exist"
SITE = "https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/"
SRC = Path(r"C:\Users\ishanpal\University of Michigan Dropbox\Ishan Pal Singh\TEACHING\ARCH 507 - GenAI\Assignments\Student Work")

# original file name (as in the student's content file) -> (path under SRC, name on Hugging Face)
FILES = {
    "C_at_el.safetensors": ("Angelica Facey/FINAL_REVIEW_Angelica Facey/2_LoRA models/C_at_el.safetensors", "angelica-facey_C_at_el.safetensors"),
    "YO_c_me_T.safetensors": ("Angelica Facey/FINAL_REVIEW_Angelica Facey/2_LoRA models/YO_c_me_T.safetensors", "angelica-facey_YO_c_me_T.safetensors"),
    "borsch_t.safetensors": ("Arushi Chopra/ArushiChopra_ThisDatasetDoesNotExist/LoRAs/borsch_t.safetensors", "arushi-chopra_borsch_t.safetensors"),
    "too_late_pytorch_lora_weights.safetensors": ("Arushi Chopra/ArushiChopra_ThisDatasetDoesNotExist/LoRAs/too_late_pytorch_lora_weights.safetensors", "arushi-chopra_too_late.safetensors"),
    "hoos.safetensors": ("Emily Naumann/final assignment/Lora 1/hoos.safetensors", "emily-naumann_hoos.safetensors"),
    "disasterpiece.safetensors": ("Emily Naumann/final assignment/Lora 2/disasterpiece.safetensors", "emily-naumann_disasterpiece.safetensors"),
    "minm": ("Emily Naumann/final assignment/Lora 3/minm", "emily-naumann_minm.safetensors"),
    "Lora-Justdoit.safetensors": ("Hua Lin (Dylan)/Final-Dylan/Lora-Justdoit.safetensors", "hua-lin_justdoit.safetensors"),
    "pencil_drawing.safetensors": ("Itamar Yahav/ASSIGNMENT_5/pencil_drawing.safetensors", "itamar-yahav_pencil_drawing.safetensors"),
    "peptides_flux.safetensors": ("Itamar Yahav/peptides_flux.safetensors", "itamar-yahav_peptides_first-try.safetensors"),
    "bnajS-FZIGxwpbwttX7GC_pytorch_lora_weights.safetensors": ("Jack Barbour/Barbour_FinalWork/bnajS-FZIGxwpbwttX7GC_pytorch_lora_weights.safetensors", "jack-barbour_brick-buildings.safetensors"),
    "Kz94z-4KsFaMTVGdWZotT_pytorch_lora_weights.safetensors": ("Jack Barbour/Barbour_FinalWork/Kz94z-4KsFaMTVGdWZotT_pytorch_lora_weights.safetensors", "jack-barbour_brick-facade-closeups.safetensors"),
    "sandmolean_pytorch_lora_weights.safetensors": ("Leo Georges/This Dataset Does Not Exist/sandmolean_pytorch_lora_weights.safetensors", "leo-georges_mullions.safetensors"),
    "moleansand_pytorch_lora_weights.safetensors": ("Leo Georges/This Dataset Does Not Exist/moleansand_pytorch_lora_weights.safetensors", "leo-georges_dunes.safetensors"),
    "Patelski.safetensors": ("Michael Natinsky/Final Project/Patelski.safetensors", "michael-natinsky_patelski.safetensors"),
    "Elevations.safetensors": ("Michael Natinsky/Final Project/Elevations.safetensors", "michael-natinsky_elevations.safetensors"),
    "stoneybaloney.safetensors": ("Ravi Kumar/Final/stoneybaloney.safetensors", "ravi-kumar_stoneybaloney.safetensors"),
    "katropalop.safetensors": ("Ravi Kumar/Final/katropalop.safetensors", "ravi-kumar_katropalop.safetensors"),
    "wikiwikiwoo.safetensors": ("Ravi Kumar/Final/wikiwikiwoo.safetensors", "ravi-kumar_wikiwikiwoo.safetensors"),
    "mont2.safetensors": ("Riley Montgomery/RileyMontgomery_Final/mont2.safetensors", "riley-montgomery_mont2.safetensors"),
    "lkjh.safetensors": ("Riley Montgomery/RileyMontgomery_Final/lkjh.safetensors", "riley-montgomery_lkjh.safetensors"),
    "mont3.safetensors": ("Riley Montgomery/RileyMontgomery_Final/mont3.safetensors", "riley-montgomery_mont3.safetensors"),
    "Tamer Tubishat_LoRA_As-Salt city of stairs and yellow stone.safetensors": ("Tamer Tubishat/Tamer_Final Assignment's Materials/Tamer Tubishat_LoRA_As-Salt city of stairs and yellow stone.safetensors", "tamer-tubishat_architamer.safetensors"),
    "FLUX 1_LORA_asdf.safetensors": ("Yewon Seo/FLUX 1_LORA_asdf.safetensors", "yewon-seo_asdf-style.safetensors"),
    "FLUX 1_LORA_qwer.safetensors": ("Yewon Seo/FLUX 1_LORA_qwer.safetensors", "yewon-seo_qwer-form.safetensors"),
}


def repo_id(slug, title):
    t = "".join(c.lower() if c.isalnum() else "-" for c in title)
    t = "-".join(p for p in t.split("-") if p)
    return f"{USER}/arch507-{slug}-{t}"[:96].rstrip("-")


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def card(meta, slug, files, examples):
    triggers = [p[3] for p in meta["lora"] if len(p) > 3 and p[3] and p[3] != "—"]
    prompt = meta.get("prompt", "").split(" — ")[0].strip()
    y = ["---", "license: other", "license_name: flux-1-dev-non-commercial-license",
         "license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md",
         "base_model: black-forest-labs/FLUX.1-dev", "library_name: diffusers", "pipeline_tag: text-to-image",
         "tags:", "  - lora", "  - flux", "  - text-to-image", "  - architecture", "  - arch507"]
    if triggers:
        y.append(f"instance_prompt: {yaml_str(triggers[0])}")
    if examples:
        y.append("widget:")
        for i, e in enumerate(examples):
            y.append(f"  - text: {yaml_str(prompt if i == 0 and prompt else meta['title'])}")
            y.append("    output:")
            y.append(f"      url: images/{e}")
    y.append("---")
    rows = ["| File | Trained on | Trigger | Strength used |", "|---|---|---|---|"]
    for p in meta["lora"]:
        p = p + [""] * (5 - len(p))
        rows.append(f"| `{files[p[0]]}` | {p[2]} | {('`' + p[3] + '`') if p[3] and p[3] != '—' else '—'} | {p[4] or '—'} |")
    gallery = "\n".join(f"![]({'images/' + e})" for e in examples)
    note = f"\n> {meta['note']}\n" if meta.get("note") else ""
    return "\n".join(y) + f"""

# {meta['title']}

**{meta['name']}** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*{meta.get('tagline', '')}*

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.
{note}
{meta['body'].strip()}

## LoRA files

{chr(10).join(rows)}

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("{repo_id(slug, meta['title'])}", weight_name="{files[meta['lora'][0][0]]}")`

Example prompt from the student's tests:

> {meta.get('prompt', '')}

## Images

{gallery}

## Credit and license

LoRA by {meta['name']}, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
"""


def main():
    dry = "--dry-run" in sys.argv
    make_public = "--public" in sys.argv
    downloads, repos = {}, []
    if not dry:
        from huggingface_hub import HfApi, CommitOperationAdd
        api = HfApi()
    out_dir = ROOT / "data" / "hf_cards"
    out_dir.mkdir(parents=True, exist_ok=True)
    for p in sorted((CONTENT / "students").glob("*.md")):
        meta, body = parse(p)
        meta["body"] = body
        slug = p.stem
        if not meta["lora"]:
            continue
        rid = repo_id(slug, meta["title"])
        repos.append(rid)
        files = {pp[0]: FILES[pp[0]][1] for pp in meta["lora"]}
        finals = [f["file"] for f in ASSETS[slug]["finals"]]
        cover = str(meta.get("cover", "1")).zfill(2)
        picks = [cover] + [f for f in finals if f != cover][:3]
        examples = [f"{f}.jpg" for f in picks]
        text = card(meta, slug, files, examples)
        (out_dir / f"{slug}.md").write_text(text, "utf-8")
        for orig, new in files.items():
            downloads[orig] = f"https://huggingface.co/{rid}/resolve/main/{new}?download=true"
        if dry:
            print("would upload", rid, list(files.values()))
            continue
        if make_public:
            api.update_repo_settings(rid, private=False)
            print("public:", rid, flush=True)
            continue
        api.create_repo(rid, repo_type="model", private=True, exist_ok=True)
        ops = [CommitOperationAdd("README.md", io.BytesIO(text.encode("utf-8")))]
        ops += [CommitOperationAdd(f"images/{e}", str(ROOT / "assets" / slug / "final" / e.replace(".jpg", "_t.jpg"))) for e in examples]
        ops += [CommitOperationAdd(new, str(SRC / FILES[orig][0])) for orig, new in files.items()]
        api.create_commit(rid, operations=ops, commit_message="Add LoRA, model card and example images")
        print("uploaded:", rid, flush=True)
    (ROOT / "data" / "downloads.json").write_text(json.dumps(downloads, indent=1), "utf-8")
    if not dry and not make_public:
        coll = next((c for c in api.list_collections(owner=USER) if c.title == COLLECTION_TITLE), None)
        if coll is None:
            coll = api.create_collection(COLLECTION_TITLE, description="Student LoRAs from ARCH 507 (Winter 2026), Taubman College, University of Michigan.", private=True)
        have = {i.item_id for i in api.get_collection(coll.slug).items}
        for rid in repos:
            if rid not in have:
                api.add_collection_item(coll.slug, item_id=rid, item_type="model")
        print("collection:", coll.slug)
    print("repos:", len(repos))


if __name__ == "__main__":
    main()
