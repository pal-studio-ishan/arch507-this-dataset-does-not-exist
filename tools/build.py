"""Build the static site from content/ and data/assets.json.

  content/course.md              course intro (front matter + markdown)
  content/students/<slug>.md     one file per student (front matter + markdown)
  data/assets.json               written by tools/prepare_assets.py
  data/downloads.json            optional: {"<lora file name>": "<download url>"}

Writes index.html and students/<slug>/index.html. Run:  python -I tools/build.py
"""
import html, json, re
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
ASSETS = json.loads((ROOT / "data" / "assets.json").read_text("utf-8"))
DL_PATH = ROOT / "data" / "downloads.json"
DOWNLOADS = json.loads(DL_PATH.read_text("utf-8")) if DL_PATH.exists() else {}
MD = markdown.Markdown(extensions=["sane_lists"])
E = html.escape


def md(text):
    MD.reset()
    return MD.convert(text)


def md_inline(text):
    out = md(text).strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", out, flags=re.S)


def parse(path):
    raw = path.read_text("utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta, body = {"lora": [], "dataset": []}, raw
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            k, v = k.strip(), v.strip()
            if k in ("lora", "dataset"):
                meta[k].append([p.strip() for p in v.split("|")])
            else:
                meta[k] = v
    return meta, body


def head(title, desc, prefix):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}site.css">
</head>
<body>
"""


def foot(course, prefix):
    return f"""<footer class="foot wrap">
  <div>{E(course['course'])}<br>{E(course['school'])} · {E(course['term'])}</div>
  <div>Instructor: {E(course['instructor'])}</div>
  <div class="foot-note">Student work shared for education and research. LoRAs are free for non-commercial use with credit to the student. Datasets built from other people's images are shown as captions and small thumbnails only.</div>
</footer>
<script src="{prefix}site.js"></script>
</body>
</html>
"""


def load_students():
    out = []
    for p in sorted((CONTENT / "students").glob("*.md")):
        meta, body = parse(p)
        meta["slug"], meta["body"] = p.stem, body
        meta["assets"] = dict(ASSETS.get(p.stem, {"finals": [], "datasets": {}}))
        hidden = {h.strip().zfill(2) for h in meta.get("hide", "").split(",") if h.strip()}
        if hidden:  # "hide: 19" leaves those images off the page (numbers as in assets/<slug>/final/)
            meta["assets"]["finals"] = [f for f in meta["assets"]["finals"] if f["file"] not in hidden]
        out.append(meta)
    return out


def cover_of(s):
    """'cover: 4' picks assets/<slug>/final/04.jpg."""
    finals = s["assets"]["finals"]
    want = str(s.get("cover", 1)).zfill(2)
    return want if any(f["file"] == want for f in finals) else (finals[0]["file"] if finals else None)


def method_block():
    """Collapsible Methodology from content/methodology.md, shown under the course intro."""
    path = CONTENT / "methodology.md"
    if not path.exists():
        return ""
    return (f'<details class="method" id="methodology"><summary class="mono">Methodology</summary>'
            f'<div class="method-body">{md(path.read_text("utf-8"))}</div></details>')


def compare_section():
    """'One prompt, every LoRA' grid(s) from data/compare.json (written by tools/prepare_compare.py)."""
    path = ROOT / "data" / "compare.json"
    if not path.exists():
        return ""
    c = json.loads(path.read_text("utf-8"))
    sets = c["sets"]
    tabs = ""
    if len(sets) > 1:
        tabs = '<div class="cmp-tabs" role="tablist">' + "".join(
            f'<button class="cmp-tab" type="button" role="tab" data-set="{st["key"]}" aria-selected="{"true" if i == 0 else "false"}">{E(st["title"])}</button>'
            for i, st in enumerate(sets)) + "</div>"
    blocks = []
    for i, st in enumerate(sets):
        k = st["key"]
        tiles = []
        for it in st["items"]:
            if it["slug"]:
                who = f'<a href="students/{it["slug"]}/">{E(it["name"])}</a>'
                what = f'{E(it["lora"])} · {it["strength"]:g}'
            else:
                who, what = '<span class="cmp-base">Base model</span>', "FLUX.1 [dev], no LoRA"
            alt = f'{it["name"]}, {it["lora"]}'
            tiles.append(f'<figure class="cmp-item"><a class="g-item" href="assets/compare/{k}/{it["file"]}.jpg">'
                         f'<img src="assets/compare/{k}/{it["file"]}_t.jpg" alt="{E(alt)}" loading="lazy" width="672" height="384"></a>'
                         f'<figcaption>{who}<span class="mono small muted">{what}</span></figcaption></figure>')
        blocks.append(f'<div class="cmp-set lb-group" data-set="{k}"{" hidden" if i else ""}>'
                      f'<p class="mono small muted cmp-settings">{E(st["settings"])} · <a href="assets/compare/{k}/sheet.jpg">contact sheet (JPG)</a></p>'
                      f'<div class="cmp-grid">{"".join(tiles)}</div></div>')
    rec = " Two versions: every LoRA at 1.0, and each at the strength its student recommended (the middle of their range)." if len(sets) > 1 else ""
    return f"""<section class="wrap compare" id="compare">
  <h2 class="section-label mono">One prompt, every LoRA</h2>
  <div class="prose"><p>One prompt, run through plain FLUX.1 [dev] and then through each of the {len(sets[0]["items"]) - 1} LoRAs, with the same seed and settings and each LoRA's trigger word added. It shows what each dataset pushes into the model on its own.{rec}</p></div>
  <div class="prompt"><p class="mono small">{E(c["prompt"])}</p><button class="copy mono small" type="button">Copy</button></div>
  {tabs}{"".join(blocks)}
