# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Considering RLF example I

#Heating load pie chart

items1 = [1,2,3]
labels1 = ["wall","roof","door"]
Heating_load_opaque = [1149.2,1240,92.5]
cols1=["r","b","g"]
plt.figure()
plt.title(" Heating load opaque surfaces")
fig1=plt.pie(Heating_load_opaque,labels=labels1,colors=cols1,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure(1)

#Cooling load pie chart

items2 = [4,5,6]
labels2 = ["wall","roof","door"]
Cooling_load_opaque = [547.5,514.6,43]
cols2=["r","b","g"]
plt.figure()
plt.title(" Cooling load opaque surfaces")
fig2=plt.pie(Cooling_load_opaque,labels=labels2,colors=cols2,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure(2)

# U vs Heating load opaque plot

x=np.arange(0,1,0.001) # range of U values, I use a numpy command to create a range of float elements

x_series = pd.Series(x)
Overall_heating_load_opaque=sum(Heating_load_opaque)#overall heating load of the opaque surfaces 
heating_load_door_roof = Overall_heating_load_opaque-1149.2 #heating load of the opaque surfaces without the heating load of the wall

# defining a function that calculate the values of the wall heating load for each U

def UFunction(x):
    y=1149.2*x/(0.438)
    return y

y_series = x_series.apply(UFunction)+heating_load_door_roof #array that contains the values of the wall heating load for each U

# plotting U vs Heating load opaque trend

plt.figure()
plt.title(" U vs Heating load opaque")
plt.xlabel(" U W/m2K")
plt.ylabel(" Q_overall_opaque W")
fig3=plt.plot(x_series,y_series)
plt.figure(3)
