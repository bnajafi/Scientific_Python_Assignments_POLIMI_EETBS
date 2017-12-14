import pandas as pd
import matplotlib.pyplot as plt
#change the colors and fix the graph
#look on the table for U values 
#include ceiling and door on the function
labels = ["Walls","Roof","Door"]
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues = [547.5,514.6,43]
cols=["sandybrown","burlywood","coral"]
cols2=["cyan","greenyellow","magenta"]
#Pie chart Heating Load
plt.figure(1)
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title("Heating Load Values %")
plt.show(1)
#Pie chart Cooling Load
plt.figure(2)
plt.pie(CoolingLoadValues,labels=labels,colors=cols2,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title("Cooling Load Values %")
plt.show(2)

#Effect of U
def QFunction(U_wall):
    Area_walls=105.8
    Tout=-4.8
    Tin=20
    Delta_heating=Tin-Tout
    HF_walls=U_wall*Delta_heating
    Q_walls=HF_walls*Area_walls
    Q_door=92.5
    Q_roof=1240
    Q=Q_walls+Q_door+Q_roof
    return Q

U_values_wall=pd.Series([0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
Q_values=U_values_wall.apply(QFunction)

plt.figure(3)
plt.plot(U_values_wall,Q_values)
plt.scatter(U_values_wall,Q_values,marker="o",s=50)
plt.xlabel("U_values [W/m^2*K]")
plt.ylabel("Q_values [W]")
plt.title("Overall Q_values vs. U_values external wall")
plt.grid()
plt.show(3)




