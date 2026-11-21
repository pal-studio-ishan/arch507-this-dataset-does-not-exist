---
name: Frank Michel
title: 1970s Soviet Interiors
tagline: Does a culturally specific dataset remove a model's Western bias? Not entirely.
cover: 1
dataset: soviet-interiors | 15 photographs of 1970s Soviet apartment interiors | Captions with the trigger phrase "Style of Flank"; some files left empty
prompt: A modest 1970s Soviet apartment living room, realistically furnished and slightly worn, featuring a low wooden wall unit filled with books, glassware, and small ornaments… Style of Flank
note: The LoRA file wasn't handed in, so there's nothing to download for this project yet.
---
## The question
If you fine-tune a model on one culture's interiors, does it stop defaulting to its own assumptions? Frank trained a LoRA on 1970s Soviet living rooms to test how much Western bias would remain.

## What they did
- Collected photographs of Soviet apartment interiors from the period and captioned them with a trigger phrase.
- Wrote twelve detailed room prompts (living room, kitchen, hallway, child's room, study, a room in winter) and generated one image for each.
- Reviewed the results with the review group, including someone who had lived in Russia.

## What they found
- The images still showed strong Western influence. The model kept adding American-style objects, especially televisions, some of them not even from the 1970s.
- It leaned into stereotypes, often producing cramped, inefficient rooms that reflected general assumptions rather than real homes.
- The base model's original training kept showing through after fine-tuning. AI doesn't fully unlearn its biases, which matters wherever accuracy and cultural authenticity count.
