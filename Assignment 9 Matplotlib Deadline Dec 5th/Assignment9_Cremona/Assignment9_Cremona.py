import pandas as pd
import matplotlib.pyplot as plt

labels = ["wall","ceiling","door"]
HeatingLoadValues = [1149.2,1240,92.5]
cols = ["r","b","g"]

plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')

labels = ["wall","ceiling","door"]
CoolingLoadValues = [547.5,514.6,43]
cols = ["r","b","g"]

plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')

# How the total heating load (opaque) changes by changing the U value of the walls

U_walls = [0.3,0.35,0.4,0.438,0.5,0.55,0.6,0.65,0.7]
Q_tot_heating_op = [2119.6,2250.8,2382,2483,2644.4,2775.6,2906.8,3038,3169.2]
plt.xlabel(" Heat transfer coefficient of the wall")
plt.ylabel(" Total heating load for opaque components")
plt.plot(U_walls,Q_tot_heating_op)
plt.scatter(U_walls,Q_tot_heating_op)