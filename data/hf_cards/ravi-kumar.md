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
instance_prompt: "stoneybaloney"
widget:
  - text: "Material LoRA + facade LoRA + text prompt; later a LoRA-generated ControlNet + material LoRA"
    output:
      url: images/11.jpg
  - text: "Amabuye"
    output:
      url: images/01.jpg
  - text: "Amabuye"
    output:
      url: images/02.jpg
  - text: "Amabuye"
    output:
      url: images/03.jpg
---

# Amabuye

**Ravi Kumar** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Rwanda's volcanic stone, a material the base model reduces to a hut, carried into contemporary form.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/ravi-kumar/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/ravi-kumar/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

> The volcanic stone dataset wasn't handed in; the stone LoRA itself is included.

## The question
Like historical archives, image models flatten non-Western histories. Asked about Rwandan architecture, they jump to generic East African huts. During a research fellowship in Kigali, Ravi saw how central basalt volcanic stone (*amabuye* in Kinyarwanda) is to Rwanda's buildings, from foundations to field boundaries. Ravi asked whether a LoRA could teach the model this material and then carry it into contemporary architecture.

## What they did
- Trained a material LoRA on the stone: its pores and its precise polygonal joints.
- Trained two facade LoRAs, one on line-art elevations and one on photographs of contemporary facades.
- Combined them in steps: material plus facade LoRA, then the material LoRA alone in context. Finally Ravi used the line-art LoRA to generate a composition, fed it in as a ControlNet, and applied the stone on top.

## What they found
- Scale was the hardest part. The model kept blowing individual stones up into facade-sized panels.
- It insisted on applying the stone the way buildings are usually made today, as hung cladding rather than solid, self-supporting masonry.
- Ravi was never fully satisfied with the images, but the process exposed how hard it is to shift a model's bias when the data it has is thin or marginalised.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `ravi-kumar_stoneybaloney.safetensors` | Rwandan volcanic stone (amabuye) details: porosity, polygonal joinery | `stoneybaloney` | — |
| `ravi-kumar_katropalop.safetensors` | Line-art elevations, white lines on black | `lineart architectural elevation` | — |
| `ravi-kumar_wikiwikiwoo.safetensors` | Straight-on photographs of contemporary facades | — | — |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-ravi-kumar-amabuye", weight_name="ravi-kumar_stoneybaloney.safetensors")`

Example prompt from the student's tests:

> Material LoRA + facade LoRA + text prompt; later a LoRA-generated ControlNet + material LoRA

## Images

![](images/11.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Ravi Kumar, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
