import os
os.chdir("C:\Users\Giulia\Desktop\Buildings\python\Assignment")
from WallCalculations_Botti import WallCalc_withParallel

from WallCalculations_Botti import WallCalc_onlyInSeries

WallSer_wall = ["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting13mm","Gypsum_wallboard13mm"]
WallPar_wall = ["Glass_fiber_insulation90mm","Wood_stud38*90mm"]
AreaFraction_wall = 0.70
WallDATA=WallCalc_withParallel(WallSer_wall,WallPar_wall,AreaFraction_wall)
U_wall = WallDATA["U_tot"]

Ser_door = ["Wood25mm"]
DoorDATA=WallCalc_onlyInSeries(Ser_door)
U_door = DoorDATA["U_tot"]

CeilingSer = ["Glass_fiber_insulation90mm","Gypsum_wallboard13mm","Wood25mm"]
CeilingDATA=WallCalc_onlyInSeries(CeilingSer)
U_ceil = CeilingDATA["U_tot"]

delta_T = 24.8
A_ceil = 200
A_door = 2.2
A_wall = 105.8

Q_heat_wall = delta_T*A_wall*U_wall
Q_heat_ceil = delta_T*A_ceil*U_ceil
Q_heat_door = delta_T*A_door*U_door

Q_tot = Q_heat_wall+Q_heat_ceil+Q_heat_door