f = open("input.txt", 'r')
abc = f.readline().split()
n = int(f.read())
f.close()

f = open("output.txt", 'w')


def print_string(abc, n, s):
    if len(s)==n:
        f.write(s + '\n')
    else:
        for letter in abc:
            print_string(abc, n, s+letter)


print_string(abc, n, "")
f.close()