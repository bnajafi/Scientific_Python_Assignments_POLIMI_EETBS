import os
os.chdir("C:\Users\Clevo\Desktop")
import wallCalculations_zhang as wC


wall_onlyInSeries = ["Wood bevel lapped siding","Wood fiberboard sheeting,13mm","Wood stud,38mm*90mm","Gypsum wallboard,13mm"]
wall_withParallel = ["Glass fiber insulation"]

Utot_Parallel_thisWall = wC.wallCalc_withParallel(wall_withParallel)
Utot_Series_thisWall = wC.wallCalc_onlyInSeries(wall_onlyInSeries)

door_layer=["Wood_50mm"]
U_door = wC.wallCalc_onlyInSeries(door_layer)

roof_layer=["AsphaltRoofing"]
U_roof=wC.wallCalc_onlyInSeries(roof_layer)

T_winter= -4.8
T_inside= 20
dT_heating=T_inside-T_winter #The delta T between inside and outside in winter

HF_wall=(Utot_Parallel_thisWall+Utot_Series_thisWall)*dT_heating
HF_door=U_door*dT_heating
HF_roof=U_roof*dT_heating

A_wall= 105.8
A_roof= 200
A_door= 2.2

Q_roof=A_roof*HF_roof
Q_door=A_door*HF_door
Q_wall=A_wall*HF_wall