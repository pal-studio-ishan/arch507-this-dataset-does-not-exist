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
instance_prompt: "architamer"
widget:
  - text: "architamer, a narrow pedestrian \"stair-street\" in As-Salt, steep limestone steps carved into the hillside, towering yellow stone walls on either side, iron railings, overhead wires crossing the blue sky, cinematic architectural perspective"
    output:
      url: images/04.jpg
  - text: "Lithic Hospitality"
    output:
      url: images/01.jpg
  - text: "Lithic Hospitality"
    output:
      url: images/02.jpg
  - text: "Lithic Hospitality"
    output:
      url: images/03.jpg
---

# Lithic Hospitality

**Tamer Tubishat** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Against the average: teaching the model the yellow stone, stairs and open doors of As-Salt, Jordan.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/tamer-tubishat/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/tamer-tubishat/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Generative models get their power from breadth, and that breadth comes from averaging, which flattens specific places. Asked for "a house in As-Salt, Jordan", base Flux produced generic Mediterranean or "Arab" buildings. Tamer argued that As-Salt's identity matters enough to be learned.

## What they did
- Built a dataset to "recover and exaggerate" what was missing: the golden-yellow local limestone, buildings cascading down steep slopes, public stair-streets, and the *madafa*, a hospitality hall tied to an "architecture of the open door".
- Trained a LoRA with the trigger word `architamer` and compared the results with the base model, before and after.
- Sequenced twelve images in four phases: visual language, scale and condition, atmosphere and hospitality, and speculative futures.

## What they found
- The trigger word held material and form steady across scales, from a single window to the whole city, and through sunsets, rain and night.
- It made a "future-primitive" Salti modernism imaginable, though some contradictory ideas such as a futuristic vertical garden didn't work.
- The designer's job is to stop accepting a model's defaults and start shaping them to protect cultural and site-specific identity.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `tamer-tubishat_architamer.safetensors` | As-Salt, Jordan: yellow limestone, hillside urbanism, stair-streets, hospitality halls | `architamer` | 1.0 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-tamer-tubishat-lithic-hospitality", weight_name="tamer-tubishat_architamer.safetensors")`

Example prompt from the student's tests:

> architamer, a narrow pedestrian "stair-street" in As-Salt, steep limestone steps carved into the hillside, towering yellow stone walls on either side, iron railings, overhead wires crossing the blue sky, cinematic architectural perspective

## Images

![](images/04.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Tamer Tubishat, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
