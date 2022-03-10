import random
compnumber=random.randrange(1,101)
usernumber=int(input("Enter Your Number="))
if compnumber>usernumber:
    print("Computer Number=",compnumber)
    print("Computer Number is Too Big")
elif compnumber<usernumber:
    print("Computer Number=", compnumber)
    print("Computer Number is Too Small")
else:
    print("Computer Number=", compnumber)
    print("Both Numbers are Equal")