s = input()

c = ''

complement = {
	'A' : 'T',
	'T' : 'A',
	'C' : 'G',
	'G' : 'C'
}

for i in range(len(s)-1, -1, -1):
	c += complement[s[i]]
	
print(c)
