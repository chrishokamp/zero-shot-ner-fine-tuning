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

(2) install Argilla
Start the Argilla UI through their Docker image:


```
docker run -d --name quickstart -p 6900:6900 argilla/argilla-quickstart:latest
```



Bonus: can you modify the GliNER architecture to do something else?

