import math

f = open("input.txt", 'r')
s = f.readline().rstrip('\n')
a = [float(i) for i in f.readline().split()]
f.close()

for gc_content in a:
    log_p = {
        'G' : math.log10(gc_content/2),
        'C' : math.log10(gc_content/2),
        'A' : math.log10((1-gc_content)/2),
        'T' : math.log10((1-gc_content)/2)
    }
    log_prob = 0
    for letter in s:
        log_prob += log_p[letter]
    print(log_prob)