import matplotlib.pyplot as plt
slices=[21,78,20,35,55]
gas=["Oxigen","Nitrogen","Argan","Carban","Others"]
clr=["r","y","g","c","m"]
textp={"fontsize":10,"color":"blue"}
edge={"edgecolor":"black","linewidth":2}
plt.pie(slices,labels=gas,autopct='%1.2f%%',colors=clr, shadow=True,explode=(0,0,0,0,0.1),
        radius=1.4,startangle=270,textprops=textp,labeldistance=1.1,wedgeprops=edge,frame=True,rotatelabels=False)
plt.show()