## Quantweet Analytics: Unleash Sentiment Analysis using Quantum Techniques

This project's focus is training a NLP model employing quantum techniques, specifically utilizing the `lambeq` library.

## Prerequisites
* Python 3.8+
* Pipenv
* Familiarity with natural language processing
* Basic understanding of quantum computing

## Insights
The dataset we're working on is `sentiment140`, an extensive repository with approximately 1,6 million tweets. It follows this classification system:
* 0 = negative
* 2 = neutral
* 4 = positive

### Cleaning Data
We remove ...


### Dataset Acquisition
This dataset can be secured from [link](https://www.kaggle.com/kazanova/sentiment140).

## Illuminate the Quantum Pipeline
### Understanding the Quantum Circuit
A quantum circuit is a sequence of quantum gates, measurements and resets, mingled with real-time classical computations. 

### Our Pipeline
We apply the `lambeq` library's pipeline to transform sentences to quantum circuits. The output of this pipeline might either be a quantum circuit or a tensor network, both suitable for training.

Pipeline visual guide:
![](https://cqcl.github.io/lambeq/_images/pipeline.png)

### Preprocessing Sentences
Sentences are first stripped of hashtags and usernames present in the tweets, for this superfluous information can disrupt the training, testing, and validation stages.
The preliminary step post preprocessing in `lambeq` involves con