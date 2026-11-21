---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
base_model: black-forest-labs/FLUX.1-dev
library_name: diffusers
pipeline_tag: text-to-image
tags:
  - lora
  - flux
  - text-to-image
  - architecture
  - arch507
widget:
  - text: "Cinematic architecture magazine photograph of a bamboo sleeping pavilion interior in a Vietnamese vernacular using traditional multi-culm bundle columns with dark coir lashing… Film photograph shot on Ilford HP5 black and white film"
    output:
      url: images/04.jpg
  - text: "Bambu"
    output:
      url: images/01.jpg
  - text: "Bambu"
    output:
      url: images/02.jpg
  - text: "Bambu"
    output:
      url: images/03.jpg
---

# Bambu

**Arushi Chopra** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*A LoRA for traditional bamboo joinery: lashing, dowels and culm bundles across vernaculars.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/arushi-chopra/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/arushi-chopra/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

> No written analysis was handed in. This summary comes from the review slides.

## The question
Base models can draw "a bamboo building" but not how bamboo actually goes together: the lashing at a node, a bundle of culms acting as a column, split-culm roof tiles. Arushi collected niche images of real joinery to see if a LoRA could carry those details into new buildings.

## What they did
- Built a dataset of bamboo joinery photographs from practices known for bamboo, with captions describing each joint in detail.
- Trained two LoRAs and compared each prompt with and without them.
- Made a series called *Culm*, moving through regional traditions: Latin American, Vietnamese, Javanese, Filipino, Indian and Japanese. Many prompts asked for black-and-white film photography (Ilford, Tri-X, Neopan).
- In the last images Arushi used both LoRAs together (2.0 and 1.0) with very short prompts, to see how much the LoRAs carried on their own.

## What the tests looked at
- Whether natural patterns such as woven screens and shadows come through.
- Whether lashing and structural logic hold up in new building types: bridges, market halls, porches, tea houses.
- How far the bamboo details survive when the prompt gives almost no detail.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `arushi-chopra_borsch_t.safetensors` | Bamboo architecture (one of two LoRAs) | — | 1.25–2.0 |
| `arushi-chopra_too_late.safetensors` | Bamboo architecture (one of two LoRAs) | — | 1.0–1.75 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-arushi-chopra-bambu", weight_name="arushi-chopra_borsch_t.safetensors")`

Example prompt from the student's tests:

> Cinematic architecture magazine photograph of a bamboo sleeping pavilion interior in a Vietnamese vernacular using traditional multi-culm bundle columns with dark coir lashing… Film photograph shot on Ilford HP5 black and white film — LoRA 1.25, guidance 4.0

## Images

![](images/04.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Arushi Chopra, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
