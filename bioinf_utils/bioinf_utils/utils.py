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


def stop_codons(dna_or_rna):
    codon_table = read_codon_table(dna_or_rna)
    stop_codons = []
    for codon in codon_table.keys():
        if codon_table[codon] == 'Stop':
            stop_codons.append(codon)
    return stop_codons


def translate_into_protein(s, dna_or_rna, stop=True):
    codon_table = read_codon_table(dna_or_rna)
    i = 0
    protein = ''
    while i < len(s) - 2:
        codon = s[i:i + 3]
        amino_acid = codon_table[codon]
        if amino_acid == 'Stop' and stop:
            break
        protein += amino_acid
        i += 3
    if protein.endswith('Stop'):
        protein = protein[:-4]
    return protein


def read_monoisotopic_mass_table():
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "monoisotopic_mass_table.txt"
    mass_table_path = os.path.join(directory, filename)
    mass_table_file = open(mass_table_path)
    mass_table_lines = mass_table_file.readlines()
    mass_table_file.close()
    mass_table = {}
    for line in mass_table_lines:
        letter, mass = line.split()
        mass = float(mass)
        mass_table[letter] = mass
    return mass_table


def get_nearest_amino_acid(mass):
    mass_table = read_monoisotopic_mass_table()
    nearest_amino_acid = None
    min_dist = 1000000
    for amino_acid in mass_table.keys():
        dist = abs(mass_table[amino_acid] - mass)
        #  print(amino_acid, dist)
        if dist < min_dist:
            min_dist = dist
            nearest_amino_acid = amino_acid
    return nearest_amino_acid, min_dist

