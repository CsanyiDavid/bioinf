import scipy


k = int(input())
n = int(input())

size = 2**k  # size of the k-th generation
# Every individual has Aa Ba genotype with p=0.25 probability (except Tom)

solution = 0

for i in range(n, size+1):
    # probability of exactly i individual with genotype Aa Bb:
    p = scipy.special.binom(size, i) * (0.25**i) * (0.75 ** (size-i))
    solution += p

print(solution)