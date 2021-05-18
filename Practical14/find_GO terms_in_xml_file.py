from xml.dom.minidom import parse
import xml.dom.minidom
import os
import re
import matplotlib.pyplot as plt
os.chdir("/Users/chenxuqi/IBI1_2020-21/Practical14")
DOM = xml.dom.minidom.parse("go_obo.xml")
collection = DOM.documentElement
terms = collection.getElementsByTagName("term")
#ues the def to repeat four times
def count_number(y):
     id_DNA = []
     dict = {}
     for term in terms:
             is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
             all_id = term.getElementsByTagName("id")[0].childNodes[0].data
             #make a dictionary to show the relationship between is_a and id
             for x in is_a:
                 if not x in dict:
                     dict[x] = [all_id]
                 else:
                     dict[x].append(all_id)
     for term in terms:     #list:id_DNA/is_a_DNA
             defstr = term.getElementsByTagName('defstr')[0]
             if re.search(y,defstr.childNodes[0].data):  #to get the id related with y(DNA/RNA/protein/carbohydrate)
                 id = term.getElementsByTagName('id')[0]
                 id_DNA.append(id.childNodes[0].data)
#calculate the number of childNodes
     def getall(dict,lists):
         all = []
         for f in lists:
             if f in dict:
                 childNodes = dict[f]
                 all += childNodes
                 all += getall(dict,childNodes)  #recursive method
         return all
     all_childnodes = getall(dict,id_DNA)
     number = len(set(all_childnodes))
     return number
DNA = count_number('DNA')
print("The number of childNodes of DNA-associated terms is:",DNA)
RNA = count_number('RNA')
print("The number of childNodes of RNA-associated terms is:",RNA)
protein = count_number('protein|Protein')
print("The number of childNodes of protein-associated terms is:",protein)  # This word can be capitalized or not
carbohydrate = count_number('carbohydrate|Carbohydrate')
print("The number of childNodes of carbohydrate-associated i s:",carbohydrate)
#creat a pie chart to show it.
labels='DNA', 'RNA', 'Protein', 'Glycoprotein'
sizes=[DNA, RNA, protein, carbohydrate]
explode=(0, 0, 0.1, 0)
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.title(' the number of childNodes associated with DNA, RNA, protein and carbohydrate')
#according to the results, the most complex is protein
print('The most comlpex is protein')
plt.show()
