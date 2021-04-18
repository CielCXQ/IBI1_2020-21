#input the three numbers
a=010502
b=190784
c=100321
#calculate the d and e 
d=abs(a-c)
e=abs(a-b)
print('d=',d)
print("e=",e)
#compare
if d < e :
  print("d smaller than e")
else:
  print("e smaller than d")

#input 
X=True 
Y=False
#define the z and w
z=(X and not Y) or (Y and not X)
w=(X!=Y)
#show 
print("Z=",z,"W=Z is",w)

