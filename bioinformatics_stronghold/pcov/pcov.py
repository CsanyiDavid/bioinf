from bioinf_utils import utils

f = open("rosalind_pcov.txt")
s = [i for i in f.read().split('\n') if i != '']
n = len(s[0])

#  print(s)

superstring = s[0]
s.remove(s[0])
while len(s) > 0:
    for read in s:
        if read[:n-1] == superstring[-n+1:]:
            superstring += read[-1]
            s.remove(read)
            break
print(superstring[n-1:])
