### 1. Research question

General-purpose text-to-image models are trained to approximate a very large distribution of images, so they reproduce its densest regions most reliably. This study treats that averaging as a measurable bias. It asks whether a small, purposive dataset, attached to a frozen base model as a low-rank adapter, can insert a counter-bias: a material, a formal logic, a mode of representation or a place that the base model under-represents. Each project is an independent intervention on the same base model, so the results can be read side by side.

### 2. Baseline probing

Before collecting any data, each student probed the base model with prompts describing their target condition and documented where it failed: generic outputs, wrong materials or scales, missing references. These failed prompts serve as the control condition. Every intervention is argued against them.

### 3. Dataset construction

Datasets are small and curated by hand, between 10 and 41 images per adapter, with most between 15 and 35. Sources include the students' own photographs and 3D models, archival and published photography, film stills and drawings. Selection prioritises consistency in the target attribute, for example a correct brick scale or a single viewing condition. Images were cropped where needed to isolate it, as in the mullion and dune sets. Some students split one idea across several datasets so that separate adapters learn separable attributes, such as style vs. form, or stone texture vs. line drawing vs. façade photography.

### 4. Annotation

Captions decide what the adapter binds to its trigger and what stays controllable from the prompt. Four strategies were used, and each project page reports which:

- short hand-written captions;
- long descriptive captions covering viewpoint, structure, material, light and objects;
- captions drafted with vision-language models (Gemini, Claude, a Florence-2 workflow) and then edited by hand;
- in one case, no captions at all.

Where a trigger was used, it is usually a rare token (`C_at_el`, `architamer`, `stoneybaloney`) prefixed to every caption, so it doesn't collide with concepts the model already holds.

### 5. Training

- **Base model:** FLUX.1 [dev], a 12-billion-parameter rectified-flow transformer.
- **Adapter:** each LoRA learns a rank-16 update to the transformer's weights, and the text encoders stay frozen. At inference the update is scaled by a strength *s*, so W′ = W + *s*·ΔW.
- **Training run:** adapters were trained with fal.ai's hosted FLUX LoRA trainer and exported as diffusers-format safetensors of about 86 MB each.
- **Output:** 25 adapters from 12 students. Three further projects were submitted as images and write-ups without weights.

### 6. Inference and evaluation

Students tuned adapter strength, trigger placement and prompt structure against base-model outputs. The working strength ranges each student reported, from 0.3 to 2.0, are listed with every LoRA. Each project concludes in a sequence of twelve images, suggested as four phases of three:

1. establishing the inserted visual language;
2. applying it across scales and conditions;
3. transforming it through new material, formal or atmospheric possibilities;
4. pushing it into speculative territory.

The set has to show a repeatable system with a distinct identity, not a one-off effect. A written statement places each intervention both technically and conceptually. Projects are assessed qualitatively on five criteria:

- the strength of the argument;
- the specificity of the intervention;
- the coherence of the sequence;
- the fit between dataset, images and text;
- the degree of authorship over generic generation.

### 7. Controlled cross-adapter comparison

To isolate each adapter's effect, one prompt is rendered through the base model and all 25 adapters, with each adapter's trigger word added. Every other variable is held fixed:

- seed 507507;
- 28 steps;
- guidance 3.5;
- euler sampler, simple scheduler;
- 1344×768;
- fp8 weights;
- strength 1.0.

A second pass sets each adapter to the middle of its student's recommended range. The results are under *One prompt, every LoRA*.

### 8. Provenance and verification

Some weights were submitted with machine-generated filenames. Each was identified by rendering same-seed tests with the student's own documented prompts and settings, then matching the results against their review material. Published files are renamed to clear names and checked by SHA-256 against the submitted originals.

### 9. Release and data governance

Adapters are released on Hugging Face under the FLUX.1 [dev] Non-Commercial License, credited to each student. Training images are published in full only where they are the student's own work, in the public domain or openly licensed. Other datasets appear as captions, source lists and small thumbnails.

### 10. Limitations

- Datasets are small and evaluation is qualitative. There is no held-out set or quantitative metric.
- Trainer settings beyond rank were not recorded for every run.
- Adapter strength works differently from one LoRA to the next. At a shared strength of 1.0 some adapters take over the image and others barely register, so cross-project comparisons should be read alongside each student's own tests.
