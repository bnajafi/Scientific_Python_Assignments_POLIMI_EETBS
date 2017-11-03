#ASSIGNMENT 5 

import numpy as np

#series

R_type=np.array(["conv","cond","cond","cond","conv"])
R_layer=np.array(["R1","R2","R3","R4","R5"])
lenght=np.array([None,0.03,0.02,0.02,None])
k=np.array([None,0.026,0.22,0.22,None])
h=np.array([10,None,None,None,25])

Area=0.25

resistances=np.array(np.zeros(5))
resistances[R_type=="cond"]=lenght[R_type=="cond"]/(k[R_type=="cond"]*Area)
resistances[R_type=="conv"]=1.0/(h[R_type=="conv"]*Area)

resistance_tot=resistances.sum()

print resistances
print resistance_tot

#parallers

R_layer_p=np.array(["R6","R7","R8"])
lenght_p=np.array([0.16,0.16,0.16])
k_p=np.array([0.22,0.72,0.22])

Areas_p=np.array([0.015,0.22,0.015])

resistances_p=lenght_p/(k_p*Areas_p)
inv_resistances=np.array(1/resistances_p)
inv_resistances_tot=inv_resistances.sum()

paraller_resistance_tot=1/inv_resistances_tot

print resistances_p
print paraller_resistance_tot

R_total=resistance_tot+paraller_resistance_tot

print R_total

