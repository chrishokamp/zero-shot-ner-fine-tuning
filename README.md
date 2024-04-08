# Zero- to Few-Shot NER Fine Tuning Lab

After this lab, you will know how to use open source datasets, zero shot NER models, and open-source annotation interfaces to:

- quickly bootstrap datasets for a specific entity recognition task
- define a entity type system, weakly annotate, and create evaluation datasets for your task
- evaluate off-the-shelf models on specific entity types to establish baselines
- build configurable training datasets for new entity types
- fine tune smaller zero-shot models for better performance in a teacher-->student setting
- evaluate the final fine-tuned models against the baselines

## Lab Tasks

### Part 0: Setup

(1) configure your environment (install miniconda if needed)     
Note: if you are using windows, we generally recommend setting up WSL + VSCode to avoid jumping through lots of windows-specific hoops.      
```
conda create -n zero-shot-ner-lab python=3.10
```

[Install docker](https://docs.docker.com/engine/install/) if you don't already have it. You will need Docker for the Argilla UI annotation step in Part 2.

set up this repo:       
`git clone https://github.com/chrishokamp/zero-shot-ner-fine-tuning`     

Now install:
```
cd zero-shot-ner-fine-tuning
conda activate zero-shot-ner-lab 
pip install -r requirements.txt
```

we also need to install the FAISS library for vector search - there are a few different installation options for this, see the first notebook in [notebooks](notebooks/) for all of them:
```
conda install -c pytorch faiss-cpu
```


### Part 1: Collect a Dataset  

**Task: Define the domain + task**       
What kind of data do you want to work with?   
What problem are you going to solve?     
What types of entities are going to be important in that domain?      
If you are doing this lab in a group setting it's nice to define the task together.

(3) collect a domain-specific dataset by semantically filtering a large dataset      
- Notebook: [semantically filter a huggingface dataset](notebooks/part-1-semantically-filter-a-huggingface-dataset.ipynb)
- your dataset should contain 10 documents at minimum, 100 or 1000 is better.
- if you get stuck on this step just write 10 sentences

Alternatives to semantic filtering:
- possible external sources: wikidata, news articles, generated with an llm, domain-specific sources


### Part 2: Establish a Baseline

**Task: establish baseline for the domain you defined in Part 1**

(4) define your Entity types and annotate your dataset with GliNER 
- what types are in your dataset? make a list of them
  - types are "things" -- the kinds of spans of text that you want to label
  - the list of entity types you make will look something like: `["referee", "vollyball player", "sports fan", "food vendor", ...]`
- Notebook: [annotate dataset with gliner](notebooks/part-2-semantically-filter-a-huggingface-dataset.ipynb)

(5) Make the evaluation dataset: install Argilla, and annotate at least 10 items in the Argilla UI
Start the Argilla UI through their Docker image:
```
docker run -d --name quickstart -p 6900:6900 argilla/argilla-quickstart:latest
```
- After annotating, export your annotations

**Optional: In a group setting, combine annotations across groups to create a larger dataset**

(6) Evaluate baseline performance
We need to evaluate performance empirically, use [nervaluate](https://github.com/MantisAI/nervaluate) to do that. 

## Part 3: Improve Performance on your domain

**Task: Improve performance and throughput by fine-tuning a task-specific model**

(7) Let's save the annotations we did manually as the evaluation set, and create a larger fine-tuning set for this task with an LLM, or with more manual annotation
- use the dataset we built earlier to go faster on this step, or do it yourself by annotating more data

(8) fine-tune a small zero-shot ner model to do better on your types (see example notebook)
- Notebook: [fine-tune and evaluate custom gliner model](notebooks/part-3-finetune-gliner.ipynb)

(9) check your annotations -- did your model improve? 
- evaluate your model empirically and compare it with the baseline

### Bonus Section

Bonus: combine your data with one or more friend's data. Can you make a better or more general model?

Bonus: can you modify the GliNER architecture to do something else?

Bonus: try using OpenAI or a local llm to do the annotation task, instead of doing it manually? https://github.com/argilla-io/distilabel
https://huggingface.co/datasets/argilla/cosmopedia-ner-argilla <-- exploring an automatically labeled dataset with argilla
