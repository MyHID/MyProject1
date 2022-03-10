import math
#ceil will show next integer value
x1=11.2
y1=11.5
z1=11.8
print(math.ceil(x1),math.ceil(y1),math.ceil(z1))
#fabs will show absolute value
x2=10
y2=-10
print(math.fabs(x2),math.fabs(y2))
#factorial function,if number is negative or real it will raise error
x3=5
print(math.factorial(x3))
#floor will show back integer value, opposite of ceil
x4=11.2
y4=11.5
z4=11.8
print(math.floor(x4),math.floor(y4),math.floor(z4))
#fsum function returns an accurate floating point sum of values in the iterables
l=[10,20,30,40,50]
t=(10,20,30,40,50)
print(math.fsum(l))
print(math.fsum(t))
#sqrt: Negative value give error
print(math.sqrt(16))
print(math.sqrt(5))
#it will show integer squareroot
print(math.isqrt(16))
#pow to find power
print(math.pow(2,6))