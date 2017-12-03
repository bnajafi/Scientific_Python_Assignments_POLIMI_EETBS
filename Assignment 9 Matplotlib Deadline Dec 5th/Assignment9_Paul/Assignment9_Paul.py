import pandas as pd,matplotlib.pyplot as plt
labels1,cols=["Wall","Roof","Door"],["r","g","b"]
HeatingLoadValues,CoolingLoadValues,U_previous=[1150,1240,92],[544,514,44],0.438
#Pie plots showing  share of each component in Heating Load & Cooling Load
plt.title("Opaque Heating Load Share")
plt.pie(HeatingLoadValues,labels=labels1,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
fig1=plt.figure()
plt.title("Opaque Cooling Load Share")
plt.pie(CoolingLoadValues,labels=labels1,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
#A 2D plot showing effect of changing U value of external wall to Opaque heating load
U_value_Series=pd.Series(range(30,60,5))*0.01               #Creating a range of U-Values from 0.3 to 0.6(step=0.05)
def percent_Change_Opaque_HeatingLoad(U_value_Series):      #A function to calculate % change in Opaque heating load as per U value of wall
    previous_heatingLoad=pd.Series(HeatingLoadValues).sum()
    new_heatingLoad=previous_heatingLoad*( U_value_Series/U_previous)       
    return (((new_heatingLoad-previous_heatingLoad)/previous_heatingLoad)*100)
percentChange_of_Opaque_HeaingLoadSeries=U_value_Series.apply(percent_Change_Opaque_HeatingLoad)
fig2=plt.figure()
plt.plot(U_value_Series,percentChange_of_Opaque_HeaingLoadSeries,'bo')
plt.xlabel("U-Value of External Wall(W/m^2K)")
plt.ylabel("Overall Opaque Heating Load Percentage Change")
plt.title("Effect of U-Value(External wall) on Opaque Heating Load(%Change)") 
plt.text(0.35,20,r'$U\_previous=0.438 W/m^2K$')



