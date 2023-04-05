f = open('rosalind_gc.txt')

lines = f.readlines()
lines = [line.strip('\n') for line in lines]
d = {}

for line in lines:
	if line.startswith('>'):
		d[line[1:]] = ''
		current_id = line[1:]
	else:
		d[current_id] += line
		
#print(d)
			
max_value = 0
max_index = -1

def gc_content(s):
	cnt = 0
	for i in s:
		if i in ['G', 'C']:
			cnt += 1
	#print(cnt, len(s), cnt/len(s))
	return cnt/len(s)


for k, v in d.items():
	current_gc_content = gc_content(v)
	if current_gc_content > max_value:
		max_value = current_gc_content
		max_id = k
		
print(max_id)
print(max_value*100)
