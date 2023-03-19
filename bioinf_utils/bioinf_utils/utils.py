import os


def read_rna_codon_table():
    directory = os.path.dirname(os.path.realpath(__file__))
    codon_table_path = os.path.join(directory, "rna_codon_table.txt")
    f = open(codon_table_path)
    text = f.read()
    f.close()
    l = text.split()
    rna_codon_table = {}
    for i in range(len(l) // 2):
        rna_codon_table[l[2 * i]] = l[2 * i + 1]
    return rna_codon_table


def read_fasta_format_dnas_from_file(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    dnas = {}

    rosalind_id = None
    for line in lines:
        if line.startswith('>'):
            rosalind_id = line
            rosalind_id = rosalind_id.replace('>', '').replace('\n', '')
            dnas[rosalind_id] = ''
        else:
            dnas[rosalind_id] = dnas[rosalind_id] + line.replace('\n', '')
    return dnas

