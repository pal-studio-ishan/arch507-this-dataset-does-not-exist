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
instance_prompt: "C_at_el"
widget:
  - text: "Delicate clusters of tiny, white flowers and blades of grass grow from the edges of a calm, sleeping lake"
    output:
      url: images/03.jpg
  - text: "Memory"
    output:
      url: images/01.jpg
  - text: "Memory"
    output:
      url: images/02.jpg
  - text: "Memory"
    output:
      url: images/04.jpg
---

# Memory

**Angelica Facey** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Teaching a razor-sharp model the grain, blur and quiet of old photographs.*

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Models like Flux chase perfect, high-resolution realism. What gets lost is imperfection: grain, softness, the feel of time passing. Angelica asked whether a model could carry the "colours of time" from old photographs, and build a world that feels both made-up and familiar, like a memory.

## What they did
- Built two datasets of black-and-white landscape photographs: forest paths and canopy light for one LoRA, mountain panoramas for the other.
- Wrote the captions as atmosphere rather than lists of objects, using words like *tranquillity*, *seclusion* and *enclosure*. Angelica "co-wrote" them with Gemini, mixing a personal description with what the model said it saw.
- Trained two FLUX LoRAs on fal.ai, then combined them in ComfyUI. One LoRA led at full strength and the other supported at 0.75, which made it possible to collage each composition.

## What they found
- Captions written as mood and story pushed the model toward a feeling, not just a subject.
- Two LoRAs on the same idea but with different subjects worked like two paintbrushes for one world.
- The grain and low-fi texture survived into new scenes the datasets never showed.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `angelica-facey_C_at_el.safetensors` | Forest paths and canopy light | `C_at_el` | 1.0 (main) |
| `angelica-facey_YO_c_me_T.safetensors` | Mountain and valley panoramas | `YO_c_me_T` | 0.75 (second) |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal13/arch507-angelica-facey-memory", weight_name="angelica-facey_C_at_el.safetensors")`

Example prompt from the student's tests:

> Delicate clusters of tiny, white flowers and blades of grass grow from the edges of a calm, sleeping lake — C_at_el 1.0 + YO_c_me_T 0.75, Flux guidance 5

## Images

![](images/03.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/04.jpg)

## Credit and license

LoRA by Angelica Facey, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