</section>"""


def build_index(course, course_body, students):
    n_lora = sum(len(s["lora"]) for s in students)
    cards = []
    for s in students:
        c = cover_of(s)
        k = len(s["lora"])
        chip = f'{k} LoRA{"s" if k != 1 else ""}' if k else "Images + write-up"
        cards.append(f"""<a class="card" href="students/{s['slug']}/">
  <div class="card-img"><img src="assets/{s['slug']}/final/{c}_t.jpg" alt="" loading="lazy"></div>
  <div class="card-meta"><span class="mono small muted">{E(s['name'])}</span><span class="chip">{chip}</span></div>
  <h3>{E(s['title'])}</h3>
  <p class="muted">{E(s.get('tagline', ''))}</p>
</a>""")
    return head(course["title"] + " — ARCH 507", course_body.strip().split("\n")[0], "") + f"""
<header class="top wrap"><span class="mono small">ARCH 507 · {E(course['term'])}</span><span class="mono small muted">Taubman College · University of Michigan</span></header>
<section class="hero wrap">
  <p class="mono small muted">Assignment 05</p>
  <h1 class="mono">{E(course['title'])}</h1>
  <p class="lede">{E(course['course'])}</p>
</section>
<section class="intro wrap">
  <div class="prose">{md(course_body)}{method_block()}</div>
  <dl class="stats">
    <div><dt>Projects</dt><dd>{len(students)}</dd></div>
    <div><dt>LoRAs</dt><dd>{n_lora}</dd></div>
    <div><dt>Base model</dt><dd>FLUX.1 [dev]</dd></div>
  </dl>
</section>
<section class="wrap">
  <h2 class="section-label mono">Projects</h2>
  <div class="grid">{''.join(cards)}</div>
</section>
{compare_section()}
<section class="wrap about">
  <h2 class="section-label mono">About the course</h2>
  <div class="about-cols">{md((CONTENT / "about.md").read_text("utf-8"))}</div>
</section>
<section class="wrap howto">
  <h2 class="section-label mono">Using the LoRAs</h2>
  <div class="howto-cols">
    <div><h3>Base model</h3><p>Every LoRA here was trained on <strong>FLUX.1 [dev]</strong> (rank 16, on fal.ai). None of them work with SDXL, even where a student's slides say SDXL.</p></div>
    <div><h3>In ComfyUI</h3><p>Put the file in <code>models/loras</code> and load it with <em>LoraLoaderModelOnly</em> after the Flux model. Start at the strength the student used, listed on each project page.</p></div>
    <div><h3>Prompting</h3><p>Use the trigger word if there is one. Each page has an example prompt from the student's own tests.</p></div>
  </div>
</section>
""" + foot(course, "")


def lora_block(s):
    if not s["lora"]:
        return ""
    rows = []
    for parts in s["lora"]:
        parts += [""] * (5 - len(parts))
        file, name, trained, trigger, strength = parts[:5]
        url = DOWNLOADS.get(file)
        btn = (f'<a class="btn" href="{E(url)}">Download</a>' if url else '<span class="btn btn-off">Download soon</span>')
        page = url.split("/resolve/")[0] if url else ""
        file = url.split("/resolve/main/")[1].split("?")[0] if url else file  # show the name it has on Hugging Face
        rows.append(f"""<div class="lora">
  <div class="lora-head"><h3 class="mono">{E(name)}</h3>{btn}</div>
  <dl>
    <div><dt>Trained on</dt><dd>{md_inline(trained)}</dd></div>
    <div><dt>Trigger</dt><dd>{('<code>' + E(trigger) + '</code>') if trigger and trigger != '—' else '<span class="muted">none</span>'}</dd></div>
    <div><dt>Strength used</dt><dd>{E(strength) if strength and strength != '—' else '<span class="muted">not stated</span>'}</dd></div>
    <div><dt>File</dt><dd class="mono small break">{E(file)}</dd></div>
  </dl>
  {f'<a class="hf-link small" href="{E(page)}">Model page on Hugging Face →</a>' if page else ''}
