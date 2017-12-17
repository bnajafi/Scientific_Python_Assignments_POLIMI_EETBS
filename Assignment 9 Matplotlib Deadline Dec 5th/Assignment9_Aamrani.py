mport pandas as pd
import matplotlib.pyplot as plt
 
items = [1,2,3]
labels = ["Wall","Roof","Door"]
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues = [547.5,514.6,43]
cols=["r","b","g"]
 
plt.figure()
fig1=plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title("Shares of opaque surfaces Heating Load Values")
plt.figure()
fig2=plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title("Shares of opaque surfaces Cooling Load Values")
 
 
U_values = pd.Series([0.3,0.35,0.4,0.438,0.45])
def Q_vs_U(U):
    A_walls=105.8
    DeltaT=24.8
    HF=U*DeltaT
    Q_walls=HF*A_walls
    Q_door=92.5
    Q_ceiling=1240
    Q=Q_walls+Q_door+Q_ceiling
    return Q
 
Q_values = U_values.apply(Q_vs_U)
 
plt.figure()
plt.plot(U_values,Q_values)
plt.ylabel("Overall Heating Load for Opaque Surfaces")
plt.xlabel("Heat Transfer Coefficient value(U) of the external wall")
plt.title("Overall Heating Load vs U of external wall")