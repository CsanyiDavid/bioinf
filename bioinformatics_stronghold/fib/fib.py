n = int(input())
k = int(input())

l = [0, 1]

for i in range(n-1):
	l.append(l[-1]+k * l[-2])

print(l)
