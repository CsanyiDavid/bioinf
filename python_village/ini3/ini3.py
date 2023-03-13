f = open('rosalind_ini3.txt')

s = f.readline()
a, b, c, d = [int(i) for i in f.readline().split()]
f.close()

print(s[a:b+1], s[c:d+1])

