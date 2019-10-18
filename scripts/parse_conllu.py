import sys

from conllu import parse_incr

filename = sys.argv[1]

with open(filename, "rt") as f_p: 
    for tokenlist in parse_incr(f_p): 
        for token in tokenlist: 
            print(token["form"], token["upostag"]) 
        print("") 
