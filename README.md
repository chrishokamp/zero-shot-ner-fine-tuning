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
We will be using Argilla for data annotation.

There are two ways to use Argilla in the scope of this lab.

1: Hosting Argilla on HuggingFace Spaces

2: Hosting Argilla locally with Docker

Hosting Argilla on HuggingSpace is streamlined and it is the faster way to do it. If you are hosting for free, unfortunately, the storage will not be consistent. That means the data will not be there anymore after the HF Space resets. This is not an issue for this lab since the data annotation is not the whole focus.

You annotations will persist on local storage on docker.

Using Argilla is recommended for its convenience. Installing docker and Argilla through Docker could slow you down.

To deploy Argilla in HF Spaces; see [this page](https://docs.argilla.io/latest/getting_started/quickstart/), and follow the "Deploy on HF Spaces" button. If you do this, you'll need to replace the `api_url` to the HF Space URL in the Part 2 notebook.

On the other hand, if you'd like to take the docker route, [install docker](https://www.docker.com/get-started/) if you don't already have it.
Check the [doc](https://docs.argilla.io/latest/getting_started/how-to-deploy-argilla-with-docker/) for setting up Argilla using Docker.

Get this repo to your local:       
`git clone https://github.com/chrishokamp/zero-shot-ner-fine-tuning`     

Now install libraries/dependencies:
```
cd zero-shot-ner-fine-tuning
conda activate zero-shot-ner-lab 
pip install -r requirements.txt
```

We also need to install the FAISS library for vector search - there are a few different installation options for this, see the first notebook in [notebooks](notebooks/) for all of them:
```
pip install faiss-cpu
```


### Part 1: Collect a Dataset  

**Task: Define the domain + task**       

Try to answer the questions below to set the direction of the lab for you.

**1. What domain would you like to work in?**

The domain could be anything; as big as sports, entertainment, healthcare, finance or as niche as keyboards, luxury watches, cancer research. Since we will be semantically filtering a larger, more general dataset, going very niche could hurt your data quality. This is OK in the spirit of experimentation.

**2. What problem are you going to solve?**

For instance, a luxury watch brand could be interested keeping a tab on what's happening with their competitors or a company could be looking for academic researcers to peer-review their research.

**3. What types of entities are going to be important in that domain?**
Think around the domain and the problem, this will point you in the right direction. For the luxury watch brand keeping the tab on competitors scenario, interesting entity types could be 'organization', 'product', 'event' etc. 

(3) collect a domain-specific dataset by semantically filtering a large dataset      
- Notebook: [semantically filter a huggingface dataset](notebooks/part-1-semantically-filter-a-huggingface-dataset.ipynb)
- your dataset should contain 10 documents at minimum, 100 or 1000 is better.
- if you get stuck on this step just write 10 sentences

Alternatives to semantic filtering:
- possible external sources: wikidata, news articles, generated with an llm, domain-specific sources

### Part 2: Establish a Baseline

**Task: establish a baseline for the domain-specific dataset you defined in Part 1**

(4) define your Entity types and annotate your dataset with GliNER 
- what types are in your dataset? make a list of them
  - types are "things" -- the kinds of spans of text that you want to label
  - the list of entity types you make will look something like: `["referee", "vollyball player", "sports fan", "food vendor", ...]`
- Notebook: [annotate dataset with gliner](notebooks/part-2-annotate-with-gliner-review-in-argilla.ipynb)

(5) Make the evaluation dataset: annotate at least 10 items in the Argilla UI. 

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
