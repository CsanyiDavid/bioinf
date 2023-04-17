f = open("rosalind_conv.txt")
a = [float(i) for i in f.readline().strip('\n').split()]
b = [float(i) for i in f.readline().strip('\n').split()]

a_minus_b = {}
max_key = None
max_multiplicity = 0
for x in a:
    for y in b:
        value = round(x-y, 5)
        if value in a_minus_b.keys():
            a_minus_b[value] += 1
        else:
            a_minus_b[value] = 1
        if a_minus_b[value] > max_multiplicity:
            max_multiplicity = a_minus_b[value]
            max_key = value

print(max_multiplicity)
print(abs(max_key))