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
instance_prompt: "pencil_drawing"
widget:
  - text: "pencil_drawing of a desert city shaped entirely by shade, airflow, and human comfort"
    output:
      url: images/01.jpg
  - text: "pencil_drawing"
    output:
      url: images/02.jpg
  - text: "pencil_drawing"
    output:
      url: images/03.jpg
  - text: "pencil_drawing"
    output:
      url: images/04.jpg
---

# pencil_drawing

**Itamar Yahav** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*A failed render LoRA, then a pencil-drawing LoRA that imagines the sustainable buildings of tomorrow.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/itamar-yahav/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/itamar-yahav/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Itamar first wanted a LoRA that could turn any Rhino model into a render in the style of the visualisation studio Internoesterno. That style was too close to what Flux already does, and the images looked the same with or without the LoRA. So Itamar switched to a style Flux can't produce: fine architectural pencil drawings. The new LoRA became a way to ask a new question, prompted by a lecture by Cas Esbach and a history class on halting new construction: what does AI think truly sustainable architecture looks like?

## What they did
- Collected 25 pencil drawings, mostly isometrics of rural and corroded buildings. A Python script resized and renamed them, and Claude wrote the captions.
- Trained the LoRA with the trigger word `pencil_drawing`, then tested it on barns, schools and column details at different strengths.
- Generated twelve "sustainable futures": a net-zero home, a shopping centre, a vertical city, a floating community, an underground complex, a desert city, Archigram-style housing, a transport hub. Itamar ran each through an upscale pass.

## What they found
- The first LoRA was too generic to matter, a useful lesson in picking a style the model doesn't already know.
- The pencil LoRA produced ideas Itamar didn't expect and couldn't have come up with alone.
- Itamar's takeaways: be patient, since this is a lot of trial and error, and use AI to make something new rather than repeat what already exists.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `itamar-yahav_pencil_drawing.safetensors` | Architectural pencil drawings, mostly isometrics of rural and worn structures | `pencil_drawing` | 1.0 (0.8–1.25) |
| `itamar-yahav_peptides_first-try.safetensors` | Architectural visualisation renders | `peptides style` | — |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal-studio/arch507-itamar-yahav-pencil-drawing", weight_name="itamar-yahav_pencil_drawing.safetensors")`

Example prompt from the student's tests:

> pencil_drawing of a desert city shaped entirely by shade, airflow, and human comfort

## Images

![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)
![](images/04.jpg)

## Credit and license

LoRA by Itamar Yahav, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
