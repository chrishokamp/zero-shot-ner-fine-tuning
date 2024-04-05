# Zero- to Few-Shot NER Fine Tuning Lab

After this lab, you will know how to use open source datasets, zero shot NER models, and open-source annotation interfaces to:

- quickly bootstrap datasets for a specific task
- define a entity type system, weakly annotate, and create evaluation datasets
- evaluate off-the-shelf models on specific types to establish baselines
- build configurable training datasets for new types
- fine tune smaller zero-shot models for better performance in a teacher-->student setting
- evaluate the final fine-tuned models against the baselines

## Lab Tasks

### Part 0: Setup

(1) configure your environment (install miniconda if needed)
```
conda create -n zero-shot-ner-lab python=3.10
conda activate zero-shot-ner-lab 
```

Install docker if you don't already have it

set up this repo:
`git clone https://github.com/chrishokamp/zero-shot-ner-fine-tuning`

Note: if you are using windows, we recommend setting up WSL + VSCode to avoid jumping through lots of windows-specific hoops. 

### Part 1: Collect a Dataset  

**Task: Define the domain + task** 
What kind of dataset do you want to work with? 
What types of entities are going to be important in that domain?

(3) collect a dataset by semantically filtering a large dataset
- Notebook: [semantically filter a huggingface dataset](notebooks/semantically-filter-a-huggingface-dataset.ipynb)
- possible external sources: wikidata, news articles, generated with an llm or another source
- your dataset should contain 10 documents at minimum, 100 or 1000 is better.
- if you get stuck on this step just write 10 sentences
- see the notebooks in data-generation/ for some dataset generation workflows

### Part 2: Establish a Baseline

**Task: establish baseline for the domain you defined in Part 1**

(4) define your types and annotate your dataset with GliNER 
- what types are in your dataset? make a list of them
  - types are "things" -- the kinds of spans of text that you want to label
- Notebook: [annotate dataset with gliner](notebooks/semantically-filter-a-huggingface-dataset.ipynb)

(5)  install Argilla, and annotate at least 10 items in the Argilla UI
Start the Argilla UI through their Docker image:
```
docker run -d --name quickstart -p 6900:6900 argilla/argilla-quickstart:latest
```
- After annotating, export your annotations


*** Optional: Combine annotations across groups to create a larger dataset

(6) Evaluate baseline performance
We need to evaluate performance empirically, use [nervaluate](https://github.com/MantisAI/nervaluate) to do that. 


## Part 3: Improve Performance on your domain

**Task: Improve performance and throughput by fine-tuning a task-specific model**

(7) Let's save the annotations we did manually as the evaluation set, and create a larger fine-tuning set for this task with an LLM, or with more manual annotation
- use the dataset we provide to go faster on this step, or do it yourself, using this notebook as a template
- alternatively, use the biggest GliNER model as your teacher model. 

(8) fine-tune the small zero-shot ner model to do better on your types (see example notebook)

(9) check your annotations -- did your model improve? 
- evaluate your model empirically and compare it with the baseline

### Bonus Section

Bonus: combine your data with one or more friend's data. Can you make a better or more general model?

Bonus: can you modify the GliNER architecture to do something else?

Bonus: try using OpenAI or a local llm to do the annotation task, instead of doing it manually? https://github.com/argilla-io/distilabel
https://huggingface.co/datasets/argilla/cosmopedia-ner-argilla <-- exploring an automatically labeled dataset with argilla
