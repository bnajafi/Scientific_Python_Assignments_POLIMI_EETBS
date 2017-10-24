import os

import assignment4_wallCalculations_Spirito as WC
  
Layers_atStuds=["woodStud_90mm","gypsum_13mm","commonBrick_100mm","woodFiberboard_13mm","woodBevelLapped"]
Layers_betweenStuds=["gypsum_13mm","commonBrick_100mm","woodFiberboard_13mm","woodBevelLapped","glassfiberInsulation_90mm"]

Wall_results=WC.wallCalc_withParallel(Layers_atStuds,Layers_betweenStuds,0.70,0.30)

DoorLayer=["wood_50mm"]
CeilingLayer=["ceiling_layer"] 

DoorCeiling_results=WC.wallCalc_onlyInSeries(DoorLayer,CeilingLayer)

Tin_winter=20
Td_heating= -4.8
DeltaT_heating= Tin_winter-Td_heating

U_Wall=Wall_results["U_wall"]
U_Door=DoorCeiling_results["U_door"]
U_Ceiling=DoorCeiling_results["U_ceiling"]

HF_wall=DeltaT_heating*U_Wall
HF_door=DeltaT_heating*U_Door
HF_ceiling=DeltaT_heating*U_Ceiling

Area_walls=105.8
Area_ceiling= 200
Area_door= 2.4

print "The heat transfer coefficient U of the ceiling is: "+str(U_Ceiling)+ " W/(m^2 degC) \n"
U_tot=HF_wall*Area_walls+HF_door*Area_door+HF_ceiling*Area_ceiling
print "THE HEATING LOAD FROM OPAQUE SURFACES IS: "+str(U_tot)+ " W"