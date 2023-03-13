mass_table_file = open("mass_table.txt")

mass_table_lines = mass_table_file.readlines()
mass_table_file.close()
mass_table = {}
for line in mass_table_lines:
    letter, mass = line.split()
    mass = float(mass)
    mass_table[letter] = mass

s = input()
weight = 0.0
for letter in s:
    weight += mass_table[letter]

print(weight)