import pandas as pd
import matplotlib.pyplot as plt
import pandas as np
items = [1,2,3]
labels = ["wall","ceiling","door"]
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues=[547.5,514.6,43]
cols=["r","b","g"]
plt.figure()
fig1=plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure()
fig2=plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
UWall=[0.4,0.43,0.438,0.44,0.46]
Qwall=[]
Qtot=[]

for U in UWall:
    DT=24.8
    A=105.8
    Qvalue=DT*A*U
    Qwall.append(Qvalue)
    QvalueTot=Qvalue+1240+92.5
    Qtot.append(QvalueTot)
print (Qtot)
print (Qwall)
plt.figure()
fig3=plt.plot(UWall,Qtot)
plt.xlabel("Uwall")
plt.ylabel("HeatingLoadValues")   
plt.show(fig3)