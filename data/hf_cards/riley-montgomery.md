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
instance_prompt: "mont2"
widget:
  - text: "A close-up of lowbush blueberry plants hybridized with plastic, translucent plastic leaves and plastic berries that refract light, growing in a natural setting… lkjh, mont3"
    output:
      url: images/05.jpg
  - text: "Upper Peninsula Understory Futures"
    output:
      url: images/01.jpg
  - text: "Upper Peninsula Understory Futures"
    output:
      url: images/02.jpg
  - text: "Upper Peninsula Understory Futures"
    output:
      url: images/03.jpg
---

# Upper Peninsula Understory Futures

**Riley Montgomery** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Speculating on future plant species in Michigan's Upper Peninsula as the climate shifts.*

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

> The training images weren't handed in with the LoRAs.

## The question
Image models know little about less common species, especially in remote places like the Keweenaw Peninsula. Riley wanted to train a model on Upper Peninsula plants and then speculate on how climate change might reshape them. Understory plants hybridise and migrate faster, and hardiness zones are expected to shift about 13 miles a decade.

## What they did
- **mont2:** 24 images of 12 species. Six were native, from Michigan State University's list, and six currently grow two hardiness zones warmer. Every caption followed the same botanical format: view, scientific and common name, native range, height, flowers, leaves, roots, pollinators, soil.
- **lkjh:** narrowed to a single plant, the lowbush blueberry, with captions from Midjourney's describe tool.
- **mont3:** a LoRA trained on plastic objects, combined with the blueberry LoRA to imagine plastic-hybrid future plants.

## What they found
- The blueberry LoRA followed the plant closely, but the images offered little more than photographs would.
- The landscapes came out generic and every bush looked the same, because the dataset leaned toward close-ups. Riley's reviewer pointed to scale.
- The plastic hybrids raised a question Riley hadn't set out to ask, about microplastics in plants and soil.
- In hindsight Riley would pick one goal: either faithful depiction of the blueberry (LoRAs by season and scale) or speculative hybrids built from a dataset of made-up hybrids.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `riley-montgomery_mont2.safetensors` | 12 Upper Peninsula plant species: 6 native, 6 expected to arrive | `mont2` | 0.3–1.5 |
| `riley-montgomery_lkjh.safetensors` | Lowbush blueberry | `lkjh` | 0.3–1.5 |
| `riley-montgomery_mont3.safetensors` | Plastic objects | `mont3` | 0.5–1.0 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-riley-montgomery-upper-peninsula-understory-futures", weight_name="riley-montgomery_mont2.safetensors")`

Example prompt from the student's tests:

> A close-up of lowbush blueberry plants hybridized with plastic, translucent plastic leaves and plastic berries that refract light, growing in a natural setting… lkjh, mont3 — strengths 0.5 + 1.0

## Images

![](images/05.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Riley Montgomery, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
