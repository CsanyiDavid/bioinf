s = input()
t = input()

indices = []
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        indices.append(i+1)
        print(i+1, end=" ")
