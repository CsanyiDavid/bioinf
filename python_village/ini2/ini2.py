f = open('rosalind_ini2.txt')

a, b = f.read().split()
a, b = int(a), int(b)
f.close()

print(a**2 + b**2)