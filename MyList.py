
#    0     1   2  3    4      5
l1=[10.2,20.5,30,40,"Hello","Namaste"]
#   -6    -5  -4 -3    -2       -1

for i in range(len(l1)):
     print(i," ",end="")  # to print index end="" for horizintal printing
     print(l1[i])

for a in l1:    # easy way to print list element
     print(a,"",end="")


for n in range(len(l1)-1,-1,-1):   #printing in reverse  start=5,end=-1,increment=-1
    print(l1[n])