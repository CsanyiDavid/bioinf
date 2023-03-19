from bioinf_utils import utils

dna_id, dna = utils.read_fasta_format_dnas_from_file('rosalind_orf.txt')

codon_table = utils.read_codon_table('dna')

start_codon = 'ATG'
stop_codons = []
for codon in codon_table.keys():
    if codon_table[codon] == 'Stop':
        stop_codons.append(codon)


def open_reading_frames(dna):
    proteins = []
    for start_index in range(len(dna)-2):
        if dna[start_index:start_index+3] == start_codon:
            i=start_index
            protein = ''
            while i<len(dna)-2:
                codon = dna[i:i+3]
                if codon in stop_codons:
                    proteins.append(protein)
                    break
                else:
                    amino_acid = codon_table[codon]
                    protein += amino_acid
                    i += 3
    return proteins


proteins = open_reading_frames(dna)
reverse_complement_dna = utils.reverse_complement(dna)
proteins += open_reading_frames(reverse_complement_dna)

for protein in set(proteins):
    print(protein)
