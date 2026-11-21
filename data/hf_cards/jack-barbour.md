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
  - text: "free standing building with parametric brick facade that girates, undulates, and makes complex geometric movements that seem to defy gravity. located in a grassy field, blue sky in the background, large windows in the building, cantilevers"
    output:
      url: images/04.jpg
  - text: "Future Facades"
    output:
      url: images/01.jpg
  - text: "Future Facades"
    output:
      url: images/02.jpg
  - text: "Future Facades"
    output:
      url: images/03.jpg
---

# Future Facades

**Jack Barbour** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Two LoRAs to get parametric brick facades with bricks at the right scale.*

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Ask a mainstream model for "a parametric brick facade" and you get bricks that are stretched and too thin, on forms that could never be built. Jack wanted facades with real brick scale and some constructive logic.

## What they did
- Trained a first LoRA on close-ups of parametric brick facades, chosen to show correct brick size and coursing.
- That alone gave abstract brick patterns, not buildings. So Jack trained a second LoRA on freestanding brick buildings shown with the ground and sky.
- Ran both LoRAs together at 1.2 and refined the prompt step by step, from "brick facade on a building" to a full description of the site, the windows and the cantilevers.

## What they found
- More steps didn't help much. Prompt work and the second LoRA did.
- The final images show coherent buildings with expressive brick facades and a believable sense of brick scale, which general-purpose models lack.
- Getting there took careful dataset curation and many prompt iterations. Purpose-built architectural datasets could make AI images far more reliable.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `jack-barbour_brick-buildings.safetensors` | Freestanding brick buildings with ground and sky | — | 1.2 |
| `jack-barbour_brick-facade-closeups.safetensors` | Close-ups of parametric brick facades | — | 1.2 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-jack-barbour-future-facades", weight_name="jack-barbour_brick-buildings.safetensors")`

Example prompt from the student's tests:

> free standing building with parametric brick facade that girates, undulates, and makes complex geometric movements that seem to defy gravity. located in a grassy field, blue sky in the background, large windows in the building, cantilevers — both LoRAs at 1.2, 35 steps

## Images

![](images/04.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Jack Barbour, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
