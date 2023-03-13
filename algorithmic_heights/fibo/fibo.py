i = int(input())

f = [0, 1]

while len(f)<i+1:
	f.append(f[-1]+f[-2])
	
print(f[i])
