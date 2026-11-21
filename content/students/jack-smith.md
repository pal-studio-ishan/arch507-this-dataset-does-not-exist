---
name: Jack Smith
title: Crockett · Villette · Oudolf
tagline: Can a LoRA rebuild a real, demolished building, not just something that looks like it?
cover: 3
prompt: Crockett + Villette + Oudolf LoRAs combined with a text prompt, FLUX.1 [dev]
note: The three LoRA files and their datasets weren't handed in, so there's nothing to download for this project yet.
---
## The question
LoRAs often give a general likeness with a "fever-dream" feel. Jack asked whether one could go further and reconstruct the actual geometry, materials and environmental logic of real places, as if from a photograph.

## What they did
- Trained three LoRAs:
  - **Crockett Technical High School** in Detroit, built in 1920 and demolished in 2025, from photos taken in its last months.
  - **Parc de la Villette** in Paris and its follies.
  - **Piet Oudolf's planting on Belle Isle**, Detroit, with a little of the Grand Parc des Docks in Paris.
- Tested each LoRA alone, then in pairs and all three together, with strength tests.

## What they found
- **Crockett:** the model picked up the masonry, window proportions and limestone details, and the prompt could show the school repaired and full of life. But it made a composite of familiar features, not an exact copy. It is good at patterns and atmosphere, less so at faithful geometry.
- **Villette:** more accurate. Clear, repeated, recognisable elements gave the model a "kit of parts".
- **Landscape:** composition, planting layout and colour worked. At wide views, individual species blurred together.
- Next step: richer captions that explain where and why each element appears, so the model can learn the logic, not just the look.
