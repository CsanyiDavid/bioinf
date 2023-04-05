f = open('rna_codon_table.txt')

text = f.read()
l = text.split()
d = {}
for i in range(len(l)//2):
	d[l[2* i]] = l[2*i+1]


rna = input()

protein = ''

print(len(rna), len(rna)//3)
for i in range(len(rna)//3):
	codon = rna[3*i:3*i+3]
	amino_acid = d[codon]
	if amino_acid == 'Stop':
		break
		c
	else:
		protein += amino_acid
print(len(protein))
print(protein)
