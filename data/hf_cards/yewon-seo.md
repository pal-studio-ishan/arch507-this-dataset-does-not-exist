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
instance_prompt: "asdf style"
widget:
  - text: "Photo of a plant pot with a growing light. S-shaped body holds the earth inside and has a lighting panel on the top. Ivy is planted inside, which is sealed with a translucent sheet… asdf style"
    output:
      url: images/02.jpg
  - text: "Render a Lamp"
    output:
      url: images/01.jpg
  - text: "Render a Lamp"
    output:
      url: images/03.jpg
  - text: "Render a Lamp"
    output:
      url: images/04.jpg
---

# Render a Lamp

**Yewon Seo** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Style + form = ? A SANAA-style LoRA and a LoRA of Yewon's own product design, mixed to render a planter lamp.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/yewon-seo/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/yewon-seo/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

> No written analysis was handed in. This summary comes from the review slides.

## The question
Can one LoRA carry a *style* and another a *form*, and can mixing them render a real design? Yewon tested it on a product of their own: a planter with a growing light, rendered in the soft, white light of SANAA's architecture.

## What they did
- Trained a **style** LoRA on photographs of SANAA buildings and a **form** LoRA on renders of Yewon's own Rhino model of the S-shaped planter lamp.
- Compared a text-only prompt with prompts that used the LoRAs, then mapped a grid of strengths: style from 1.2 to 2.0 with form fixed, and the reverse.
- Tested five ControlNets (DepthAnything, LineArt, Canny, HED, Binary) and settled on depth with style 1.6 and form 1.0.
- Made the final series by keeping everything fixed and changing only the noise seed.

## What the tests looked at
- How much of the lamp's real shape survives when the style LoRA is turned up.
- Which kind of ControlNet keeps the form while letting the style change the material and light.
- How much one fixed setup varies from seed to seed.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `yewon-seo_asdf-style.safetensors` | Photographs of SANAA buildings: white, light, minimal | `asdf style` | 1.6 |
| `yewon-seo_qwer-form.safetensors` | Renders of Yewon's own S-shaped planter-lamp model | — | 1.0 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-yewon-seo-render-a-lamp", weight_name="yewon-seo_asdf-style.safetensors")`

Example prompt from the student's tests:

> Photo of a plant pot with a growing light. S-shaped body holds the earth inside and has a lighting panel on the top. Ivy is planted inside, which is sealed with a translucent sheet… asdf style — style 1.6, form 1.0, DepthAnything ControlNet

## Images

![](images/02.jpg)
![](images/01.jpg)
![](images/03.jpg)
![](images/04.jpg)

## Credit and license

LoRA by Yewon Seo, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
