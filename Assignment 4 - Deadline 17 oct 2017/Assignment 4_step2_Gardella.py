import os
os.chdir("C:/Users/Fabio/Documents/Polimi/Magistrale/Buildings/Assignments")

from wall_Calculations_Gardella import wallCalc_withParallel;

from wall_Calculations_Gardella import wallCalc_onlyInSeries;


#SOLVE THE EXERCISE

#Data

DeltaT=24.8

Aceiling=200
Awall=105.8
Adoor=2.2


#Wall

WallInSeies=["Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Gypsum_Wallboard"]

WallInParallel=["Glass_Fiber_Insulation","Wood_Stud"]

AreaFraction=0.70

WallData=wallCalc_withParallel(WallInSeies,WallInParallel,AreaFraction)

Uwall=WallData["Utot"]

QHeatWall=Uwall*Awall*DeltaT

#Ceiling

CeilingInSeries=["Wood","Gypsum_Wallboard","Glass_Fiber_Insulation"]

CeilingData=wallCalc_onlyInSeries(CeilingInSeries)

Uceiling=CeilingData["Utot"]

QHeatCeiling=Uceiling*Aceiling*DeltaT

#Door

DoorInSeries=["Wood"]

DoorData=wallCalc_onlyInSeries(DoorInSeries)

Udoor=DoorData["Utot"]

QHeatDoor=Udoor*Adoor*DeltaT