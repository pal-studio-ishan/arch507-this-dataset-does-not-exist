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
instance_prompt: "AA Dogma style"
widget:
  - text: "The exterior of the AA Dogma style building features a three-story continuous residential structure. The overall form is a highly saturated red volume… It has the style of architectural publications, with clear boundaries, blank sky, and a slight grain texture."
    output:
      url: images/02.jpg
  - text: "2.5D World"
    output:
      url: images/01.jpg
  - text: "2.5D World"
    output:
      url: images/03.jpg
  - text: "2.5D World"
    output:
      url: images/04.jpg
---

# 2.5D World

**Hua Lin (Dylan)** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Using a flat, collage-like drawing style to escape the smudged look of "realistic" AI images.*

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Dylan loves Dogma's collage style because it feels "real" and "unreal" at the same time, a three-dimensional world built from flat images (a 2.5D world). Earlier assignments showed that "realistic" AI images often look smudged and over-rendered, like a photo taken at too high an ISO. The hypothesis: a style built from lines, flat colour and simple shadows might avoid that.

## What they did
- First tried image-to-image: feeding Dylan's own studio line drawings in to get a Dogma-style collage. It didn't work.
- Switched to text-to-image with a LoRA trained on Dogma-style images, each with a long, specific caption.
- Planned the series as "8 + 4". Four buildings each got an exterior and an interior view, then four close-ups of everyday details: a bathroom sink, a steaming pot, socks by a bed, laundry by a window.

## What they found
- The hypothesis held. The images avoided the smudged texture and read clearly as a whole.
- Some details still broke real-world logic, but the overall effect went past Dylan's expectations.
- Very specific, everyday prompts worked too. The model seemed to really take on the style and build a consistent 2.5D world.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `hua-lin_justdoit.safetensors` | Dogma-style architectural collages | `AA Dogma style` | 1.0 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-hua-lin-2-5d-world", weight_name="hua-lin_justdoit.safetensors")`

Example prompt from the student's tests:

> The exterior of the AA Dogma style building features a three-story continuous residential structure. The overall form is a highly saturated red volume… It has the style of architectural publications, with clear boundaries, blank sky, and a slight grain texture.

## Images

![](images/02.jpg)
![](images/01.jpg)
![](images/03.jpg)
![](images/04.jpg)

## Credit and license

LoRA by Hua Lin (Dylan), made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
