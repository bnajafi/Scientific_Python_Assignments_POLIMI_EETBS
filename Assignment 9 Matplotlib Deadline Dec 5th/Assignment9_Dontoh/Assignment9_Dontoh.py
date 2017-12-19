import pandas as pd
import matplotlib.pyplot as plt

labels=["Wall","Roof","Door"]
cols=["y","g","r"]
HeatingLoadValues=[1149,1240,92]
CoolingLoadValues=[548,514,43]


#Pie chart representation of each component for Heating Load
plt.title("Opaque_Heating_Load")
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')

#Pie chart representation of each component for Cooling Load
figure=plt.figure()
plt.title("Opaque_Cooling_Load_Share")
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')

#2D plots showing change of U value of external wall to Opaque heating load
Uvalue_Series=pd.Series(range(30,50,5))*0.01   #assuming U values,ranging from 30 to 50 with step functions as 5
def OpaqueHeatingLoad(Uvalue_Series):  
    wall_HeatingLoad=Uvalue_Series*24.8*105.8  #deltaT_Heating=24.8; Wall_Area=105.8.
    return (wall_HeatingLoad+HeatingLoadValues[1]+HeatingLoadValues[2])
    
OpaqueheatingLoadSeries=Uvalue_Series.apply(OpaqueHeatingLoad)
figure1=plt.figure()
plt.plot(Uvalue_Series,OpaqueheatingLoadSeries)
plt.xlabel("U-Value of External Wall")
plt.ylabel("Overall Opaque Heating Load")
plt.title("Effect of the U-Value on Opaque Heating Load")

