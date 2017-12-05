import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")


HeatingOpaqueLoadValues = [1149.2,1240,92.5]
CoolingOpaqueLoadValues = [547.5,541.6,43]
labels=['wall','roof','door']
plt.pie(HeatingOpaqueLoadValues,labels=labels,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure(2)
plt.pie(CoolingOpaqueLoadValues,labels=labels,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

import numpy as np
UH_series=np.arange(0.0, 1.0, 0.05)
UH=pd.Series(UH_series)

def function(x):
    y=(1149.2*x*0.438+1240+92.5)
    return y
    
y_series=UH.apply(function) #in this way u can do functions without vectorize ur array
plt.figure(3)
plt.plot(UH,y_series)
plt.show()
plt.xlabel("U value")
plt.ylabel("Wall heating value")
plt.title("Heating value wrt U value")
