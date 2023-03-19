import os


def read_codon_table(dna_or_rna):
    if dna_or_rna=='rna':
        filename = "rna_codon_table.txt"
    elif dna_or_rna=='dna':
        filename = "dna_codon_table.txt"
    else:
        raise Exception('Invalid dna_or_rna!')
    directory = os.path.dirname(os.path.realpath(__file__))
    codon_table_path = os.path.join(directory, filename)
    f = open(codon_table_path)
    text = f.read()
    f.close()
    l = text.split()
    rna_codon_table = {}
    for i in range(len(l) // 2):
        rna_codon_table[l[2 * i]] = l[2 * i + 1]
    return rna_codon_table


def read_fasta_format_dnas_from_file(filename='input.txt'):
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
    if len(list(dnas.keys()))==1:
        dna_id = list(dnas.keys())[0]
        dna = list(dnas.values())[0]
        return dna_id, dna
    else:
        return dnas


def reverse_complement(dna):
    complement_dna = ''
    complement_nucleotide = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    for i in range(len(dna)-1, -1, -1):
        nucleotide = dna[i]
        complement_dna += complement_nucleotide[nucleotide]
    return complement_dna


