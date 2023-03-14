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


