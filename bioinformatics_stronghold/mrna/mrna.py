from bioinf_utils import utils


rna_codon_table = utils.read_codon_table('rna')
possible_codon_cnt = {}
for codon, amino_acid in rna_codon_table.items():
    if amino_acid in possible_codon_cnt.keys():
        possible_codon_cnt[amino_acid] += 1
    else:
        possible_codon_cnt[amino_acid] = 1

s = input()
possible_rna_cnt = 1
for i in s:
    possible_rna_cnt *= possible_codon_cnt[i]
    possible_rna_cnt %= 1000000

possible_rna_cnt *= possible_codon_cnt['Stop']
possible_rna_cnt %= 1000000

print(possible_rna_cnt)