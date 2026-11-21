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
instance_prompt: "Style of michaelset / Patelski Elevations"
widget:
  - text: "Graphic architectural elevation drawing in the style of Sander Patelski, an early modern bauhaus style glass and pastel building. Bright saturated colors… Style of michaelset"
    output:
      url: images/02.jpg
  - text: "AI as a Drawing Tool"
    output:
      url: images/01.jpg
  - text: "AI as a Drawing Tool"
    output:
      url: images/03.jpg
  - text: "AI as a Drawing Tool"
    output:
      url: images/04.jpg
---

# AI as a Drawing Tool

**Michael Natinsky** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Generating architectural elevations in the flat, colourful style of Sander Patelski.*

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Could AI be a real design tool for elevations, generating facade patterns and compositions worth bringing into your own work? Midjourney's attempts at elevations mostly failed, so Michael trained custom LoRAs.

## What they did
- Trained one LoRA on Sander Patelski's flat, colourful elevations and a second on plain architectural elevation drawings.
- Pushed the style across very different prompts: a Bauhaus pastel building, a Chicago skyscraper in the rain, a stone European village, and buildings in the spirit of Barragán, Herzog & de Meuron, Zumthor and Ando.

## What they found
- The Patelski style dominated. Even when Michael asked for brick, wood or stone, it fell back on flat pastel colours, and buildings floated in empty space unless the prompt forced context in.
- The landscape aspect ratio cut skyscrapers off. The model wouldn't show the full height.
- The drawing LoRA added window rhythms and some sketchy drafting lines.
- The model rearranges patterns rather than designing. It understands neither structure nor material. This tool may be best for presenting your own work, for example by running your elevations through it with ControlNet, which Michael planned but couldn't get running.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `michael-natinsky_patelski.safetensors` | Sander Patelski's graphic elevations | `Style of michaelset / Patelski Elevations` | 1.0 |
| `michael-natinsky_elevations.safetensors` | Plain architectural elevation drawings | — | 1.0 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-michael-natinsky-ai-as-a-drawing-tool", weight_name="michael-natinsky_patelski.safetensors")`

Example prompt from the student's tests:

> Graphic architectural elevation drawing in the style of Sander Patelski, an early modern bauhaus style glass and pastel building. Bright saturated colors… Style of michaelset

## Images

![](images/02.jpg)
![](images/01.jpg)
![](images/03.jpg)
![](images/04.jpg)

## Credit and license

LoRA by Michael Natinsky, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
