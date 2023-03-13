k = int(input())  # homozygous dominant
m = int(input())  # heterozygous
n = int(input())  # homozygous recessive

population = k + m + n

hetero_homorec = 2 * (m/population) * (n/(population-1))
homorec = (n/population) * ((n-1)/(population-1))
hetero = (m/population) * ((m-1)/(population-1))
homodominant = (2 * (k/population) - (k/population)*((k-1)/(population-1)))
# print(hetero_homorec + homorec + hetero + homodominant)
assert abs(hetero_homorec + homorec + hetero + homodominant - 1) < 0.00001
# print(hetero_homorec * 0.5, homorec * 0, hetero * 0.75, homodominant * 1)
pr = hetero_homorec * 0.5 + homorec * 0 + hetero * 0.75 + homodominant * 1

print(pr)
