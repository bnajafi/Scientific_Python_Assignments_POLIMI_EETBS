import pandas as pd
import matplotlib.pyplot as plt

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [1149.2,1240,92.5]
cols=["r","b","g"]
plt.figure()
graph = plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.show(graph)

items = [4,5,6]
labels = ["wall","roof","door"]
CoolingLoadValues = [547.5,514.6,43]
cols=["r","b","g"]
plt.figure()
graph = plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.show(graph)

#plt.close("all")
x = range(1,3)
x_series = pd.Series(x)

def Function(x):
    y = HeatingLoadValues[0]**x+HeatingLoadValues[1]+HeatingLoadValues[2]
    return y
    
y_series = x_series.apply(Function)
plt.plot(x_series,y_series)
plt.xlabel("Changing range of U_wall value")
plt.ylabel("New Heating Load of OpaqueSurface")
plt.title("Changing Effect by the variation of U on the Total Heating Load")
plt.show()