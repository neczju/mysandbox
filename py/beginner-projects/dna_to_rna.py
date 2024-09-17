dna = 'AATG'
dna_list = list(dna)
print(dna_list)
rna = ''
for i in range(len(dna_list)):
    if dna_list[i] == 'T':
        del dna_list[i]
        dna_list.insert(i, 'U')
    rna += dna_list[i]
print(rna)
