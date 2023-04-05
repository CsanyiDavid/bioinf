n = int(input())
m = int(input())

rabbit_cnt = [0, 1]
mature_cnt = [1, 0]
new_cnt = [0, 1]

for i in range(n-1):
	new_rabbit_cnt = rabbit_cnt[-1] + mature_cnt[-1]
	new_mature_cnt = rabbit_cnt[-1]
	if len(rabbit_cnt)>=m+1:
		die_cnt = mature_cnt[-m-1]
	else:
		die_cnt = 0
	rabbit_cnt.append(new_rabbit_cnt-die_cnt)
	mature_cnt.append(new_mature_cnt-die_cnt)

print(mature_cnt)
print(rabbit_cnt)
