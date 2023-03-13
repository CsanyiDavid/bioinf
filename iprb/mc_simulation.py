import random

k = int(input())  # homozygous dominant
m = int(input())  # heterozygous
n = int(input())  # homozygous recessive

population = k + m + n


def generate_random_individual_alleles():
    r1 = random.randint(1, population)
    r2 = random.randint(1, population-1)
    if r1 <= r2:
        r2 += 1

    if r1 <= k:
        alleles1 = "AA"
    elif r1 <= k+m:
        alleles1 = "Aa"
    elif r1 <= k+m+n:
        alleles1 = "aa"

    if r2 <= k:
        alleles2 = "AA"
    elif r2 <= k+m:
        alleles2 = "Aa"
    elif r2 <= k+m+n:
        alleles2 = "aa"
    return alleles1, alleles2


dominant_allele_cnt = 0
test_cnt = 100000

for i in range(test_cnt):
    first_individual_alleles, second_individual_alleles = generate_random_individual_alleles()
    first_inherited_allele_index = random.randint(0, 1)
    second_inherited_allele_index = random.randint(0, 1)
    offspring_alleles = first_individual_alleles[first_inherited_allele_index] \
                        + second_individual_alleles[second_inherited_allele_index]
    if offspring_alleles[0] == 'A' or offspring_alleles[1] == 'A':
        dominant_allele_cnt += 1

print(dominant_allele_cnt/test_cnt)
