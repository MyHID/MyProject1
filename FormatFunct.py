txt1="Welcome {} to {} Christian Eminet".format("Good", "Morning")
print(txt1)
txt2="Welcome {0} to {1} Christian Eminet".format("Good", "Morning")
print(txt2)
txt2="Welcome {1} to {0} Christian Eminet".format("Good", "Morning")
print(txt2)
txt3="Welcome {a} to {b} Christian Eminet".format(a=20,b=30)
print(txt3)
txt4="Welcome {a} to {b} Christian Eminet".format(a=20,b="Hi")
print(txt4)
txt5="Welcome {a:10} to {b} Christian Eminet".format(a=30,b=40)   #formatting with spacing
print(txt5)
txt6="Welcome {a:^10} to {b} Christian Eminet".format(a=30,b=40)  # central spacing
print(txt6)
txt7="Welcome {a:<10} to {b:>10} Christian Eminet".format(a=30,b=40) #left, right spacing
print(txt7)
txt8="Welcome {a:<10} to {b:^10} Christian{c:>10} Eminet".format(a=30,b=40, c=50) #left, right spacing
print(txt8)