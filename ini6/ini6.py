f = open('rosalind_ini6.txt')

words = f.read().split()
f.close()

d = {}

for word in words:
    if word in d.keys():
        d[word]+=1
    else:
        d[word]=1

f = open('out.txt', 'w')
for k, v in d.items():
    f.write(k + ' ' + str(v) +'\n')

f.close()