---
name: Angelica Facey
title: Memory
tagline: Teaching a razor-sharp model the grain, blur and quiet of old photographs.
cover: 3
lora: C_at_el.safetensors | C_at_el | Forest paths and canopy light | C_at_el | 1.0 (main)
lora: YO_c_me_T.safetensors | YO_c_me_T | Mountain and valley panoramas | YO_c_me_T | 0.75 (second)
dataset: forest | 25 black-and-white forest photographs (Robert Adams, *An Old Forest Road*) | Captions co-written with Gemini, each starting with the trigger word
dataset: mountain | 15 black-and-white mountain photographs (Ansel Adams, Alma Lavenson, Carleton Watkins, Adam Clark Vroman) | Captions co-written with Gemini, each starting with the trigger word
prompt: Delicate clusters of tiny, white flowers and blades of grass grow from the edges of a calm, sleeping lake — C_at_el 1.0 + YO_c_me_T 0.75, Flux guidance 5
---
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