</div>""")
    return f'<section class="block"><h2 class="section-label mono">LoRAs</h2><div class="loras">{"".join(rows)}</div></section>'


def dataset_block(s):
    if not s["dataset"]:
        return ""
    out = []
    for parts in s["dataset"]:
        parts += [""] * (3 - len(parts))
        key, desc, captioning = parts[:3]
        d = s["assets"]["datasets"].get(key, {})
        thumbs = ""
        if d.get("show_thumbs") and d.get("thumbs"):
            thumbs = '<div class="thumbs">' + "".join(
                f'<img src="../../assets/{s["slug"]}/{key}/{t}.jpg" alt="" loading="lazy">' for t in d["thumbs"]) + "</div>"
        caps = [c for c in d.get("captions", []) if c][:2]
        cap_html = "".join(f"<blockquote>{E(c[:420])}{'…' if len(c) > 420 else ''}</blockquote>" for c in caps)
        cap_link = (f'<a class="small" href="../../assets/{s["slug"]}/{key}-captions.txt">All {d.get("count", "")} captions (.txt)</a>'
                    if any(d.get("captions", [])) else "")
        out.append(f"""<div class="dataset">
  <p>{md_inline(desc)}</p>
  <p class="muted small">{md_inline(captioning)}</p>
  {thumbs}
  {cap_html}
  {cap_link}
</div>""")
    return f'<section class="block"><h2 class="section-label mono">Dataset</h2>{"".join(out)}</section>'


def build_student(course, s, prev_s, next_s):
    slug = s["slug"]
    finals = s["assets"]["finals"]
    c = cover_of(s)
    gallery = "".join(
        f'<a class="g-item" href="../../assets/{slug}/final/{f["file"]}.jpg" data-w="{f["w"]}" data-h="{f["h"]}">'
        f'<img src="../../assets/{slug}/final/{f["file"]}_t.jpg" alt="{E(s["title"])}, image {i}" loading="lazy" width="{f["w"]}" height="{f["h"]}"></a>'
        for i, f in enumerate(finals, 1))
    note = f'<p class="note">{md_inline(s["note"])}</p>' if s.get("note") else ""
    prompt = (f'<section class="block"><h2 class="section-label mono">Try it</h2><div class="prompt"><p class="mono small">{E(s["prompt"])}</p>'
              f'<button class="copy mono small" type="button">Copy</button></div></section>') if s.get("prompt") else ""
    triggers = [p[3] for p in s["lora"] if len(p) > 3 and p[3] and p[3] != "—"]
    glance = f"""<dl class="glance">
  <div><dt>LoRAs</dt><dd>{len(s['lora']) or 'Not handed in'}</dd></div>
  <div><dt>Base model</dt><dd>FLUX.1 [dev]</dd></div>
  <div><dt>Trigger words</dt><dd>{', '.join('<code>' + E(t) + '</code>' for t in triggers) or '<span class="muted">none</span>'}</dd></div>
  <div><dt>Final images</dt><dd>{len(finals)}</dd></div>
</dl>"""
    return head(f"{s['title']} — {s['name']}", s.get("tagline", ""), "../../") + f"""
<header class="top wrap">
  <a class="mono small" href="../../">← All projects</a>
  <nav class="mono small pager"><a href="../{prev_s['slug']}/">← {E(prev_s['name'])}</a><a href="../{next_s['slug']}/">{E(next_s['name'])} →</a></nav>
</header>
<section class="p-hero wrap">
  <p class="mono small muted">{E(s['name'])}</p>
  <h1>{E(s['title'])}</h1>
  <p class="lede">{E(s.get('tagline', ''))}</p>
</section>
<div class="p-cover wrap"><img src="../../assets/{slug}/final/{c}.jpg" alt=""></div>
<section class="p-body wrap">
  <article class="prose">{note}{md(s['body'])}</article>
  <aside>{glance}</aside>
</section>
<section class="block wrap"><h2 class="section-label mono">Final images</h2><div class="gallery">{gallery}</div></section>
<div class="wrap">{lora_block(s)}{dataset_block(s)}{prompt}</div>
<nav class="wrap pager-bottom mono small"><a href="../{prev_s['slug']}/">← {E(prev_s['title'])}</a><a href="../{next_s['slug']}/">{E(next_s['title'])} →</a></nav>
""" + foot(course, "../../")


def main():
    course, course_body = parse(CONTENT / "course.md")
    students = load_students()
    (ROOT / "index.html").write_text(build_index(course, course_body, students), "utf-8")
    for i, s in enumerate(students):
        d = ROOT / "students" / s["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(build_student(course, s, students[i - 1], students[(i + 1) % len(students)]), "utf-8")
    print(f"built index + {len(students)} student pages")


if __name__ == "__main__":
    main()
