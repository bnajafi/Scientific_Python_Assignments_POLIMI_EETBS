import os
os.chdir("C:\Users\Lorenzo\Desktop\git_fork_clone\Python4ScientificComputing_Fundamentals\Assignment4")

import wallCalculations_Ferre as FC

series_wall_layer = ["wood_bevel","wood_fiberboard_13mm","gypsum_wallboard_13mm"]
parallel_wall_layer = ["glass_fiber_90mm","wood_stud_38mmx90mm"]
first_ratio=float(0.75)
door = ["wood_5cm"]
roof = ["wood_140mm","asphalt_shingle_roofing"]

U_wall = FC.wallCalc_withParallel(series_wall_layer,parallel_wall_layer,first_ratio)
U_door = FC.wallCalc_onlyInSeries(door)
U_roof = FC.wallCalc_onlyInSeries(roof)

U = {"U_wall":U_wall,"U_door":U_door,"U_roof":U_roof}
print str(U)

T_design_heating = -4.8
T_int = 20
Delta_T_heating =(T_int - T_design_heating)

HF=[]
for anyelement in U:
    HF.append(Delta_T_heating*U[anyelement])

HF={"HF_wall":HF[0],"HF_door":HF[1],"HF_roof":HF[2]}
print str(HF)

A_walls = 105.8
A_door = 2.2
A_roof = 200

Q_heating=[]
for anyelement in HF:
    Q_heating.append(A_walls*HF[anyelement])

Q_heating={"Q_heating_wall":Q_heating[0],"Q_heating_door":Q_heating[1],"Q_heating_roof":Q_heating[2]}
print str(Q_heating)
