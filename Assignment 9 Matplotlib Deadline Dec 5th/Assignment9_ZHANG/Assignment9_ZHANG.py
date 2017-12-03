import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [1149.2,1240,92.4]
CoolingLoadValues = [547.5,514.6,43]
cols=["r","b","g"]
# 1
plt.figure()
fig1=plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
# 2
plt.figure()
fig2=plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
# 3
Uwall_value = np.arange(0.4,0.5,0.01)
Dt = 24.8
A = 105.8
Qwall = Dt*A*Uwall_value   
Qtot = Qwall +1240+92.4
plt.figure()
fig3 = plt.plot(Uwall_value,Qtot)
plt.xlabel(" Uwall_")
plt.ylabel("  heating load ")
plt.title(" effect of changing the U ")


