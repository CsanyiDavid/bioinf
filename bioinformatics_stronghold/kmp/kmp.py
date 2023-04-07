#  KMP preprocess
from bioinf_utils import utils


filename = "rosalind_kmp.txt"
dna_id, s = utils.read_fasta_format_dnas_from_file(filename)


def kmp_preprocess(s):
    m = len(s)
    k = 0
    p = [0]
    for i in range(1, m):
        while k > 0 and s[i] != s[k]:
            k = p[k-1]
        if s[k] == s[i]:
            k += 1
        p.append(k)  # p[i]=k
    return p


p = kmp_preprocess(s)
f = open("output.txt", 'w')
for i in p:
    f.write(str(i) + ' ')
f.close()