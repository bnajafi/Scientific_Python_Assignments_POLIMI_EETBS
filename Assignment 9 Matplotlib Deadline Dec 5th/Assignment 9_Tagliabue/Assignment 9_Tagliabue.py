import pandas as pd
import matplotlib.pyplot as plt
import pandas as np
deltaTheating=24.8
deltaTcooling=7.9
A=105.8
items = [1,2,3]
labels = ["wall","ceiling","door"]
HeatingLoadValues = [1150,1240,92.5]
CoolingLoadValues=[547,514,44]
cols=["r","b","g"]
plt.close("all")
plt.figure()
fig1=plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure()
fig2=plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
Uwall=[0.10,0.12,0.14,0.145,0.15]
Qwallheating=[]
Qopqheating=[]
for u in Uwall:
    Q=deltaTheating*A*u
    Qwallheating.append(Q)
    Qtot=HeatingLoadValues[1]+HeatingLoadValues[2]+Q
    Qopqheating.append(Q)
    Q=deltaTcooling*A*u
print (Qwallheating)
print (Qopqheating)
plt.figure()
fig3=plt.plot(Uwall,Qopqheating)
plt.xlabel("Uwall")
plt.ylabel("HeatingLoadValues")   
plt.show()

