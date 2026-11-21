---
name: Tamer Tubishat
title: Lithic Hospitality
tagline: Against the average: teaching the model the yellow stone, stairs and open doors of As-Salt, Jordan.
cover: 4
lora: Tamer Tubishat_LoRA_As-Salt city of stairs and yellow stone.safetensors | architamer | As-Salt, Jordan: yellow limestone, hillside urbanism, stair-streets, hospitality halls | architamer | 1.0
dataset: as-salt | 35 photographs of As-Salt: limestone houses, arcades, stair-streets, madafa (hospitality) halls, the city on its slopes | Short captions starting with the trigger word "architamer"
prompt: architamer, a narrow pedestrian "stair-street" in As-Salt, steep limestone steps carved into the hillside, towering yellow stone walls on either side, iron railings, overhead wires crossing the blue sky, cinematic architectural perspective
---
## The question
Generative models get their power from breadth, and that breadth comes from averaging, which flattens specific places. Asked for "a house in As-Salt, Jordan", base Flux produced generic Mediterranean or "Arab" buildings. Tamer argued that As-Salt's identity matters enough to be learned.

## What they did
- Built a dataset to "recover and exaggerate" what was missing: the golden-yellow local limestone, buildings cascading down steep slopes, public stair-streets, and the *madafa*, a hospitality hall tied to an "architecture of the open door".
- Trained a LoRA with the trigger word `architamer` and compared the results with the base model, before and after.
- Sequenced twelve images in four phases: visual language, scale and condition, atmosphere and hospitality, and speculative futures.

## What they found
- The trigger word held material and form steady across scales, from a single window to the whole city, and through sunsets, rain and night.
- It made a "future-primitive" Salti modernism imaginable, though some contradictory ideas such as a futuristic vertical garden didn't work.
- The designer's job is to stop accepting a model's defaults and start shaping them to protect cultural and site-specific identity.
