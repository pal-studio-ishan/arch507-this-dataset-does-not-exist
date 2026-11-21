---
name: Itamar Yahav
title: pencil_drawing
tagline: A failed render LoRA, then a pencil-drawing LoRA that imagines the sustainable buildings of tomorrow.
cover: 1
lora: pencil_drawing.safetensors | pencil_drawing | Architectural pencil drawings, mostly isometrics of rural and worn structures | pencil_drawing | 1.0 (0.8–1.25)
lora: peptides_flux.safetensors | peptides (first try) | Architectural visualisation renders | peptides style | —
dataset: pencil-drawing | 25 architectural pencil drawings, mostly isometrics, collected on Pinterest | Captions written with Claude (the caption files weren't included with the dataset)
dataset: renders-first-try | 15 renders used for the first, abandoned LoRA | Detailed captions
prompt: pencil_drawing of a desert city shaped entirely by shade, airflow, and human comfort
---
## The question
Itamar first wanted a LoRA that could turn any Rhino model into a render in the style of the visualisation studio Internoesterno. That style was too close to what Flux already does, and the images looked the same with or without the LoRA. So Itamar switched to a style Flux can't produce: fine architectural pencil drawings. The new LoRA became a way to ask a new question, prompted by a lecture by Cas Esbach and a history class on halting new construction: what does AI think truly sustainable architecture looks like?

## What they did
- Collected 25 pencil drawings, mostly isometrics of rural and corroded buildings. A Python script resized and renamed them, and Claude wrote the captions.
- Trained the LoRA with the trigger word `pencil_drawing`, then tested it on barns, schools and column details at different strengths.
- Generated twelve "sustainable futures": a net-zero home, a shopping centre, a vertical city, a floating community, an underground complex, a desert city, Archigram-style housing, a transport hub. Itamar ran each through an upscale pass.

## What they found
- The first LoRA was too generic to matter, a useful lesson in picking a style the model doesn't already know.
- The pencil LoRA produced ideas Itamar didn't expect and couldn't have come up with alone.
- Itamar's takeaways: be patient, since this is a lot of trial and error, and use AI to make something new rather than repeat what already exists.
