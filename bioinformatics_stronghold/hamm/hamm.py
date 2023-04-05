s = input()
t = input()

dist = 0
for i in range(len(s)):
	if s[i] != t[i]:
		dist +=1 
print(dist)
