from setuptools import setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


with open('VERSION') as f:
    version = f.read().strip()


setup(
    name="zero_shot_ner_lab",
    version=version,
    packages=['zero_shot_ner_lab'],
    install_requires=requirements,
    extras_require={
        'gpu':  ['spacy[cuda12x]>=3.7.4'],
    }
)
