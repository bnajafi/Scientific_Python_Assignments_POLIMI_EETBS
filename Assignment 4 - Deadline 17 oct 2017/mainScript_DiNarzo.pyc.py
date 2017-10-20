# -*- coding: utf-8 -*-
# Importing the function wall_calc

import wallCalculations_DiNarzo as wc

#Calculating the U-Value for the wall

Between_studs= ['Wood_bevel_lapped','Wood_fiberboard','Glass_fiber','Gypsum']
At_studs= ['Wood_bevel_lapped','Wood_fiberboard','Wood_stud','Gypsum']
farea=[0.75,0.25]


results=wc.wall_calc_with_parallel(Between_studs,At_studs,farea)
R_Wall= results['R_total']
U_Wall= results['U_Total']

print ' '

#Calculating the U-Value for the door

Door= ['Wood_5cm']
results_s=wc.wallCalc_onlyInSeries(Door)
R_Door= results_s['R_total_series']
U_Door=results_s['U_Total_series']

print ' '

#Calculating the U-Value for the ceiling 

Ceiling=['Wood_bevel_lapped','Gypsum','Wood_fiberboard']
results_s=wc.wallCalc_onlyInSeries(Ceiling)
R_Ceiling= results_s['R_total_series']
U_Ceiling=results_s['U_Total_series']

print ' '

#Calculating the Q-Value of Opaque surfaces

Delta_T= 24.8

Wall={'U_Value':U_Wall,'Area':105.8}
Door={'U_Value':U_Door,'Area':2.2}
Ceiling={'U_Value':U_Ceiling,'Area':200}

List_of_layers=[Wall,Door,Ceiling]
Q=0
for anyl in List_of_layers:
    HF=anyl['U_Value']*Delta_T
    Q=HF*anyl['Area']
print 'The total Q value is ' +str(Q) +' W' 