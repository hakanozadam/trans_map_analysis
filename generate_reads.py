#from io.Fastq import FastqFile

#from io.generate_fastq import deneme
from genomic_io import generate_fastq
import gzip
import sys

MIN_LEN = 15
MAX_LEN = 40

def main():
    if len(sys.argv) < 3:
        print("Usage: \npython /path/to/script input_fasta output_fastq")
        exit(1)

    print(" ".join(sys.argv))


    generate_fastq.generate_reads(fasta_file = sys.argv[1],
                   length_min = MIN_LEN,
                   length_max = MAX_LEN,
                   output_file = sys.argv[2])




if __name__ == "__main__":
    main()
