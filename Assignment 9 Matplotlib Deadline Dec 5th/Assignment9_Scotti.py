import pandas as pd
import matplotlib.pyplot as plt

items = [1,2,3]
labels = ["Wall","Roof","Door"]
HeatLoadValues = [1149.2,1240,92.5]
cols = ["r","b","g"]

#This command makes a pie graph for heating & cooling load values for opaque surfaces and 
fig1=plt.pie(HeatLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title("Opaque surfaces Heating Load Values")

fig1=plt.pie(CoolLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title("Opaque surfaces Cooling Load Values")

#Here we define constants, and the differents U values as an array. in order to calcule the total Q we create a cycle for each value of U
A_walls=105.8
DeltaT=24.8
Q_door=92.5
Q_ceiling=1240
U_values = pd.Series([0.3,0.35,0.4,0.438,0.45])

def Q_vs_U(U):
    HF=U*DeltaT
    Q_walls=HF*A_walls
    Q=Q_Door+Q_ceiling+Q_walls
    return Q

Q_val=U_values.apply(Q_vs_U)

#Plot the graph
plt.figure()
plt.plot(U_values,Q_values)
plt.xlabel("Total Heat Load for opaque surfaces")
plt.ylabel("U of the external wall")
plt.title("Total heat load respect to U values")