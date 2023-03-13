f = open('rosalind_ins.txt')
n = int(f.readline())
a = [int(i) for i in f.readline().split()]


def insertion_sort(a):
    n = len(a)
    swap_cnt = 0
    for i in range(1, n):
        k = i
        while k > 0 and a[k] < a[k-1]:
            a[k], a[k-1] = a[k-1], a[k]
            swap_cnt += 1
            k -= 1
    return swap_cnt


swap_cnt = insertion_sort(a)
print(a)
print(swap_cnt)