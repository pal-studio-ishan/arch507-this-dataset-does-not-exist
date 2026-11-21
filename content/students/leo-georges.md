---
name: Leo Georges
title: Sand
tagline: Using dune geometry, not sand texture, to bend a facade's mullion grid.
cover: 4
lora: sandmolean_pytorch_lora_weights.safetensors | Mullions | Window mullion systems: grid, spacing, repetition | — | 0.75
lora: moleansand_pytorch_lora_weights.safetensors | Dunes | Sand dunes: flow, curvature, continuity | — | 0.75
dataset: mullions | 25 cropped images of facade mullion systems | Captions from a Florence-2 workflow and Claude, edited by hand
dataset: dunes | 25 cropped images of wind-shaped sand dunes | Captions from a Florence-2 workflow and Claude, edited by hand
prompt: Facade detail on flat surface, glass curtain wall with parametric mullions derived from dune contour lines, strict grid with subtle horizontal deformation, clean separation of structure and facade, soft light — both LoRAs at 0.75, guidance 4
---
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
