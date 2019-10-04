# 🤗 + ⚛️ Fine-tuned Transformers compatible BERT models for Sequence Tagging

This repository contains fine-tuned [Transformers](https://github.com/huggingface/transformers)
compatible BERT models for sequence tagging tasks like NER or PoS tagging.

We use the ([coming soon](https://github.com/huggingface/transformers/pull/1275))
fine-tuning NER example from the awesome [Transformers](https://github.com/huggingface/transformers)
repository.

# Changelog

* 23.09.2019: PoS tagging results on
  [German HDT](https://universaldependencies.org/treebanks/de_hdt/index.html) added
* 21.09.2019: Initial release of this repo. Publicly available models are coming soon!

# CoNLL datasets

For NER tasks, the CoNLL 2002 and 2003 datasets are used. The following
languages are covered: German, English, Dutch and Spanish.

These models are trained with a max. sequence length of 128.

❔ But what happens, if a sentence in the dataset is longer than 128 subtokens?
We simply split longer sentences into smaller ones. We **do not** ✂️ sentences,
which would be bad for evaluation!

❔ What is current state-of-the-art for fine-tuned models? Well, we mainly
compare our models to the following two papers:

* ["How multilingual is Multilingual BERT?"](https://arxiv.org/abs/1906.01502)
  by Pires, Schlinger and Garrette (2019)

* ["Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT"](https://arxiv.org/abs/1904.09077)
  by Wu and Dredze (2019)

❔ We use a max. sequence length of 128 and a batch size of 32. These are the
same parameters as used by Pires, Schlinger and Garrette (2019).

## Results

We report an averaged F1-score of 5 different runs. We use different seeds for
each run. The official CoNLL evaluation script from
[here](https://www.clips.uantwerpen.be/conll2003/ner/bin/conlleval) is used.

### English

| Model                    | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg.
| ------------------------ | ----- | ----- | ----- | ----- | ----- | ---------
| BERT base, cased (Dev)   | 95.13 | 95.29 | 95.07 | 95.12 | 95.53 | 95.23
| BERT base, cased (Test)  | 90.89 | 90.76 | 90.82 | 91.09 | 91.60 | 91.03
| BERT large, cased (Dev)  | 95.69 | 95.47 | 95.77 | 95.86 | 95.91 | 95.74
| BERT large, cased (Test) | 91.73 | 91.17 | 91.77 | 91.22 | 91.46 | **91.47**

Pires, Schlinger and Garrette (2019) report a F1-score of 91.07% using the
*EN-BERT* model.

### German

**Notice**: For this experiment we use the original CoNLL-2003 data. The dataset
also includes an 2006 update that fixes various MISC annotations. However, it
turns out that most papers are not using the updated 2006 version of the
dataset. So in this experiment, we use the "old" dataset in order to achieve
a better comparison to other papers. See a more detailed discussion about this
dataset in [here](https://github.com/zalandoresearch/flair/issues/1102).

We use three BERT models:

* Multilingual BERT (base and cased), further called *mBERT*
* German BERT (base and cased) from [here](https://deepset.ai/german-bert)
* An own trained German BERT (base and cased), currently unreleased

| Model                              | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg.
| ---------------------------------- | ----- | ----- | ----- | ----- | ----- | ---------
| mBERT base, cased (Dev)            | 86.04 | 85.64 | 86.04 | 85.10 | 83.16 | 85.20
| mBERT base, cased (Test)           | 83.02 | 82.80 | 82.56 | 82.21 | 82.14 | 82.55
| German BERT base, cased (Dev)      | 87.33 | 86.34 | 87.05 | 86.52 | 86.80 | 86.81
| German BERT base, cased (Test)     | 83.84 | 83.98 | 83.62 | 83.70 | 83.37 | 83.70
| Own German BERT base, cased (Dev)  | 86.66 | 86.75 | 87.06 | 86.61 | 87.22 | 86.86
| Own German BERT base, cased (Test) | 84.32 | 84.47 | 84.76 | 84.38 | 84.68 | **84.52**

Pires, Schlinger and Garrette (2019) report a F1-score of 82.00% for their
fine-tuned multilingual BERT model, whereas Wu and Dredze (2019) report a
F1-score of 82.82%.

### Dutch

| Model                    | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg.
| ------------------------ | ----- | ----- | ----- | ----- | ----- | ---------
| mBERT base, cased (Dev)  | 90.73 | 91.11 | 90.82 | 90.94 | 91.05 | 90.93
| mBERT base, cased (Test) | 90.94 | 90.29 | 90.10 | 90.32 | 90.27 | **90.38**

Pires, Schlinger and Garrette (2019) report a F1-score of 89.86% for their
fine-tuned multilingual BERT model, whereas Wu and Dredze (2019) report a
F1-score of 90.94%.

### Spanish

| Model                    | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg.
| ------------------------ | ----- | ----- | ----- | ----- | ----- | ----------
| mBERT base, cased (Dev)  | 86.50 | 86.25 | 86.44 | 86.99 | 86.70 | 86.576
| mBERT base, cased (Test) | 87.80 | 87.93 | 87.92 | 87.00 | 87.53 | **87.636**

Pires, Schlinger and Garrette (2019) report a F1-score of 87.18% for their
fine-tuned multilingual BERT model, whereas Wu and Dredze (2019) report a
F1-score of 87.38%.

# GermEval 2014

We train three models for the [GermEval 2014](https://sites.google.com/site/germeval2014ner/)
shared task: mBERT, German BERT and our own German BERT model.

**Notice**: the original dataset includes some strange character control
sequences (all labeled with "O" tag). We remove them in a pre-processing
step (for train/dev/test sets).

## Results

We report averaged F1-score over 5 different runs (with different seeds).
The [official evaluation script](https://sites.google.com/site/germeval2014ner/evaluation)
is used for evaluation. We report the *Strict, Combined Evaluation (official)*
metric here.

| Model                              | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg.
| ---------------------------------- | ----- | ----- | ----- | ----- | ----- | ---------
| mBERT base, cased (Dev)            | 86.97 | 87.04 | 86.66 | 87.11 | 86.53 | 86.86
| mBERT base, cased (Test)           | 85.90 | 86.37 | 86.47 | 86.56 | 86.00 | 86.26
| German BERT base, cased (Dev)      | 87.36 | 87.03 | 87.55 | 87.53 | 87.23 | 87.34
| German BERT base, cased (Test)     | 86.35 | 86.93 | 86.71 | 86.85 | 86.23 | 86.61
| Own German BERT base, cased (Dev)  | 87.74 | 87.7  | 87.77 | 87.96 | 88.52 | 87.94
| Own German BERT base, cased (Test) | 86.96 | 86.85 | 87.01 | 86.89 | 86.73 | **86.89**

# Universal Depedencies

## German HDT

We train three models (mBERT, German BERT and our own German BERT model) on the
recently released [German HDT](https://universaldependencies.org/treebanks/de_hdt/index.html)
Universal Dependencies corpus. It contains over 200K annotated sentences,
resulting in one of the largest UD corpora. We use the latest data from the `dev`
branch on the German HDT
[repository](https://github.com/UniversalDependencies/UD_German-HDT/tree/dev).

### Results

We report averaged accuracy over 5 different runs (with different seeds).

| Model                              | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Avg.
| ---------------------------------- | ----- | ----- | ----- | ----- | ----- | ---------
| mBERT base, cased (Dev)            | 98.36 | 98.35 | 98.36 | 98.36 | 98.36 | 98.35
| mBERT base, cased (Test)           | 98.58 | 98.57 | 98.58 | 98.58 | 98.58 | **98.58**
| German BERT base, cased (Dev)      | 98.37 | 98.37 | 98.37 | 98.39 | 98.35 | 98.37
| German BERT base, cased (Test)     | 98.57 | 98.55 | 98.57 | 98.54 | 98.57 | 98.56
| Own German BERT base, cased (Dev)  | 98.38 | 98.38 | 98.39 | 98.37 | 98.36 | 98.38
| Own German BERT base, cased (Test) | 98.57 | 98.56 | 98.56 | 98.57 | 98.58 | 98.57

# ToDo

* [ ] Release models (incl. `BertTokenizer` and `BertModel` example usage)
* [ ] Provide more details about training parameters, and prediction script
* [ ] Release own trained BERT models: German (cased, uncased) and Historic German (cased, uncased)