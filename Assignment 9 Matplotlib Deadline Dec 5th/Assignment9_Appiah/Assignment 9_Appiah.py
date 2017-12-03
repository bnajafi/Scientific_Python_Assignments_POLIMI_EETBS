import pandas as pd
import matplotlib.pyplot as plt

Qheating=[1149.2,1240,92.5]
Qcooling=[547.5,514.6,43]
labels=['walls','roof','door']
cols=["r","b","g"]

#plotting total heating load 
fig1=plt.figure()
plt.pie(Qheating,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.legend()
plt.title("Share of each component in the total heating load (opaque)")

#plotting share of cooling load
fig2=plt.figure()
plt.pie(Qcooling,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.legend()
plt.title("Share of each component in the total Cooling load (opaque)")

# Effect of changing U_value of external wall to Opaque heating load
U_wall_old = 0.438
x=range(20,50,5)
U_new_Series=pd.Series(x)*0.01
#Defining a function to calculate Opaque heating load per change in U value of external wall
def Opaque_Qheating(U_new_Series):                         
    Qheating_wall_new =Qheating[0]*(U_new_Series/U_wall_old) 
    Overall_Qheating= Qheating_wall_new+Qheating[1]+Qheating[2] 
    return Overall_Qheating   
Qheating_Series=U_new_Series.apply(Opaque_Qheating)

# 2D plot Overall Qheating vs U value of external wall
fig3=plt.figure()
plt.plot(U_new_Series,Qheating_Series)
plt.xlabel("U_Value of External Wall")
plt.ylabel("Overall Q_Heating Load")
plt.title("Effect of changing U_Value of External wall on Opaque Heating Load")   