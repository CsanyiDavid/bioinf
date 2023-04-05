f = open("input.txt", 'r')
abc = f.readline().split()
n = int(f.read())
f.close()

f = open("output.txt", 'w')


def print_string(abc, n, s):
    if len(s)>0:
        f.write(s + '\n')
    if len(s)<n:
        for letter in abc:
            print_string(abc, n, s+letter)


print_string(abc, n, "")
f.close()