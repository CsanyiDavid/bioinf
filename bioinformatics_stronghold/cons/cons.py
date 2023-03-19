from bioinf_utils import utils

dnas = utils.read_fasta_format_dnas_from_file('rosalind_cons.txt')
n = len(list(dnas.values())[0])

#print(dnas)

nucleotides = ['A', 'C', 'G', 'T']

profile_matrix = {nucleotide: [0 for i in range(n)] for nucleotide in nucleotides}

for dna in dnas.values():
    for i in range(n):
        nucleotide = dna[i]
        profile_matrix[nucleotide][i] += 1

consensus_string = ''
for i in range(n):
    most_common_nucleotide = 'A'
    for nucleotide in nucleotides:
        if profile_matrix[nucleotide][i] > profile_matrix[most_common_nucleotide][i]:
            most_common_nucleotide = nucleotide
    consensus_string += most_common_nucleotide


def print_profile_matrix(profile_matrix):
    for nucleotide in nucleotides:
        print(nucleotide + ': ', end=' ')
        for i in profile_matrix[nucleotide]:
            print(i, end=' ')
        print()

print(consensus_string)
print_profile_matrix(profile_matrix)
