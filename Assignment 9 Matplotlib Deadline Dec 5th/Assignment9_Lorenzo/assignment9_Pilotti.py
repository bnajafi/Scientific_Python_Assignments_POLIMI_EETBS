# Assignment 10

import pandas as pd
import matplotlib.pyplot as plt


# RLF example 1 - Data
labels=["walls", "roof", "door" ]
Areas=[105.8, 200, 2.2]
Areas_series=pd.Series(Areas)
DeltaT_H=24.8
DeltaT_C=7.9
DR=11.9

U_winter=[0.438, 0.25, 1.694]
U_winterSeries=pd.Series(U_winter)
U_summer=[0.435, 0.25, 1.655]
U_summerSeries=pd.Series(U_summer)


#Heating Loads
Q_Heating=Areas_series*U_winterSeries*DeltaT_H
plt.figure()
plt.pie(Q_Heating, labels=labels, startangle=90, explode=(0.1, 0.1, 0.1), autopct='%1.1f%%')
plt.title("Heating loads (opaque surfaces) distribution")

#Cooling Loads
Q_DoorCooling=U_summerSeries[2]*(DeltaT_C+8.2-0.36*DR)*Areas_series[2]
Q_RoofCooling=U_summerSeries[1]*(0.62*DeltaT_C+7.655-0.19*DR)*Areas_series[1]
Q_WallsCooling=U_summerSeries[0]*(DeltaT_C+8.2-0.36*DR)*Areas_series[0]

Q_Cooling=pd.Series([Q_WallsCooling, Q_RoofCooling, Q_DoorCooling])

plt.figure()
plt.pie(Q_Cooling, labels=labels, startangle=90, explode=(0.1, 0.1, 0.1), autopct='%1.1f%%')
plt.title("Cooling loads (opaque surfaces) distribution")

#Changing the U values...
U_Range=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
U_RangeSeries=pd.Series(U_Range)

NewWallsHeating_Load=U_RangeSeries/U_winterSeries[0]*Q_Heating[0]
Q_overall=NewWallsHeating_Load+Q_Heating[1]+Q_Heating[2]

plt.figure()
plt.plot(U_RangeSeries, NewWallsHeating_Load)
plt.title("Q_overall behaviour changing U_value")
plt.xlabel("U range [W/m2/K]")
plt.ylabel("Q_Heating of walls [W]")