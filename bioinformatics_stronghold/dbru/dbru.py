from bioinf_utils import utils

f = open("rosalind_dbru.txt")
s = [i for i in f.read().split('\n') if i!='']
n = len(s[0])
rcs = [utils.reverse_complement(v) for v in s]

edges = list(set(s + rcs))
print(edges)
f = open("output.txt", 'w')
for edge in edges:
    u = edge[:n-1]
    v = edge[1:]
    f.write(f"({u}, {v})\n")
f.close()
