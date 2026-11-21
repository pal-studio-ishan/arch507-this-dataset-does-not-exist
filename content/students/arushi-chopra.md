---
name: Arushi Chopra
title: Bambu
tagline: A LoRA for traditional bamboo joinery: lashing, dowels and culm bundles across vernaculars.
cover: 4
lora: borsch_t.safetensors | borsch_t | Bamboo architecture (one of two LoRAs) | — | 1.25–2.0
lora: too_late_pytorch_lora_weights.safetensors | too_late | Bamboo architecture (one of two LoRAs) | — | 1.0–1.75
dataset: bamboo | 35 photographs of architectural bamboo joinery: lashing and dowel details, roofs, columns, beams and stairs (sources: Guadua Bamboo, Bamboo Batu, Bamboo U, VTN Architects) | Detailed captions naming the joint, the culm size, the lashing and the regional tradition
prompt: Cinematic architecture magazine photograph of a bamboo sleeping pavilion interior in a Vietnamese vernacular using traditional multi-culm bundle columns with dark coir lashing… Film photograph shot on Ilford HP5 black and white film — LoRA 1.25, guidance 4.0
note: No written analysis was handed in. This summary comes from the review slides.
---
## The question
Base models can draw "a bamboo building" but not how bamboo actually goes together: the lashing at a node, a bundle of culms acting as a column, split-culm roof tiles. Arushi collected niche images of real joinery to see if a LoRA could carry those details into new buildings.

## What they did
- Built a dataset of bamboo joinery photographs from practices known for bamboo, with captions describing each joint in detail.
- Trained two LoRAs and compared each prompt with and without them.
- Made a series called *Culm*, moving through regional traditions: Latin American, Vietnamese, Javanese, Filipino, Indian and Japanese. Many prompts asked for black-and-white film photography (Ilford, Tri-X, Neopan).
- In the last images Arushi used both LoRAs together (2.0 and 1.0) with very short prompts, to see how much the LoRAs carried on their own.

## What the tests looked at
- Whether natural patterns such as woven screens and shadows come through.
- Whether lashing and structural logic hold up in new building types: bridges, market halls, porches, tea houses.
- How far the bamboo details survive when the prompt gives almost no detail.
