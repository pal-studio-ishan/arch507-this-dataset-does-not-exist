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
instance_prompt: "in the style of hoos"
widget:
  - text: "cinematic architecture magazine photograph of a library carved into a desert cliff outside Marrakech, designed in the spirit of Luis Barragán and Tadao Ando… In the style of disasterpiece"
    output:
      url: images/12.jpg
  - text: "le_zine"
    output:
      url: images/01.jpg
  - text: "le_zine"
    output:
      url: images/02.jpg
  - text: "le_zine"
    output:
      url: images/03.jpg
---

# le_zine

**Emily Naumann** · ARCH 507 *Generative AI: Thinking and Designing with Machine Intelligence* · Taubman College, University of Michigan · Winter 2026 · Instructor: Ishan Pal Singh

*Three LoRAs trained on film, old magazines and photography, to pull AI images back toward real design.*

**Project page:** [https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/emily-naumann/](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/students/emily-naumann/) · all projects: [course site](https://pal-studio-ishan.github.io/arch507-this-dataset-does-not-exist/)

This LoRA comes from the assignment **This Dataset Does Not Exist**. Each student built and captioned their own dataset to insert a new bias into FLUX.1 [dev]: something the base model couldn't make with enough force or specificity.

## The question
Popular models make sleek, futuristic images that read as AI right away and often carry little design value. Emily wanted the retro feel of a late-20th-century architecture magazine. A quick test showed the gap: adding "in the style of an 1980s architecture magazine" to a prompt barely changed the image, but a LoRA changed it immediately.

## What they did
- Trained three LoRAs on "archaic" media: stills from *Phantom Thread* (**hoos**), 1970s–90s magazine photography (**disasterpiece**), and the photographers Josef Sudek and Saul Leiter (**minm**).
- Ran the same prompt, a Japanese-inspired bedroom, through each LoRA. Emily repeated it with a thesis collage of their own as a reference image, then in pairs, then with longer and longer prompts.

## What they found
- The magazine LoRA came closest to what Emily wanted, but its bias was strong. It overrode prompts and echoed famous projects in the dataset (Maison de Verre), which made truly new designs hard.
- The Sudek/Leiter LoRA was the most flexible. It added a distinctive blur and grain without changing the space, so it worked with any prompt.
- The film LoRA caught the movie's mood at high strength (~2) but didn't carry over easily into architecture.
- The LoRAs didn't combine the way Emily hoped (one's palette with another's composition). Even so, all three were more useful to Emily than the base model.

## LoRA files

| File | Trained on | Trigger | Strength used |
|---|---|---|---|
| `emily-naumann_hoos.safetensors` | Stills from the film *Phantom Thread* | `in the style of hoos` | 1.25–2 |
| `emily-naumann_disasterpiece.safetensors` | 1970s–90s architecture magazine photography | `in the style of disasterpiece` | 1.25–2 |
| `emily-naumann_minm.safetensors` | Photographs by Josef Sudek and Saul Leiter | `in the style of minm` | 1.25 |

## How to use

- Base model: **FLUX.1 [dev]**. These LoRAs don't work with SDXL.
- ComfyUI: put the file in `models/loras` and load it with *LoraLoaderModelOnly* after the Flux model. Start at the strength listed above.
- diffusers: `pipe.load_lora_weights("pal-studio/arch507-emily-naumann-le-zine", weight_name="emily-naumann_hoos.safetensors")`

Example prompt from the student's tests:

> cinematic architecture magazine photograph of a library carved into a desert cliff outside Marrakech, designed in the spirit of Luis Barragán and Tadao Ando… In the style of disasterpiece

## Images

![](images/12.jpg)
![](images/01.jpg)
![](images/02.jpg)
![](images/03.jpg)

## Credit and license

LoRA by Emily Naumann, made for ARCH 507 at Taubman College, University of Michigan. It was trained on FLUX.1 [dev], so it falls under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md). Please credit the student when you share results. The training images aren't redistributed here.
