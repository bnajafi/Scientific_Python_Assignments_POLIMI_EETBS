import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
HeatingLoad=[1149.2,1240,92.4]
CoolingLoad=[547.5,514.6,43.12]
label=["walls","ceiling","door"]
color=["red","black","yellow"]
plt.figure()

#total heating load
fig1=plt.pie(HeatingLoad,labels=label,colors=color,startangle=90,explode=(0.05,0.05,0.05)) 
plt.figure()

#total cooling load
fig2=plt.pie(CoolingLoad,labels=label,colors=color,startangle=90,explode=(0.05,0.05,0.05)) 
n=range(1,50)
n_vector=pd.Series(n)

def Ucalculator(n):
     U=n*0.03
     return U
     
Uvector=n_vector.apply(Ucalculator)
Qtotal=[]
Qwall=[]
A=105.8
T_heat=24.8

for U in Uvector:
     Q=A*U*T_heat
     Qwall.append(Q)
     Qtot=Q+1240+92.4
     Qtotal.append(Qtot)


plt.figure()
fig3=plt.plot(Uvector,Qtotal)
plt.show(fig3)
plt.xlabel("Uwall")
plt.ylabel("Q heating opaque")
plt.title("Qtotal=f(Uwall)")
