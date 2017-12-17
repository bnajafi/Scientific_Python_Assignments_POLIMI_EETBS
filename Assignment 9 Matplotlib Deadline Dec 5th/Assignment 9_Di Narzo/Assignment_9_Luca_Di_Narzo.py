import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [1149,1240,93]
CoolingLoadValues = [548,514,43]
cols=["r","b","g"]

plt.close("all")
plt.figure(1)
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,autopct='%1.1f%%')
plt.title('Heating Load')

plt.figure(2)
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,autopct='%1.1f%%')
plt.title('Cooling Load')

Delta_T=24.8
Area=105.8
U_Wall=np.arange(0.0, 1.0, 0.1) #Range in witch U_value of wall changes,
x_series = pd.Series(U_Wall)
list_of_ones=[1]*len(x_series) #I'm creating a list of ones that has the same length of x_series
y_series=pd.Series(list_of_ones)
y=x_series*Delta_T*Area+(1240+93)*y_series

plt.figure(3)
plt.plot(x_series,y)
plt.xlabel('U_Wall')
plt.ylabel('Q_Heating')
plt.title('Effect of changing the U_Wall value')
plt.show()