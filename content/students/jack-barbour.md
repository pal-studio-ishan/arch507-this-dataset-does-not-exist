---
name: Jack Barbour
title: Future Facades
tagline: Two LoRAs to get parametric brick facades with bricks at the right scale.
cover: 4
lora: bnajS-FZIGxwpbwttX7GC_pytorch_lora_weights.safetensors | Brick buildings | Freestanding brick buildings with ground and sky | — | 1.2
lora: Kz94z-4KsFaMTVGdWZotT_pytorch_lora_weights.safetensors | Brick facade close-ups | Close-ups of parametric brick facades | — | 1.2
dataset: facade-closeups | 16 close-up photographs of parametric brick facades, chosen for correct brick scale | No captions
dataset: brick-buildings | 10 photographs of whole brick buildings with ground and sky | Paragraph captions
prompt: free standing building with parametric brick facade that girates, undulates, and makes complex geometric movements that seem to defy gravity. located in a grassy field, blue sky in the background, large windows in the building, cantilevers — both LoRAs at 1.2, 35 steps
---
## The question
Ask a mainstream model for "a parametric brick facade" and you get bricks that are stretched and too thin, on forms that could never be built. Jack wanted facades with real brick scale and some constructive logic.

## What they did
- Trained a first LoRA on close-ups of parametric brick facades, chosen to show correct brick size and coursing.
- That alone gave abstract brick patterns, not buildings. So Jack trained a second LoRA on freestanding brick buildings shown with the ground and sky.
- Ran both LoRAs together at 1.2 and refined the prompt step by step, from "brick facade on a building" to a full description of the site, the windows and the cantilevers.

## What they found
- More steps didn't help much. Prompt work and the second LoRA did.
- The final images show coherent buildings with expressive brick facades and a believable sense of brick scale, which general-purpose models lack.
- Getting there took careful dataset curation and many prompt iterations. Purpose-built architectural datasets could make AI images far more reliable.
