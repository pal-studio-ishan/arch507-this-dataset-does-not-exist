---
name: Emily Naumann
title: le_zine
tagline: Three LoRAs trained on film, old magazines and photography, to pull AI images back toward real design.
cover: 12
lora: hoos.safetensors | hoos | Stills from the film *Phantom Thread* | in the style of hoos | 1.25–2
lora: disasterpiece.safetensors | disasterpiece | 1970s–90s architecture magazine photography | in the style of disasterpiece | 1.25–2
lora: minm | minm | Photographs by Josef Sudek and Saul Leiter | in the style of minm | 1.25
dataset: hoos | 12 film stills chosen for composition and colour | Short captions (RTF files)
dataset: disasterpiece | 18 photographs of architecture from 1970s–90s publications | Short captions (RTF files)
dataset: minm | 16 photographs by Josef Sudek (black and white) and Saul Leiter (subtle colour) | Short captions (RTF files)
prompt: cinematic architecture magazine photograph of a library carved into a desert cliff outside Marrakech, designed in the spirit of Luis Barragán and Tadao Ando… In the style of disasterpiece
---
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
