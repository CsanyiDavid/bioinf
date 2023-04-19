from bioinf_utils import utils

mass_table = utils.read_monoisotopic_mass_table()

f = open("rosalind_sgra.txt")
l = [float(i) for i in f.read().split('\n') if i != '']
f.close()
#  print(l)
l.sort()
n = len(l)

in_edge_list = [[] for i in range(n)]
for i in range(n):
    for other_node in range(i+1, n):
        mass = l[other_node]-l[i]
        amino_acid, dist = utils.get_nearest_amino_acid(mass)
        if dist < 0.001:
            in_edge_list[other_node].append([i, amino_acid])

#  print(in_edge_list)

prefix_longest_string = ['']
for i in range(1, n):
    s = ''
    for prev_node, amino_acid in in_edge_list[i]:
        new_string = prefix_longest_string[prev_node] + amino_acid
        if len(new_string) > len(s):
            s = new_string
    prefix_longest_string.append(s)

#  print(prefix_longest_string)
print(prefix_longest_string[-1])