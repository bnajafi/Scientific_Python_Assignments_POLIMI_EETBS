#ASSIGNMENT 9

import pandas as pd
import matplotlib.pyplot as plt

H_L_Values=[1149.2,1240,92.4]        #heating load
C_L_Values=[547.5,514.6,43.12]       #cooling load
Label=["walls","ceilings","door"] 
Color=["red","blue","aqua"]

plt.figure()
fig1=plt.pie(H_L_Values,labels=Label,colors=Color,startangle=90,explode=(0.01,0,0))     #pie graph
plt.title("Total heating load values")

plt.figure()
fig2=plt.pie(C_L_Values,labels=Label,colors=Color,startangle=90,explode=(0.01,0,0))     #pie graph
plt.title("Total cooling load values")

n=range(1,80)
n_values=pd.Series(n)
Uwall_winter=0.438
def Function_U_calculation(n):
    U=n*Uwall_winter
    return U
    
U_values=n_values.apply(Function_U_calculation)
DT_heating=24.8
A=105.8
Q_ceil=1240
Q_door=92.4 
Q_wall=[]
Q_tot=[]   

for U in U_values:
    Q=A*U*DT_heating
    Q_wall.append(Q)
    Qtot=Q+Q_ceil+Q_door
    Q_tot.append(Qtot)
    
print Q_wall
print Q_tot

plt.figure()
fig3=plt.plot(U_values,Q_tot)
plt.xlabel("Uwall (0.025*n) ")                      #name on X axis
plt.ylabel("Q_tot_heating_opaque_surphace (W) ")    #name on Y axis
plt.title("Q_tot function of Uwall(n)")             #title of the plot
    
    
    