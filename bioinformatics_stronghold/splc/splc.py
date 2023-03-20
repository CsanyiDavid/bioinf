from bioinf_utils import utils

filename = 'rosalind_splc.txt'
f = open(filename)
s_id = f.readline().replace('>', '').replace('\n', '')
f.close()

substrings = utils.read_fasta_format_dnas_from_file(filename)
s = substrings[s_id]
substrings.pop(s_id)

i = 0
while i<len(s):
    for substring in substrings.values():
        if s[i:i+len(substring)] == substring:
            s = s[:i] + s[i+len(substring):]
            break
    i+=1


protein = utils.translate_into_protein(s, 'dna')
print(protein)