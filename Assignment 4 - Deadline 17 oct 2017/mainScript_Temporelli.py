#assignment4_step2_mainScript_Temporelli (only winter)

import sys
import os
ThisfileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisfileDirectory)
print os.getcwd()
import wallCalculation_Temporelli as CW

ListOfSeriesLayersWall=["InsideSurface","WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard","OutsideSurfaceWinter","CommonBrick"]
ListOfParallelLayers=["GlassFiberInsulation","Woodstud"]
ListOfSeriesDoor=["InsideSurface","WoodDoor","OutsideSurfaceWinter"]
ListOfSeriesRoof=["Roof"]
area_fraction_ins = 0.70

U_wall=CW.wallCalc_withParallel(ListOfSeriesLayersWall,ListOfParallelLayers,area_fraction_ins)
print ("U_wall: "+str(U_wall)+" [W/m2K]")
U_door=CW.wallCalc_onlyInSeries(ListOfSeriesDoor)
print ("U_door: "+str(U_door)+" [W/m2K]")
U_roof=CW.wallCalc_onlyInSeries(ListOfSeriesRoof)
print ("U_roof: "+str(U_roof)+" [W/m2K]")

T_outside_winter=-4.8
T_inside_winter=20
deltaT_heating=T_inside_winter-T_outside_winter

HF_wall=deltaT_heating*U_wall
HF_door=deltaT_heating*U_door
HF_roof=deltaT_heating*U_roof

A_wall=105.8
A_door=2.2
A_roof=200

Q_wall=A_wall*HF_wall
Q_door=A_door*HF_door
Q_roof=A_roof*HF_roof

print ("Heating loads: "+"Q_wall: "+str(Q_wall)+" [W]"+" Q_door: "+str(Q_door)+" [W]"+" Q_roof: "+str(Q_roof)+" [W]")
