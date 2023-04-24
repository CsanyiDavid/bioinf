from bioinf_utils import utils

dna_dict = utils.read_fasta_format_dnas_from_file("rosalind_long.txt")
dnas = list(dna_dict.values())
n = len(dnas)
print(dnas)


def glue_read(read, s):
    half_len = len(read)//2
    for i in range(half_len, len(read)):
        if read[:i] == s[-i:]:
            return s + read[i:], True
    for i in range(half_len, len(read)):
        if read[-i:] == s[:i]:
            return read[:-i] + s, True
    return s, False



superstring = dnas[0]
dnas.remove(dnas[0])
while len(dnas) != 0:
    for i in range(len(dnas)):
        superstring, success = glue_read(dnas[i], superstring)

        if success:
            dnas.remove(dnas[i])
            break

print(superstring)