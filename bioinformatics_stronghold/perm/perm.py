import math

f = open('output.txt', 'w')

n = int(input())

f.write(str(math.factorial(n))+'\n')


def print_permutations(s, l):
    if len(l) == 0:
        f.write(s+'\n')
    else:
        for i in l:
            print_permutations(s+i+' ', [x for x in l if x!=i])


print_permutations('', [str(i) for i in range(1, n+1)])
f.close()