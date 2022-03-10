#Bar Plot
import matplotlib.pyplot as plt
import numpy as np
x=["Python","C++","Java","Pascal"]
y=[85,50,45,70]
z=[70,20,35,95]
width=0.2
p=np.arange((len(x)))
p1=[j+width for j in p]
plt.xlabel("Languages",fontsize=15)
plt.ylabel("Popularity",fontsize=15)
plt.title("Bar Chart",fontsize=20)
c=["r","y","g","b"]
b=["g","b","r","y"]
#plt.bar(x,y,width=0.4,color=c,align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.4,label="Namaste")
plt.bar(p,y,width,color=c,label="Namaste")
plt.bar(p1,z,width,color=b,label="Hello")
plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()