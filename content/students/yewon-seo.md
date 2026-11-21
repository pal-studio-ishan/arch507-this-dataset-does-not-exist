---
name: Yewon Seo
title: Render a Lamp
tagline: Style + form = ? A SANAA-style LoRA and a LoRA of Yewon's own product design, mixed to render a planter lamp.
cover: 2
lora: FLUX 1_LORA_asdf.safetensors | asdf (style) | Photographs of SANAA buildings: white, light, minimal | asdf style | 1.6
lora: FLUX 1_LORA_qwer.safetensors | qwer (form) | Renders of Yewon's own S-shaped planter-lamp model | — | 1.0
dataset: style-sanaa | 27 photographs of SANAA buildings (Zollverein School, Kanazawa, Rolex Learning Center, Grace Farms and others; full credits in the review slides) | Precise captions describing light, materials and object positions
dataset: form-lamp | 30 renders of Yewon's own Rhino model of the planter lamp (ProtoLiO Growing Light) | Captions describing each loop, cut-out and viewing angle
prompt: Photo of a plant pot with a growing light. S-shaped body holds the earth inside and has a lighting panel on the top. Ivy is planted inside, which is sealed with a translucent sheet… asdf style — style 1.6, form 1.0, DepthAnything ControlNet
note: No written analysis was handed in. This summary comes from the review slides.
---
## The question
Can one LoRA carry a *style* and another a *form*, and can mixing them render a real design? Yewon tested it on a product of their own: a planter with a growing light, rendered in the soft, white light of SANAA's architecture.

## What they did
- Trained a **style** LoRA on photographs of SANAA buildings and a **form** LoRA on renders of Yewon's own Rhino model of the S-shaped planter lamp.
- Compared a text-only prompt with prompts that used the LoRAs, then mapped a grid of strengths: style from 1.2 to 2.0 with form fixed, and the reverse.
- Tested five ControlNets (DepthAnything, LineArt, Canny, HED, Binary) and settled on depth with style 1.6 and form 1.0.
- Made the final series by keeping everything fixed and changing only the noise seed.

## What the tests looked at
- How much of the lamp's real shape survives when the style LoRA is turned up.
- Which kind of ControlNet keeps the form while letting the style change the material and light.
- How much one fixed setup varies from seed to seed.
