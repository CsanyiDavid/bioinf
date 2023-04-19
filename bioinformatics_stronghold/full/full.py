from bioinf_utils import utils

mass_table = utils.read_monoisotopic_mass_table()

f = open("rosalind_full.txt")
l = [float(i) for i in f.read().split('\n') if i != '']
f.close()
l[1:] = sorted(l[1:])

s = ""

n = (len(l) - 1)//2 -1

prefix_weights = l[1:n+2]

i = 1
while i <= n:
    mass = prefix_weights[i] - prefix_weights[i - 1]
    amino_acid, dist = utils.get_nearest_amino_acid(mass)
    if dist < 0.0001:
        s += amino_acid
        i += 1
    else:
        prefix_weights[i] = l[0] - prefix_weights[i]
        prefix_weights.sort()

print(s)
print(len(s))