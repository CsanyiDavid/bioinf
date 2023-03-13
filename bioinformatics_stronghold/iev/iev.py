f = open("rosalind_iev.txt")
a = [int(i) for i in f.readline().split()]
f.close()

print(2*(a[0] + a[1] + a[2] + 0.75 * a[3] + 0.5 * a[4] + 0 * a[5]))
