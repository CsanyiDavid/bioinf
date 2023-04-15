#f = open("input.txt", 'r')
f = open("rosalind_nwck.txt", 'r')
lines = [i.rstrip('\n') for i in f.readlines() if i != '\n']
f.close()
for k in range(len(lines)//2):
    nwck = lines[2 * k]
    x, y = lines[2 * k + 1].split()
    x_pos = nwck.find(x)
    y_pos = nwck.find(y)
    assert x_pos != -1
    assert y_pos != -1
    #  print(nwck, x, x_pos, y, y_pos)
    first_pos = min(x_pos, y_pos)
    second_pos = max(x_pos, y_pos)

    parenthesis_cnt = 0  # right_parenthesis_cnt - left_parenthesis_cnt
    max_parenthesis_cnt = 0
    last_parenthesis_pos = None
    for i in range(first_pos, second_pos):
        if nwck[i] == ')':
            parenthesis_cnt += 1
            last_parenthesis_pos = i
            if parenthesis_cnt > max_parenthesis_cnt:
                max_parenthesis_cnt = parenthesis_cnt
        elif nwck[i] == '(':
            parenthesis_cnt -= 1

    #print("parenthesis cnt: ", parenthesis_cnt)
    if parenthesis_cnt == max_parenthesis_cnt and nwck[second_pos-1] == ')':
        #  (dog, cow)cat;
        print(parenthesis_cnt, end=' ')
    else:
        print(max_parenthesis_cnt + (max_parenthesis_cnt - parenthesis_cnt) + 2, end=' ')
    #  print(first_pos, last_parenthesis_pos, second_pos)
