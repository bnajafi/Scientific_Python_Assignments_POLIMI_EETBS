import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


U_wall_heat = 0.438
U_wall_heat_changed = np.arange(0.2,0.8,0.05)
A_wall = 105.8
DeltaT_heat = 24.8

q_heat_wall_changed = U_wall_heat_changed*A_wall*DeltaT_heat
q_heat_tot_changed = q_heat_wall_changed + 1240 + 92.5

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues = [547.5,514.4,43]
cols=["r","b","g"]

plt.figure(1)
plt.title("Heating Load")
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')
plt.show(1)
plt.figure(2)
plt.title("Cooling Load")
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')

plt.figure(3)
plt.title("Qtotal with different U (heating)")
plt.plot(U_wall_heat_changed,q_heat_tot_changed,color="g")
plt.xlabel("U_wall")
plt.ylabel("q_tot")