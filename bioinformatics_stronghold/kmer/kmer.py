from bioinf_utils import utils

dna_id, dna = utils.read_fasta_format_dnas_from_file(filename="rosalind_kmer.txt")

kmer_file = open("4mers.txt", 'r')
kmer_list = [i for i in kmer_file.read().split('\n') if i != '']
kmer_decomposition = {kmer : 0 for kmer in kmer_list}

for i in range(len(dna)-4+1):
    kmer_decomposition[dna[i:i+4]] += 1

f = open("output.txt", "w")
for kmer in kmer_list:
    f.write(str(kmer_decomposition[kmer]) + ' ')
f.close()