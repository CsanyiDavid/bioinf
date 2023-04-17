import numpy as np
from bioinf_utils import utils

f = open("rosalind_prsm.txt")
n = int(f.readline().strip('\n'))
strings = []

for i in range(n):
    s = f.readline().strip('\n')
    strings.append(s)

R = [float(i) for i in f.read().split('\n') if i != '']
f.close()

mass_table = utils.read_monoisotopic_mass_table()
#print(mass_table)


def get_weight(s):
    weight = 0
    for letter in s:
        weight += mass_table[letter]
    return weight


def get_complete_spectrum(s):
    spectrum = []
    for i in range(1, len(s)):
        prefix_weight = get_weight(s[:i])
        suffix_weight = get_weight(s[i:])
        spectrum.append(prefix_weight)
        spectrum.append(suffix_weight)
    return spectrum


complete_spectrums = []
for s in strings:
    complete_spectrums.append(get_complete_spectrum(s))


def get_max_multiplicity_of_minkowski_difference(a, b):
    a_minus_b = {}
    max_key = None
    max_multiplicity = 0
    for x in a:
        for y in b:
            value = round(x-y, 5)
            if value in a_minus_b.keys():
                a_minus_b[value] += 1
            else:
                a_minus_b[value] = 1
            if a_minus_b[value] > max_multiplicity:
                max_multiplicity = a_minus_b[value]
                max_key = value
    return max_multiplicity, max_key


max_multiplicities = []
for i in range(len(strings)):
    max_multiplicity, _ = get_max_multiplicity_of_minkowski_difference(R, complete_spectrums[i])
    max_multiplicities.append(max_multiplicity)

print(max(max_multiplicities))
print(strings[np.argmax(max_multiplicities)])