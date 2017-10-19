import os
os.chdir("C:\Users\Manuel\Documents\Polimi\Building systems\Assignments\Assignment 4")

import wallCalculations_Mosconi as uFunc

series_wall=["gypsumBoard","commonBrick","woodfiberboard_13mm","woodBevel"]
parallel_wall=["glassFiber","woodStud"]
ratio=0.7

U_wall= uFunc.wallCalc_withParallel(series_wall,parallel_wall,ratio)

door_layer=["wood_50mm"]
U_door=uFunc.wallCalc_onlyInSeries(door_layer)

roof_layer=["wood_50mm","glassFiber","asphaltRoofing","woodfiberboard_13mm"]
U_roof=uFunc.wallCalc_onlyInSeries(roof_layer)

T_winter=-4.8
T_inside=20
dT_heating=T_inside-T_winter

A_roof=200
A_net_wall=105.8
A_door=2.2

Q_roof=A_roof*U_roof*dT_heating
Q_door=A_door*U_door*dT_heating
Q_wall=A_net_wall*U_wall*dT_heating