#Assignment 9 - Riccardi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Walls=[105.8,0.458,24.8,0,547.5]
Door=[2.2,1.694,24.8,0,43]
Roof=[200,0.25,24.8,0,514.6]
Surfaces_names = ["Walls","Door","Roof"]
Columns_names=["Area","Ufactor","DeltaT_Heating","HeatingLoad","CoolingLoad"]
Surfaces_DF=pd.DataFrame([Walls,Door,Roof],index=Surfaces_names,columns=Columns_names)
Surfaces_DF["HeatingLoad"]=Surfaces_DF["Area"]*Surfaces_DF["Ufactor"]*Surfaces_DF["DeltaT_Heating"]

#pie chart for heating loads
plt.figure("Pie chart for heating loads")
plt.pie(Surfaces_DF["HeatingLoad"],labels=Surfaces_names,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')

#pie chart for cooling loads
plt.figure("Pie chart for cooling loads")
plt.pie(Surfaces_DF["CoolingLoad"],labels=Surfaces_names,startangle=90,explode=(0.1,0.1,0.1), autopct='%1.1f%%')

#How does the total heating load change if I change the values of U-factors for the walls?
def NewHeatingLoads_Finder(OldHeatingLoads,NewUfactors,OldUfactor):
    NewHeatingL=OldHeatingLoads/OldUfactor*NewUfactors
    return NewHeatingL

NewUfactors=np.array([0.2,0.3,0.4,0.5,0.6,0.7,0.8])
NewHeatingLoadsWalls=NewHeatingLoads_Finder(Surfaces_DF["HeatingLoad"]["Walls"],NewUfactors,Surfaces_DF["Ufactor"]["Walls"])

NewHeatingLoadsOpaque=[]
for load in NewHeatingLoadsWalls:
    NewHeatingLoadsOpaque=np.append(NewHeatingLoadsOpaque,Surfaces_DF["HeatingLoad"]["Roof"]+Surfaces_DF["HeatingLoad"]["Door"]+load)
    
plt.figure("Variation of total heating load in function of U") 
plt.plot(NewUfactors,NewHeatingLoadsOpaque)




