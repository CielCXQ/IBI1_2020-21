import os
import re
os.chdir("/Users/chenxuqi/IBI1_2020-21/Practical8")
pre_gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output = open('unknown_function.fa', 'w')
# define a new variable to calculate the line in part two
seq = ''
a = ''
protein = ''
b=''
name=''
sequence = ''
for line in pre_gene:
    if line.startswith('>'):
#seperate the two unknown and the known
        if 'unknown function'in line:
            number = 1
        else:
            number = 0
#the unknown function part
    if number == 1:
        if line.startswith('>'):
            b = len(seq)
            output.write('>' + f'{name:20}' + str(b) + '\n' + seq +'\n')
            name = ''
            name = re.findall('gene:(\S+)', line)[0]
            protein = ''
            b = ''
            seq = ''
        else:
            gene = line.replace('\n', '')
            seq = seq + gene
#add the last gene
output.write('>' + f'{name:20}' + str(len(seq)) + '\n' + seq +'\n')
pre_gene.close()
output.close()
#remove the first two lines
with open('unknown_function.fa', 'r') as fin:
    data = fin.read().splitlines(True)
with open('unknown_function.fa', 'w') as fout:
    fout.writelines(data[2:])