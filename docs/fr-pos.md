# Universal Dependencies: French PoS tagging

We use the following datasets for PoS tagging experiments for French:

| Dataset | # Sentences | Repository
| ------- | ----------- | ----------
| ParTUT  |  1,020      | [here](https://github.com/UniversalDependencies/UD_French-ParTUT/tree/dev)
| GSD     | 16,342      | [here](https://github.com/UniversalDependencies/UD_French-GSD/tree/dev)
| Sequoia |  3,099      | [here](https://github.com/UniversalDependencies/UD_French-Sequoia/tree/dev)
| FQB     |  2,289      | [here](https://github.com/UniversalDependencies/UD_French-FQB/tree/dev)
| Spoken  |  2,786      | [here](https://github.com/UniversalDependencies/UD_French-Spoken/tree/dev)
| PUD     |  1,000      | [here](https://github.com/UniversalDependencies/UD_French-PUD/tree/dev)
| FTB     | 18,535      | [here](https://github.com/UniversalDependencies/UD_French-FTB/tree/dev)

# Preprocessing I

Just clone the repository for a specific dataset and use the `dev` branch:

```bash
git clone -b dev https://github.com/UniversalDependencies/UD_French-ParTUT
```

Use the CoNLL-U helper script to parse the dataset:

```bash
python3 parse_conllu.py UD_French-ParTUT/fr_partut-ud-train.conllu > train.txt.tmp
python3 parse_conllu.py UD_French-ParTUT/fr_partut-ud-dev.conllu > dev.txt.tmp
python3 parse_conllu.py UD_French-ParTUT/fr_partut-ud-test.conllu > test.txt.tmp
```

# Preprocessing II

We use a max. sequence length of 128 subtokens. Longer sentences are split
with the `preprocess.py` script:

```bash
python3 preprocess.py train.txt.tmp bert-base-multilingual-cased 128 > train.txt
python3 preprocess.py dev.txt.tmp bert-base-multilingual-cased 128 > dev.txt
python3 preprocess.py test.txt.tmp bert-base-multilingual-cased 128 > test.txt
```

# Preprocessing III

In the last step, all PoS tagging tags (= tagset) must be extracted:

```bash
cat train.txt dev.txt test.txt | cut -d " " -f 2 | grep -v "^$" | sort | uniq > labels.txt
```

# Training

After the dataset has been preprocessed, training and fine-tuning of a PoS
tagging model can be started with:

```bash
...
```