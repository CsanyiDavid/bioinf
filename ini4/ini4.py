f = open('rosalind_ini4.txt')

a, b = [int(i) for i in f.readline().split()]
f.close()

sum = 0
for i in range(a, b+1):
    if i%2==1:
        sum += i

print(sum)