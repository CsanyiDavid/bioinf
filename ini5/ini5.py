f = open('rosalind_ini5.txt')

lines = f.readlines()
f.close()

out_file = open('out.txt', 'w')

for i in range(1, len(lines), 2):
    out_file.write(lines[i])

out_file.close()