import random
#randint: return any random value b/w the range both inclusive
print(random.randint(2,10))
#randrange: return any random value b/w the range start inclusive(3), end not included(9)
print(random.randrange(3,9))
#choice:return any random number from list
l=[1,23,43,5,7,89,56,10,20,45]
t=(23,43,89,56,10,20,45)
print(random.choice(l))
print(random.choice(t))
#random:return any random float number b/w 0 and 1
print(random.random())
#shuffle:take a sequence and return sequence in random order
random.shuffle(l)
print(l)
#uniform:return any random float number b/w two parameters
print(random.uniform(3,9))
