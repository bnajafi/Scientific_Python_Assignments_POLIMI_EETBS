import matplotlib.pyplot as plt
import pandas as pd

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [1149.2,1240,92.5]
cols=["r","b","g"]
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')


CoolingLoadValues = [547.5,514.6,43]
plt.close()
plt.figure()
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

plt.close("all")
x=range(0,2) #it's the ratio of Uwall,new to Uwall,previous - 0 is not realistic but i can't take a float number as start
x_ser = pd.Series(x)

Qwall = 1149.2
Qroof = 1240
Qdoor = 92.5
def QFunction(x):
    y=Qwall**x+Qroof+Qdoor
    return y

y_ser = x_ser.apply(QFunction)
plt.plot(x_ser,y_ser)
plt.xlabel(" Range of change in U value of the wall")
plt.ylabel(" New heating load of the opaque surface")
plt.title(" Effect of changing the U value of the wall on the total heating load")
