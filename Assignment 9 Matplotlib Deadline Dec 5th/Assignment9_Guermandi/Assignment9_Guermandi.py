import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

areas = [105.8,2.2,200]
seriearea = pd.Series(areas)
Uwinter=[0.4385,1.694,0.25]
Usummer=[0.435,1.655,0.25]
alfaroof=0.85
OFt=np.array([1,1,0.62])
OFb=np.array([8.2,8.2,14.3*alfaroof-4.5])
OFr=np.array([-0.36,-0.36,-0.19])
quandofafreddo=20-(-4.8)
quandofacaldo=31.9-24
DR=11.9
quantosidisperde=pd.Series(Uwinter)
quantarobaentra=pd.Series(Usummer)
HF=quandofafreddo*quantosidisperde
heatingLoad = HF*seriearea
labels = ["wall","door","ceiling"]
colors=["r","g","b"]
plt.figure(1)
plt.pie(heatingLoad,labels=labels,colors=colors,explode=(0.1,0.1,0.1),autopct='%1.1f%%', startangle=90)
plt.title("How much heat is being desperded from each opaque component?")
plt.show()
malloppo=OFt*quandofacaldo+OFb+OFr*DR
inestate=pd.Series(malloppo)
CF=inestate*quantarobaentra
coolingLoad=CF*seriearea
plt.figure(2)
plt.pie(coolingLoad,labels=labels,colors=colors,explode=(0.1,0.1,0.1),autopct='%1.1f%%', startangle=90)
plt.title("Share of each opaque component in the total cooling load")
plt.show()

#if I change Uwall
Unew=[0.28,1.694,0.25]
U=[0.435,0.28]
items=[1,2]
Unew=pd.Series(Unew)
HFnew=quandofafreddo*Unew
heatingLoadnew = HFnew*seriearea
heatingLoadValues=pd.Series([heatingLoad.sum(),heatingLoadnew.sum()])
plt.figure(3)
plt.bar(items,heatingLoadValues,color="b")
plt.title("U_wall=0.435                          U_wall=0.28")
