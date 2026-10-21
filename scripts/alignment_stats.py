from Bio import AlignIO
from collections import Counter

alignment = AlignIO.read("cytb_aligned.fasta", "fasta")

length = alignment.get_alignment_length()

constant = 0
variable = 0
informative = 0
singleton = 0

for i in range(length):
    column = [record.seq[i].upper() for record in alignment]
    counts = Counter(column)

    if len(counts) == 1:
        constant += 1
    else:
        variable += 1

        repeated_states = sum(1 for count in counts.values() if count >= 2)

        if repeated_states >= 2:
            informative += 1
        else:
            singleton += 1

print("Alignment length:", length)
print("Constant sites:", constant)
print("Variable sites:", variable)
print("Parsimony-informative sites:", informative)
print("Singleton variable sites:", singleton)
