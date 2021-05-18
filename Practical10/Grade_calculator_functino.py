#Task_3
class grades:
    def __init__(self,name,code_portfolio,poster_presentation,final_exam):
        self.x = name
        self.y = code_portfolio
        self.z = poster_presentation
        self.w = final_exam
#input the inforation
S1=grades('CXX',90,88,68)
#calculate the grades
#An examole
final_grade1 = S1.y*0.4+S1.z*0.3+S1.w*0.3
#input
print('Here is a example：name is CXX，code_portfolio is 90，poster_presentation is 88 and final_exam is 68，Final grade of '+S1.x + ' is '+ str(final_grade1))
a=input('Please input the name :')
b=input('Please input the grade of code portfolil:')
c=input('Please input the grade of poster_presentation:')
d=input('Please input the grade of code final_exam:')
S2=grades(a,int(b),int(c),int(d))
final_grade2 = int(S2.y*0.4+S2.z*0.3+S2.w*0.3)
print('Final grade of '+S2.x + ' is '+ str(final_grade2))
