import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

items=[1,2,3]
labels=["walls", "ceilings" , "door"]
HeatingLoadValues=[1149.2,1240,92.5]
CoolingLoadValues=(547.5,514.6,43)
cols=['r','b','g']
plt.figure()
plt.pie(HeatingLoadValues,labels=labels, colors= cols, startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title("HeatingLoadValues")

plt.figure()
plt.pie(CoolingLoadValues,labels=labels, colors= cols, startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title("CoolingLoadValues")

#####################################

U_values = pd.Series([0.3,0.35,0.4,0.438,0.45,0.5])
def HeatingLoad(Uvalue):  
    Q_walls=Uvalue*24.8*105.8 ###A_walls=105.8, DeltaT=24.8
    Q_door=92.5
    Q_ceiling=1240
    Q_total=Q_walls+Q_door+Q_ceiling
    return Q_total
    
    
Q_values = U_values.apply(HeatingLoad)

plt.figure()
plt.plot(U_values,Q_values)
plt.xlabel("Overall Heating Load")
plt.ylabel("Heat Transfer Coefficient value of the external wall")
plt.title("Overall Heating Load vs U of external wall")
