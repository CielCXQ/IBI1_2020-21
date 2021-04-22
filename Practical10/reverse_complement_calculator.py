#Task 1
def task_1(DNA):
#A dictiory
    complementary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G','a':'t','t':'a','g':'c','c':'g'}
    letters = list(DNA)
#convert it to the reverse complement
    letters = [complementary[base] for base in letters]
#reverse its order
    list.reverse(letters)
#change the list to string
    return print("".join(letters))
#input DNA
print('If I input the DNA: ATCGGTCAAGTCatcgcgta, the result is shown:')
task_1('ATCGGTCAAGTCatcgcgta')
DNA2=input('please input the DNA:')
task_1(str(DNA2))
