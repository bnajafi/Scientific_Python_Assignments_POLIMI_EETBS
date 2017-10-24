#Call of the file containing the functions 
import os
os.chdir ("D:\Polimi Piacenza\Energy and Environment\notes\3 Python Files and Guidelines\assignment4")


import wallCalculations_Khoudari as WC

series_materials=["wood_bevel","gypsum_13mm", "Common_Brick" ,"fiberboard_13mm"] 
paralel_materials=["glassfiber_90mm","woodstud_90mm"]
fraction=0.7

results_thisWall = WC.wall_calc_parallel(series_materials,paralel_materials,fraction)

#Call of the second function

door= ["Wood_50mm","outsideSurface_winter","insideSurface"]
ceiling=["outsideSurface_winter","insideSurface",
        "fiberboard_13mm","woodstud_90mm","gypsum_13mm"]


results_door = WC.WallCalcOnlyinSeries (door)
results_roof = WC.WallCalcOnlyinSeries (ceiling)

#Calculation of the heat transfer

Tin = 20
Tout = -4.8
delta_T = Tin - Tout

Wall_area = 105.8
Ceiling_area = 20*10
Door_area = 1*2.2

Qwall = Wall_area * delta_T * results_thisWall['Uoverall']
Qdoor = Door_area * delta_T * results_door ['Uoverall']
Qceiling = Ceiling_area * delta_T * results_roof ['Uoverall']

Qtot = Qwall + Qdoor + Qceiling

print "Q of wall= " + str(Qwall) + "W"
print "Q of door= " + str(Qdoor) + "W"
print "Q of ceiling= " + str(Qceiling) + "W"

print "Q total= " + str (Qtot) + "W"

