Zero- to Few-Shot NER Fine Tuning Lab

This lab shows students how to use new open source zero shot NER models, general purpose LLM APIs, and open-source annotation interfaces to:

- define new type(s) and create evaluation datasets for them
- quickly evaluate off-the-shelf models on specific types
- build configurable training datasets for new types
- fine tune zero-shot models for better performance
- evaluate fine-tuned models

### Lab Tasks
(1) configure your environment (install miniconda if needed)
```
conda create -n zero-shot-ner-lab python=3.10
conda activate zero-shot-ner-lab 
```

Install Docker if needed


(2) install Argilla
Start the Argilla UI through their Docker image:


```
docker run -d --name quickstart -p 6900:6900 argilla/argilla-quickstart:latest
```

(3) collect a dataset of events from wikidata

(4) what types are in your dataset? make a list of them

(5) annotate your dataset with GliNER and look at it in the Argilla UI

(6) After annotating, export your annotations

We need to evaluate performance, use [nervaluate](https://github.com/MantisAI/nervaluate) to do that. 

(7) Let's save the annotations we did manually as the evaluation set, and create a larger fine-tuning set for this task with an LLM, or with more manual annotation
- use the dataset we provide to go faster on this step, or do it yourself, using this notebook as a template

(8) fine-tune the zero-shot ner model to do better

(9) check your annotations -- did your model improve? 

### Bonus Section

Bonus: can you modify the GliNER architecture to do something else?

Bonus: try using OpenAI or a local llm to do the annotation task, instead of doing it manually? https://github.com/argilla-io/distilabel
https://huggingface.co/datasets/argilla/cosmopedia-ner-argilla <-- exploring an automatically labeled dataset with argilla
