import os
os.chdir("C:\Users\Lavinia\Desktop\PoliPC\Building systems\Wall")
fraction=float(0.70)

layers_wall_parallel= ["glassFiberInsulation_90mm","woodStud_90mm"]
layers_wall_series = ["outsideSurfaceWinter","woodBevel","woodFiberboard_13mm", "gypsumWallboard_13mm","insideSurface","commonBrick"]

import wallcalculation_Persico as WC

U_overall= WC.wall_calc(layers_wall_series,layers_wall_parallel,fraction)

door_layer=["outsideSurfaceWinter","wood","insideSurface"]
U_door= WC.wall_calc_series(door_layer)

roof_layer=["insideSurface", "glassFiberInsulation_90mm","woodStud_90mm","gypsumWallboard_13mm","outsideSurfaceWinter"]
U_roof=WC.wall_calc_series(roof_layer)

T_winter=-4.8
T_inside=20
DeltaT_heating=T_inside-T_winter

A_roof=200
A_net_wall=105.8
A_door=2.2

Q_wall=U_overall*A_net_wall*DeltaT_heating
Q_roof=U_roof*A_roof*DeltaT_heating
Q_door=U_door*A_door*DeltaT_heating
Qtot=Q_wall+Q_roof+Q_door
print "the total load for heating of opaque surfaces is " +str(Qtot)