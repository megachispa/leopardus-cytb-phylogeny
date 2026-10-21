from Bio import AlignIO

alignment = AlignIO.read("cytb_aligned.fasta", "fasta")

print("Number of sequences:", len(alignment))
print("Alignment length:", alignment.get_alignment_length())

for record in alignment:
    seq = str(record.seq).upper()
    print(
        record.id,
        "length =", len(seq),
        "gaps =", seq.count("-"),
        "Ns =", seq.count("N")
    )
