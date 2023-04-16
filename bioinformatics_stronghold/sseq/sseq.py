from bioinf_utils import utils

filename = "rosalind_sseq.txt"
dnas = utils.read_fasta_format_dnas_from_file(filename)

s = list(dnas.values())[0]
t = list(dnas.values())[1]
if len(s) < len(t):
    swap(s, t)

print(s, t)

index_in_t = 0
indices = []
for i in range(len(s)):
    if s[i] == t[index_in_t]:
        indices.append(i)
        index_in_t += 1
    if index_in_t == len(t):
        break

f = open("output.txt", 'w')
f.write(' '.join([str(i+1) for i in indices]))
f.close()