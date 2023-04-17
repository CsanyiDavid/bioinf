f = open("rosalind_conv.txt")
a = [float(i) for i in f.readline().strip('\n').split()]
b = [float(i) for i in f.readline().strip('\n').split()]
f.close()


def get_max_multiplicity_of_minkowski_difference(a, b):
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
    return max_multiplicity, max_key


max_multiplicity, max_key = get_max_multiplicity_of_minkowski_difference(a, b)
print(max_multiplicity)
print(abs(max_key))
