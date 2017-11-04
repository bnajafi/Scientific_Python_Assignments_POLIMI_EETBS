# -*- coding: utf-8 -*-
import numpy as np

T1= 20 #Indoor temperature
T2= -10 #Outdoor temperatureL1= 0.03 #Thickness of foam
H=0.25 #Total heigth

#Assuming the width equal to 1m

#Calculating the resistence in series
resistance_names_series = np.array(["R1","R2","R3","R4"])
resistances_types_series = np.array(["conv","cond","cond","conv"])
resistances_h_series = np.array([10,None,None,25])
resistances_k_series=np.array([None,0.026,0.22,None])
resistances_L_series= np.array([None,0.03,0.04,None])
resistances_A_series= 0.25
Resistances_RValues_series= np.array(np.zeros(4))
Resistances_RValues_series[resistances_types_series=="cond"]=resistances_L_series[resistances_types_series=="cond"]/ (resistances_k_series[resistances_types_series=="cond"]*resistances_A_series)
Resistances_RValues_series[resistances_types_series=="conv"] = 1.0 / (resistances_h_series[resistances_types_series=="conv"]*resistances_A_series)
Resistances_Rtot_series=Resistances_RValues_series.sum()

#Calculating the resistence in parallel
resistance_names_parallel = np.array(["R1","R2","R3","R4","R5"])
resistances_types_parallel = np.array(["conv","cond","cond","cond","conv"])
resistances_h_parallel = np.array([10,None,None,None,25])
resistances_k_parallel=np.array([None,0.22,0.22,0.72,None])
resistances_L_parallel= np.array([None,0.16,0.16,0.16,None])
resistances_A_parallel= np.array([None,0.015,0.015,0.22,None])
Resistances_RValues_parallel_recip=resistances_k_parallel[resistances_types_parallel=="cond"]*resistances_A_parallel[resistances_types_parallel=="cond"]/resistances_L_parallel[resistances_types_parallel=="cond"]
Resistances_Rtot_parallel=1/Resistances_RValues_parallel_recip.sum()

#Calculating the RTot
Rtot=Resistances_Rtot_series+Resistances_Rtot_parallel
print ('The total resistence is ') + str(Rtot) + (' °C/W')
print ' '

#Calculating the Q-Value
Q=(T1-T2)/Rtot #Q of the unit area
print ('The rate of heat transfer through the wall per unit area is ') +str(Q) + (' W')
print ' '
Htot=3 #Total height
Ltot=5 #Total width
print ' '
Qtot=Q*Ltot*Htot/H #Q total
print ('The total rate of heat transfer through the wall is ') +str(Qtot) + (' W')