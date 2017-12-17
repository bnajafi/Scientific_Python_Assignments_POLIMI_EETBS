import pandas as pd
import matplotlib.pyplot as plt
heatingLoadValues=[1149,1240,92.5]
coolingLoadValues=[547,514,43]
labels=["wall","roof","door"]
items=[1,2,3]
#plt.close("all")
cols=["r","b","g"]

fig1=plt.pie(heatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure()#plt.close("all")
fig2=plt.pie(coolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure()
#suppose current U value is 1.5 , we wanna find the effect of U in total load betweenU of  1 and 2
x=range(10,21)
x=pd.Series(x)
x=x/10
newWallHeat=[]
for i in x:
    print ("1")
    newWallHeat.append(1149*i/1.5)
totalHeat=[]
for i in newWallHeat:
    totalHeat.append(i+heatingLoadValues[1]+heatingLoadValues[2])
fig3=plt.plot(x,totalHeat)
plt.xlabel(" U wall")
plt.ylabel(" Total Heat Load")






