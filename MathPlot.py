import matplotlib.pyplot as plt
Day=[1,2,3,4,5,6,7]
Night=[2,4,5,3,5,6,9]
colors=["r","y","g","b","r","g","r"]
sizes=[50,60,40,55,200,90,70]
plt.scatter(Day,Night,c=colors,s=sizes)
#plt.scatter(Day,Night,c=colors,s=sizes,alpha=0.5,marker="*",edgecolors="g",linewidths=3)
plt.title("Scatter Plot",fontsize=15)
plt.xlabel("Day",fontsize=15)
plt.ylabel("Night",fontsize=15)
plt.show()
