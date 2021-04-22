#Task_2
#creat a class
class Student:
    def __init__(self, first_name, last_name, undergraduate_programme):
        self.x = first_name
        self.y = last_name
        self.z = undergraduate_programme
#An example
S1=Student('Xuqi','Chen','BMS')
#input data
print('Here is a example：The first name is Xuqi, last name is Chen and tbe undergraduate programmethe is BMS. Here is the result:'+S1.x + S1.y + ' is a ' + S1.z + ' student')
A = input('Please input the first name :')
B = input('Please input the last name :')
C = input('Please input the undergraduate programme :')
S2=Student(A,B,C)
print(S2.x + S2.y + ' is a ' + S2.z + ' student')
