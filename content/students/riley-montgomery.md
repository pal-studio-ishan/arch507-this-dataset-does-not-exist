---
name: Riley Montgomery
title: Upper Peninsula Understory Futures
tagline: Speculating on future plant species in Michigan's Upper Peninsula as the climate shifts.
cover: 5
hide: 19
lora: mont2.safetensors | mont2 | 12 Upper Peninsula plant species: 6 native, 6 expected to arrive | mont2 | 0.3–1.5
lora: lkjh.safetensors | lkjh | Lowbush blueberry | lkjh | 0.3–1.5
lora: mont3.safetensors | mont3 | Plastic objects | mont3 | 0.5–1.0
prompt: A close-up of lowbush blueberry plants hybridized with plastic, translucent plastic leaves and plastic berries that refract light, growing in a natural setting… lkjh, mont3 — strengths 0.5 + 1.0
note: The training images weren't handed in with the LoRAs.
---
## The question
Image models know little about less common species, especially in remote places like the Keweenaw Peninsula. Riley wanted to train a model on Upper Peninsula plants and then speculate on how climate change might reshape them. Understory plants hybridise and migrate faster, and hardiness zones are expected to shift about 13 miles a decade.

## What they did
- **mont2:** 24 images of 12 species. Six were native, from Michigan State University's list, and six currently grow two hardiness zones warmer. Every caption followed the same botanical format: view, scientific and common name, native range, height, flowers, leaves, roots, pollinators, soil.
- **lkjh:** narrowed to a single plant, the lowbush blueberry, with captions from Midjourney's describe tool.
- **mont3:** a LoRA trained on plastic objects, combined with the blueberry LoRA to imagine plastic-hybrid future plants.

## What they found
- The blueberry LoRA followed the plant closely, but the images offered little more than photographs would.
- The landscapes came out generic and every bush looked the same, because the dataset leaned toward close-ups. Riley's reviewer pointed to scale.
- The plastic hybrids raised a question Riley hadn't set out to ask, about microplastics in plants and soil.
- In hindsight Riley would pick one goal: either faithful depiction of the blueberry (LoRAs by season and scale) or speculative hybrids built from a dataset of made-up hybrids.
