f = open("rosalind_grph.txt")
lines = f.readlines()
f.close()
d = {}

rosalind_id = None
for line in lines:
    if line.startswith('>'):
        rosalind_id = line
        rosalind_id = rosalind_id.replace('>', '').replace('\n', '')
        d[rosalind_id] = ''
    else:
        d[rosalind_id] = d[rosalind_id] + line.replace('\n', '')

#print(d)
nodes = d.values()
arc_list = []


def is_arc(string_u, string_v, k):
    if string_u[-k:] == string_v[:k]:
        return True
    else:
        return False


for u in d.keys():
    for v in d.keys():
        if u != v:
            if is_arc(d[u], d[v], 3):
                arc_list.append([u, v])

f = open('output.txt', 'w')

for i in range(len(arc_list)):
    f.write(arc_list[i][0] + ' ' + arc_list[i][1] + '\n')

f.close()
