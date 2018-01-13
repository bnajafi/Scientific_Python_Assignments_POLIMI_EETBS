import pandas as pd
import matplotlib.pyplot as plt

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues=[547.5,514.6,43]
cols=["r","b","g"]

#Pie chart for heating loads
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

#Pie chart for cooling loads
plt.figure()
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')

#Defining a function which calculate Qtot while Uwall is varying
UWall = [0.35,0.40,0.42,0.45,0.47] #Arbitrary values of Uwall
Qwall = []
Qtot = []
Qroof = 1240
Qdoor = 92.5

for U in UWall:
    deltaT = 24.8
    A = 105.8
    Qvalue = deltaT*A*U
    Qwall.append(Qvalue)
    QTot = Qvalue+Qroof+Qdoor
    Qtot.append(QTot)
print Qtot
print Qwall

#Plotting how Heating Loads vary when Uwall varies
plt.figure()
fig3=plt.plot(UWall,Qtot)
plt.xlabel("Uwall")
plt.ylabel("HeatingLoadValues") 