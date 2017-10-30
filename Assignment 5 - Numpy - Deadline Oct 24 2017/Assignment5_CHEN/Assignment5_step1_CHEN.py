#Assignment5_Step1_CHEN

import numpy as np

#resistance in series
resistance_names_series = np.array(["R1","R2","R3","R4","R5"])
resistances_types_series = np.array(["conv","cond","cond","cond","conv"])
resistances_h_series = np.array([10,None,None,None,25])
resistances_k_series=  np.array([None,0.026,0.22,0.22,None])
resistances_L_series= np.array([None,0.03,0.02,0.02,None])
resistance_A_series=15 #the total area m2
Resistances_RValues_series= np.array(np.zeros(5))
Resistances_RValues_series[resistances_types_series=="cond"] = resistances_L_series[resistances_types_series=="cond"]/ (resistances_k_series[resistances_types_series=="cond"]*resistance_A_series)
Resistances_RValues_series[resistances_types_series=="conv"] = 1.0 / (resistances_h_series[resistances_types_series=="conv"]*resistance_A_series)
Resistances_Rtot_series=Resistances_RValues_series.sum()

#resistance in parallel
resistance_names_parallel = np.array(["R6","R7","R8"])
resistances_types_parallel = np.array(["cond","cond","cond"])
resistances_k_parallel=  np.array([0.22,0.72,0.22])
resistances_L_parallel= np.array([0.16,0.16,0.16])
resistance_A_parallel=np.array([0.9,13.2,0.9])
Resistances_RValues_parallel= np.array(np.zeros(3))
Resistances_RValues_parallel[resistances_types_parallel=="cond"] = resistances_L_parallel[resistances_types_parallel=="cond"]/( resistances_k_parallel[resistances_types_parallel=="cond"]*resistance_A_parallel)
Resistances_Rtot_Inverse=(1/Resistances_RValues_parallel).sum()
Resistances_Rtot_parallel=1/Resistances_Rtot_Inverse

Resistances_Rtot=Resistances_Rtot_series+Resistances_Rtot_parallel

T1=20 #The indoor temperature
T2=-10 #The outdoor temperature
Q=(T1-T2)/Resistances_Rtot 

print "so the overall resistance of the wall is: " + str(Resistances_Rtot) + " degC/W"
print "so the total heat loss of the wall is: "+ str(Q) + " W"