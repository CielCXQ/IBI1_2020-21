a=010502
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
print('d=',d)
print("e=",e)
if d < e :
  print "d smaller than e"
else:
  print "e smaller than d"

X=True 
Y=False
z=(X and not Y) or (Y and not X)
w=(X!=Y)
print("Z=",z,"W=Z is",w)

