import pandas as pd
import matplotlib.pyplot as plt

plt.figure()
labels = ["wall","roof","door"]
Heating_load = [1149.2,1240,92.5]
color=["red","blue","aqua"]
fig1=plt.pie(Heating_load,labels=labels,colors=color,startangle=90, autopct='%1.1f%%')
plt.title("Heating load percentages")

plt.figure()
Cooling_load = [547.5,514.6,43]
color2=["violet","blue","yellow"]
fig2=plt.pie(Cooling_load,labels=labels,colors=color2,startangle=90, autopct='%1.1f%%')
plt.title("Cooling load percentages")

n=range(1,50)
n_values=pd.Series(n)
def U_calculation(n):
    U=n*0.438
    return U
    
U_values=n_values.apply(U_calculation)
T_heat=24.8
Area_wall=105.8
Q_roof=1240
Q_door=92.4 
Q_wall=[]
Q_tot=[]   

for U in U_values:
    Q=Area_wall*U*T_heat
    Q_wall.append(Q)
    Qtot=Q+Q_roof+Q_door
    Q_tot.append(Qtot)
    
print Q_wall
print Q_tot

plt.figure()
fig3=plt.plot(U_values,Q_tot)
plt.xlabel("Uwall [W/m^2 K")                      
plt.ylabel("Q_tot_heat_opq [W/m^2]")    
plt.title("Q_tot_heat_opq=f(U_wall)")             
    