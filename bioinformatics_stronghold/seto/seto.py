#f = open("input.txt", 'r')
f = open("rosalind_seto.txt", 'r')
n = int(f.readline().rstrip('\n'))
A = {int(i) for i in f.readline().strip("\n{}").split(', ')}
B = {int(i) for i in f.readline().strip("\n{}").split(', ')}
U = set(range(1, n+1))
f.close()
f = open("output.txt", "w")


def write_set_to_file(file, s):
    file.write('{')
    file.write(', '.join([str(i) for i in s]))
    file.write('}\n')


write_set_to_file(f, A | B)
write_set_to_file(f, A & B)
write_set_to_file(f, A - B)
write_set_to_file(f, B - A)
write_set_to_file(f, U - A)
write_set_to_file(f, U - B)
