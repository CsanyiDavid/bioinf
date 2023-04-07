from bioinf_utils import utils

mass_table = utils.read_monoisotopic_mass_table()

f = open("rosalind_spec.txt", 'r')
l = [float(i) for i in f.read().split('\n') if i != '']


def get_nearest_amino_acid(mass):
    nearest_amino_acid = None
    min_dist = 1000000
    for amino_acid in mass_table.keys():
        dist = abs(mass_table[amino_acid] - mass)
        #  print(amino_acid, dist)
        if dist < min_dist:
            min_dist = dist
            nearest_amino_acid = amino_acid
    return nearest_amino_acid


s = ""
for i in range(1,len(l)):
    mass = l[i] - l[i-1]
    s += get_nearest_amino_acid(mass)

print(s)