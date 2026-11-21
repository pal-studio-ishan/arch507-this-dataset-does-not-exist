# This Dataset Does Not Exist

Student LoRA projects from **ARCH 507 — Generative AI: Thinking and Designing with Machine Intelligence**, Winter 2026, Taubman College, University of Michigan. Instructor: Ishan Pal Singh.

Each student found something FLUX.1 [dev] couldn't make, built and captioned a small dataset for it, trained a LoRA, and made a series of images. The site has one page per project: what they tested, what they built, what they found, their final images, their LoRAs and their dataset.

**Site:** https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/ · **LoRAs:** [Hugging Face collection](https://huggingface.co/collections/pal-studio/arch-507-this-dataset-does-not-exist-6b01774374191f228f0122bd)

## How the repo is organised

```
content/course.md              intro text on the home page
content/students/<name>.md     one file per student: summary, LoRAs, datasets, example prompt
assets/<name>/final/           final images (web-sized copies)
assets/<name>/<dataset>/       small dataset thumbnails, plus <dataset>-captions.txt
data/assets.json               list of images, written by tools/prepare_assets.py
data/downloads.json            LoRA download links (Hugging Face), once uploaded
tools/prepare_assets.py        copies and resizes images from the course Dropbox
tools/build.py                 turns content/ into index.html and students/<name>/index.html
index.html, students/          the built site, served by GitHub Pages
site.css, site.js              styles, image viewer, copy-prompt button
```

To change a summary, edit the student's file in `content/students/` and rebuild. The top of each file holds the structured parts:

- `lora:` file | name | trained on | trigger word | strength used
- `dataset:` key | description | how it was captioned
- `cover:` which final image is the cover, `hide:` images to leave out
- `prompt:` an example prompt, `note:` a short notice shown above the summary

## LoRAs

All LoRAs are FLUX.1 [dev], rank 16, trained on fal.ai. They're too large for GitHub, so they're hosted separately and linked from each project page.

## Datasets

Full dataset images appear only where they're the student's own work, public domain or openly licensed. Datasets built from other people's images are shown as captions, sources and small thumbnails.
