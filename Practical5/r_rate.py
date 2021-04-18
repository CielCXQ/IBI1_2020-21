#define the  start number
n=84
r=1.2
# round  five time
for x in range(0,5):
  n=n*r+n

print("When the r rate is " + str(r) + ", the totol number of individuals infected after 5 generations is " + str(int(n)))
