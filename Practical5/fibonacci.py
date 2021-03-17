#Fibonacci sequence
#define the first two
n1=1
n2=1
print("n1=",1)
print("n2=",1)
#how many times do we need to do: do the circle
for x in range(1,12):
  nth=n1+n2
#print nth
#next loop
  print("n",x+2,"=",nth)
  n1=n2 
  n2=nth 
