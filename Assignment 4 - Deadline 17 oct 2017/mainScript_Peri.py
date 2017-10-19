## step2 Peri

L_series_wall=["gypsumBoard","WoodFiberboard_13mm","WoodBevel",
"Outside_surface_winter","Inside_surface","CommonBrik"]
L_parallel_wall=["WoodStud_90mm","insulation_glassFiber"]
L_door=["Outside_surface_winter","Inside_surface","Wood_50mm"]
L_ceiling=["Outside_surface_winter","Inside_surface","gypsumBoard","insulation_glassFiber",
"WoodFiberboard_13mm"]

import os
os.chdir("C:\Users\Luca\Desktop\environment")


import wallCalculations_Peri as UtotCalc_sp
import wallCalculations_Peri as UtotCalc_s


A_wall=105.8
A_ceiling=200
A_door=2.2

Delta_T=25
Ratio=0.70

print "\n--------WALL--------\n"
Utot_wall=UtotCalc_sp.wallCalc_withParallel(L_series_wall,L_parallel_wall,Ratio)
print "\n--------DOOR--------\n"
Utot_door=UtotCalc_s.wallCalc_onlySeries(L_door)
print "\n--------CEILING--------\n"
Utot_ceiling=UtotCalc_s.wallCalc_onlySeries(L_ceiling)

Q_wall=Utot_wall*A_wall*Delta_T
print
Q_door=Utot_door*A_door*Delta_T
Q_ceiling=Utot_ceiling*A_ceiling*Delta_T

Qsum=Q_wall+Q_door+Q_ceiling
print "\n\n*_*_*_*_*_*_*_*_*_*_*_*"
print "The total heat transfer of the building is: "+str(Qsum)+" W"
print "*_*_*_*_*_*_*_*_*_*_*_*"

