---
name: Ravi Kumar
title: Amabuye
tagline: Rwanda's volcanic stone, a material the base model reduces to a hut, carried into contemporary form.
cover: 11
lora: stoneybaloney.safetensors | stoneybaloney | Rwandan volcanic stone (amabuye) details: porosity, polygonal joinery | stoneybaloney | —
lora: katropalop.safetensors | katropalop | Line-art elevations, white lines on black | lineart architectural elevation | —
lora: wikiwikiwoo.safetensors | wikiwikiwoo | Straight-on photographs of contemporary facades | — | —
dataset: lineart-elevations | 38 line-art elevations in the style of a ControlNet line drawing | Detailed captions describing floors, openings and relief
dataset: elevation-photos | 41 straight-on photographs of contemporary facades | Detailed captions describing structure and cladding
prompt: Material LoRA + facade LoRA + text prompt; later a LoRA-generated ControlNet + material LoRA
note: The volcanic stone dataset wasn't handed in; the stone LoRA itself is included.
---
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
