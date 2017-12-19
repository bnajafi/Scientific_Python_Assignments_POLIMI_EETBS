import pandas as pd
import matplotlib.pyplot as plt

heating_value=[1149.2,1240,92.5]
cooling_load_value=[547.5,514.6,43]
opaque_surface=["wall","ceiling","door"]
colors=["y","r","b"]

plt.figure()
plt.pie(heating_value,labels=opaque_surface, colors= colors, startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title("HeatingLoadValues")

plt.figure()
plt.pie(cooling_load_value,labels=opaque_surface, colors= colors, startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title("CoolingLoadValues")


U = pd.Series([0.3,0.35,0.4,0.438,0.45,0.5])
def HeatingLD(Uvalue):  
    Q_walls=Uvalue*24.8*105.8 
    Q_door=92.5
    Q_ceiling=1240
    Q_tot=Q_walls+Q_door+Q_ceiling
    return Q_tot
   #deltaT=24.8  A=105.8 
    
Q= U.apply(HeatingLD)

plt.figure()
fig3=plt.plot(U,Q)
plt.xlabel("Uwall")                      
plt.ylabel("Q_tot_opaque_surface")    
plt.title("Q_tot_wall(n)")             
    