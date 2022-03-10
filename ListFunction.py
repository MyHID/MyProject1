l=[10,20,30,40,50]
print(l)
del l[1]  #it delete index value
print(l)

l.pop(2)
print(l)
print(l.pop(2)) #it delete index value and return value too

l.remove(30)  #works on value not on index
print(l)

l.clear()  #clear all value of list
print(l)

a=[100,200,300,400,500]
a[0]=90       #update a list
print(a)

a.insert(0,78)
a.insert(3,88)  #insert value in given index
print(a)

a.append(27)  #insert value at the end only
print(a)

a.append([56,76]) #insert a list at the end
print(a)

x=[10,20,50,30,80]
y=[78,90]
x.extend(y)  #insert only list value at the end not list itself as append does
print(x)


