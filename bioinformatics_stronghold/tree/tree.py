f = open("rosalind_tree.txt", "r")

lines = temp = f.read().splitlines()

n = int(lines[0])
m = len(lines) - 1

print(n-1-m)