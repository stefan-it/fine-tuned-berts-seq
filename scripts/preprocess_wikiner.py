import sys

filename = sys.argv[1]


def parse_file(filename: str):
    with open(filename, "rt") as f_p:
        for line in f_p:
            line = line.rstrip()

            if not line:
                continue

            # Convert
            # L'|DET:ART|O Afghanistan|NAM|I-LOC a|VER:pres|O pour|PRP|O codes|NOM|O :|PUN|O
            # into CoNLL-like format:
            # token ner
            print(
                "\n".join(f"{' '.join(word.split('|')[::2])}" for word in line.split())
            )

            print("")


parse_file(filename)
