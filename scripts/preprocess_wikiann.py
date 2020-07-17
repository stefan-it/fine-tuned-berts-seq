import sys

split_filename = sys.argv[1]

with open(split_filename, "rt") as f_p:
    for line in f_p:
        line = line.rstrip()
        
        print("".join(line.split(":")[1:]))