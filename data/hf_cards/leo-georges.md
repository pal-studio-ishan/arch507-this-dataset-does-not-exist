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
  - text: "Facade detail on flat surface, glass curtain wall with parametric mullions derived from dune contour lines, strict grid with subtle horizontal deformation, clean separation of structure and facade, soft light"
    output:
      url: images/04.jpg
  - text: "Sand"
    output:
      url: images/01.jpg
  - text: "Sand"
    output:
      url: images/02.jpg
  - text: "Sand"
    output:
      url: images/03.jpg
---

# Sand

**Leo Georges** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Using dune geometry, not sand texture, to bend a facade's mullion grid.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/leo-georges/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/leo-georges/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Base models read landscape as surface: texture, colour, material. When you ask for a building that responds to its site, they bury it in the terrain or carve it out of the rock. Leo wanted to treat landscape as geometry, as a system that could organise a facade.

## What they did
- Started with mountains and cliffs, but the images were too noisy. The model latched onto rock texture and colour.
- Switched to sand dunes, whose uniform material isolates pure curvature and flow.
- Built two separate datasets of 25 images: **mullions** (grid, repetition, order) and **dunes** (deformation, continuity). Each image was cropped to remove context and captioned with a Florence-2 workflow and Claude, then edited by hand.
- Trained both LoRAs on fal.ai and combined them in ComfyUI, with the mullions as structure and the dunes as a modifier. The twelve images move through four phases: establish the language, apply it, transform it, and push it to speculation.

## What they found
- At first the model collapsed geometry into material. Buildings turned sandy or rose out of the ground, because the LoRA strength was too high (1.2), the data leaned toward sand, and the prompts implied blending.
- Lowering the strength to 0.75, adding more facade examples and writing prompts that kept building and context separate fixed it.
- In the final images the grid stays readable while dune contours deform it. Natural geometry drives the facade without being copied.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `leo-georges_mullions.safetensors` | Window mullion systems: grid, spacing, repetition | — | 0.75 |
| `leo-georges_dunes.safetensors` | Sand dunes: flow, curvature, continuity | — | 0.75 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-leo-georges-sand", weight_name="leo-georges_mullions.safetensors")`

Example prompt from the student's tests:

> Facade detail on flat surface, glass curtain wall with parametric mullions derived from dune contour lines, strict grid with subtle horizontal deformation, clean separation of structure and facade, soft light — both LoRAs at 0.75, guidance 4

## Images

![](images/04.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Leo Georges, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
