import os 
os.chdir("G:\Sem 1\ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS\Canopy Files\Assignment 4")
import wallCalculations_Parsana as W

material_series1=['wood_bevel_siding','wood_fiberboard_13mm','glass_fiber_90mm','gypsum_13mm']
material_series2=['wood_bevel_siding','wood_fiberboard_13mm','wood_stud_38*90mm','gypsum_13mm']
material_door=['Wood_door_50mm']
material_roof=['asphaltshingles_roofing','Wood_roof_100mm']

wall_Utot=W.U_wall_layer(material_series1,material_series2)["Total U of Wall"]
result=W.U_roof_door(material_door,material_roof)
U_R_door=result["Total U of Door is "]
U_R_roof=result["Total U of Roof is "]

DeltaT=24.8
A_wall=105.8
A_roof=200.0
A_door=2.2

Heat_Load=(wall_Utot*DeltaT)*A_wall+(U_R_door*DeltaT)*A_door+(U_R_roof*DeltaT)*A_roof

print("\nThe total heating load is: "+str(Heat_Load)+" (W)")


