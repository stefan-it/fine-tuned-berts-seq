import random
import sys

from dataclasses import dataclass
from pathlib import Path
from typing import List, NamedTuple


@dataclass
class Annotation:
    token: str
    tag: str


Sentence = List[Annotation]


class RandomSplit(NamedTuple):
    train_sentences: List[Sentence]
    dev_sentences: List[Sentence]
    test_sentences: List[Sentence]


def build_sentences(filename: Path) -> List[Sentence]:
    """
    Builds sentences from file: Reads a CoNLL-like file line by line. Split line into token and tag pair. Empty line
    determines a new sentence.
    :param filename: file to be parsed
    :return: List of sentences
    """
    with open(filename, "rt") as f_p:
        sentences: List[Sentence] = []
        current_annotations: Sentence = []
        for line in f_p:
            line = line.rstrip()

            if line.startswith("#"):
                continue

            if not line:
                sentences.append(current_annotations)
                current_annotations = []
                continue

            token, tag = line.split()

            current_annotations.append(Annotation(token=token, tag=tag))

    return sentences


def create_random_split(all_sentences: List[Sentence], seed: int) -> RandomSplit:
    """
    Creates one random split: 80/10/10 (Training, development, test).
    Logic is heavily taken from:
    https://github.com/kylebgorman/SOTA-taggers/blob/master/random_split.py
    :param all_sentences: list of all sentences
    :param seed: seed value for rng
    :return: New random split
    """
    random.seed(seed)
    random.shuffle(all_sentences)

    length = len(all_sentences)

    shard_size = length // 10

    train_boundary = shard_size * 8
    dev_boundary = train_boundary + shard_size

    new_train_sentences = all_sentences[:train_boundary]
    new_dev_sentences = all_sentences[train_boundary:dev_boundary]
    new_test_sentences = all_sentences[dev_boundary:]

    random_split = RandomSplit(
        train_sentences=new_train_sentences,
        dev_sentences=new_dev_sentences,
        test_sentences=new_test_sentences,
    )

    return random_split


def save_sentences(sentences: List[Sentence], output_filename: str) -> None:
    """
    Saves a list of sentences into a CoNLL-like file.
    :param sentences: list of sentences
    :param output_filename: output filename
    """
    with open(output_filename, "wt") as f_p:
        for sentence in sentences:
            annotations = "\n".join(
                f"{annotation.token} {annotation.tag}" for annotation in sentence
            )
            f_p.write(annotations)
            f_p.write("\n\n")


def save_random_split(random_split: RandomSplit, seed: int) -> None:
    """
    Saves a random split and stores them into train, dev and test files.
    :param random_split: random split to be dumped
    :param seed: seed value for rng
    """
    train_sentences, dev_sentences, test_sentences = random_split

    for sentences, sentence_filename in zip(
        [train_sentences, dev_sentences, test_sentences],
        ["train.txt", "dev.txt", "test.txt"],
    ):
        save_sentences(
            sentences=sentences, output_filename=f"{seed}_{sentence_filename}"
        )


def create_splits(input_file, num_random_splits):
    all_sentences = build_sentences(Path(input_file))

    for i in range(1, num_random_splits + 1):
        random_split = create_random_split(all_sentences, i)
        save_random_split(random_split=random_split, seed=i)


input_file = sys.argv[1]
num_random_splits = int(sys.argv[2])

create_splits(input_file, num_random_splits)
