import pandas as pd
import matplotlib.pyplot as plt

HeatingValues=[1149.2,1240,92.4]        
CoolingValues=[547.5,514.6,43.12]       
Label=["walls","ceiling","door"] 
Color=["red","blue","aqua"]

plt.figure()
plt.title(" Heating load opaque surfaces")
fig1=plt.pie(HeatingValues,labels=Label,colors=Color,startangle=90,explode=(0.01,0.01,0.01), autopct='%1.1f%%')
plt.figure()
plt.title(" Cooling load opaque surfaces")
fig2=plt.pie(CoolingValues,labels=Label,colors=Color,startangle=90,explode=(0.01,0.01,0.01), autopct='%1.1f%%')



n=range(1,100)
n_values=pd.Series(n)

def Function_U_calculation(n):
    U=n*0.438
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
plt.xlabel("Uwall (0.025*n) ")                  
plt.ylabel("Q_tot_heating_opaque_surphace (W) ")
plt.title("Q_tot function of Uwall(n)")             
    
    
    