from genomic_io import generate_fastq, Fastq

import os
from io import StringIO
import gzip

fasta_contents=\
""">gene_1
ACGTAAAA
CCCCGGGG
TTTTATAT
>gene_2
TTTTTTTT
AAAAAAAA
TATATATA
GT"""

# Expected sequences for lengths 20 and 21
EXPECTED_SEQUENCES = \
"""ACGTAAAACCCCGGGGTTTT
CGTAAAACCCCGGGGTTTTA
GTAAAACCCCGGGGTTTTAT
TAAAACCCCGGGGTTTTATA
AAAACCCCGGGGTTTTATAT
TTTTTTTTAAAAAAAATATA
TTTTTTTAAAAAAAATATAT
TTTTTTAAAAAAAATATATA
TTTTTAAAAAAAATATATAT
TTTTAAAAAAAATATATATA
TTTAAAAAAAATATATATAG
TTAAAAAAAATATATATAGT
ACGTAAAACCCCGGGGTTTTA
CGTAAAACCCCGGGGTTTTAT
GTAAAACCCCGGGGTTTTATA
TAAAACCCCGGGGTTTTATAT
TTTTTTTTAAAAAAAATATAT
TTTTTTTAAAAAAAATATATA
TTTTTTAAAAAAAATATATAT
TTTTTAAAAAAAATATATATA
TTTTAAAAAAAATATATATAG
TTTAAAAAAAATATATATAGT"""


def main():
    fasta_file     = "sample.fa.gz"
    sample_output  = "sample_out.fastq.gz"

    with gzip.open(fasta_file, "wt") as output_stream:
        print(fasta_contents, file=output_stream)

    generate_fastq.generate_reads(fasta_file  = fasta_file,
                                  length_min  = 20,
                                  length_max  = 21,
                                  output_file = sample_output)

    fastq_handle = Fastq.FastqFile(sample_output)

    text_list = list()
    for entry in fastq_handle:
        text_list.append(entry.sequence)

    generated_sequences = "\n".join(text_list)

    if generated_sequences == EXPECTED_SEQUENCES:
        print("Sequence Generation is Working!!!")
    else:
        print("There was an error! The generated sequences are:")
        print(generated_sequences)

    os.remove(fasta_file)
    os.remove(sample_output)



main()



"""
Sequence Generation:

ACGTAAAACCCCGGGGTTTTATAT

ACGTAAAACCCCGGGGTTTT
CGTAAAACCCCGGGGTTTTA
GTAAAACCCCGGGGTTTTAT
TAAAACCCCGGGGTTTTATA
AAAACCCCGGGGTTTTATAT

TTTTTTTTAAAAAAAATATATATAGT

TTTTTTTTAAAAAAAATATA
TTTTTTTAAAAAAAATATAT
TTTTTTAAAAAAAATATATA
TTTTTAAAAAAAATATATAT
TTTTAAAAAAAATATATATA
TTTAAAAAAAATATATATAG
TTAAAAAAAATATATATAGT

ACGTAAAACCCCGGGGTTTTATAT

ACGTAAAACCCCGGGGTTTTA
CGTAAAACCCCGGGGTTTTAT
GTAAAACCCCGGGGTTTTATA
TAAAACCCCGGGGTTTTATAT


TTTTTTTTAAAAAAAATATATATAGT

TTTTTTTTAAAAAAAATATAT
TTTTTTTAAAAAAAATATATA
TTTTTTAAAAAAAATATATAT
TTTTTAAAAAAAATATATATA
TTTTAAAAAAAATATATATAG
TTTAAAAAAAATATATATAGT
"""
