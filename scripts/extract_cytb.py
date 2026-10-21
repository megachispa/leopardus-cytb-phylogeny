from Bio import SeqIO

input_file = "sequence.gb"
output_file = "cytb.fasta"

cytb_records = []

for record in SeqIO.parse(input_file, "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            gene = feature.qualifiers.get("gene", [""])[0]

            if gene.upper() == "CYTB":
                seq = feature.extract(record.seq)

                species = record.annotations["organism"].replace(" ", "_")

                seq_record = record[:0]
                seq_record.id = species
                seq_record.name = species
                seq_record.description = record.id
                seq_record.seq = seq

                cytb_records.append(seq_record)

SeqIO.write(cytb_records, output_file, "fasta")

print(f"Extracted {len(cytb_records)} CYTB sequences")

for record in cytb_records:
    print(record.id, len(record.seq))
