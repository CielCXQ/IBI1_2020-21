#task 3
import os
import re
os.chdir("/Users/chenxuqi/IBI1_2020-21/Practical8")
input_name = input('Please input the filename: ')
DNA = open('unknown_function.fa', 'r')
output = open(input_name, 'w')
translation_table = {
    'ATA': 'J', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'B', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': 'O', 'TAG': 'U',
    'TGC': 'C', 'TGT': 'C', 'TGA': 'X', 'TGG': 'W',
}
protein = ''
for line in DNA:
    if line.startswith('>'):
        name = re.findall('>(\S+)', line)[0]
        line = next(DNA)
        #make them in one line and become string
        s = line.replace('\n','')
        #translate
        for i in range(0, len(s), 3):
            condon = s[0 + i:3 + i]
            protein += (translation_table[condon])
        output.write('>' + f'{name:20}' + str(len(protein)) + '\n' + protein + '\n' )
        protein = ''
DNA.close()
output.close()

