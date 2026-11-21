---
name: Michael Natinsky
title: AI as a Drawing Tool
tagline: Generating architectural elevations in the flat, colourful style of Sander Patelski.
cover: 2
lora: Patelski.safetensors | Patelski | Sander Patelski's graphic elevations | Style of michaelset / Patelski Elevations | 1.0
lora: Elevations.safetensors | Elevations | Plain architectural elevation drawings | — | 1.0
dataset: patelski | 18 elevation drawings by Sander Patelski | Captions describing each drawing
dataset: elevations | 19 basic architectural elevation drawings | Captions describing each drawing
prompt: Graphic architectural elevation drawing in the style of Sander Patelski, an early modern bauhaus style glass and pastel building. Bright saturated colors… Style of michaelset
---
## The question
Could AI be a real design tool for elevations, generating facade patterns and compositions worth bringing into your own work? Midjourney's attempts at elevations mostly failed, so Michael trained custom LoRAs.

## What they did
- Trained one LoRA on Sander Patelski's flat, colourful elevations and a second on plain architectural elevation drawings.
- Pushed the style across very different prompts: a Bauhaus pastel building, a Chicago skyscraper in the rain, a stone European village, and buildings in the spirit of Barragán, Herzog & de Meuron, Zumthor and Ando.

## What they found
- The Patelski style dominated. Even when Michael asked for brick, wood or stone, it fell back on flat pastel colours, and buildings floated in empty space unless the prompt forced context in.
- The landscape aspect ratio cut skyscrapers off. The model wouldn't show the full height.
- The drawing LoRA added window rhythms and some sketchy drafting lines.
- The model rearranges patterns rather than designing. It understands neither structure nor material. This tool may be best for presenting your own work, for example by running your elevations through it with ControlNet, which Michael planned but couldn't get running.
