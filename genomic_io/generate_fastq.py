from . import Fastq, Fasta
import gzip
import sys

MIN_LEN = 15
MAX_LEN = 16




def generate_transcript_reads(header, transcript_sequence, this_length, file_handle):
    current_pos = 0
    t_len       = len(transcript_sequence)
    result      = []
    quality_str = "I" * this_length

    while current_pos + this_length <= t_len:

        this_entry   = "\n".join( ["@{}__{}__{}".format(header, current_pos, this_length),
                                      transcript_sequence[current_pos : current_pos + this_length],
                                      "+",
                                      quality_str]
                                    )
        print(this_entry, file = file_handle)
        current_pos += 1


def generate_reads(fasta_file, length_min, length_max, output_file):

    if output_file[-2:].lower() == "gz":
        file_handle = gzip.open(output_file, "wt")
    else:
        file_handle = open(output_file, "wt")

    for current_length in range(length_min, length_max + 1):
        input_fasta = Fasta.FastaFile(fasta_file)
        for entry in input_fasta:
            generate_transcript_reads(
                header              = entry.header,
                transcript_sequence = entry.sequence,
                this_length         = current_length,
                file_handle         = file_handle )

    file_handle.close()


def main():
    if len(sys.argv) < 3:
        print("Usage: \npython /path/to/script input_fasta output_fastq")
        exit(1)

    print(" ".join(sys.argv))

    """
    generate_reads(fasta_file = sys.argv[1],
                   length_min = MIN_LEN,
                   length_max = MAX_LEN,
                   output_file = sys.argv[2])
    """



if __name__ == "__main__":
    main()
