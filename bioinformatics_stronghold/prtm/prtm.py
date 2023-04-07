from bioinf_utils import utils

mass_table = utils.read_monoisotopic_mass_table()

s = input()
weight = 0.0
for letter in s:
    weight += mass_table[letter]

print(weight)