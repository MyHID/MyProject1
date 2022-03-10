#Simple Function
def Myfun():
    print("Good Morning")

Myfun()

#Function with argument
def Myargument(a,b):
    c=a+b
    print(c)

Myargument(10,20)

#Function with default value
def Myargument(a,b=5):
    c=a+b
    print(c)

Myargument(10,50)
Myargument(10)

#Function with return value
def Myreturn(x,y):
    z=x+y
    return z

n1=int(input("Enter First Value="))
n2=int(input("Enter First Value="))
Output=Myreturn(n1,n2)
print("Return Value is=",Output)

#Function with multiple return value
def sqr(x):
    return x*x,x*2
s=sqr(5)
print(s)
