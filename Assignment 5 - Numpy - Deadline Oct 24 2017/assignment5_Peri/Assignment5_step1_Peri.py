#assignment 5step 1 peri

import numpy as np

#resistances in series 
R_names=np.array(["R1","R2","R3","R6","R7"])#from external to internal
R_type=np.array(["conv","cond","cond","cond","conv"])
R_h=np.array([10,None,None,None,25]) #conv. coeffs
R_t=np.array([None,0.03,0.02,0.02,None])#material thickness
R_k=np.array([None,0.026,0.22,0.22,None])# cond. coeff
R_areas=np.array(np.ones(5)*0.25)
Rcalc=np.array(np.zeros(5))
Rcalc[R_type=="conv"]=1.0/(R_h[R_type=="conv"]*R_areas[R_type=="conv"]) #calculates convective resistance
Rcalc[R_type=="cond"]=R_t[R_type=="cond"]/(R_k[R_type=="cond"]*R_areas[R_type=="cond"]) #calculates conductive resistances
R_series=Rcalc.sum()

#resistances in parallel (only conduction)
r_names=np.array(["R4","R5"])
r_t=np.array([0.16,0.16])
r_k=np.array([0.72,0.22])
r_areas=np.array([0.22,0.015])
rcalc=np.array(np.zeros(2))
rcalc=r_t/(r_k*r_areas)
R_parallel=1.0/(1/rcalc[0]+2/rcalc[1])

Rtot=R_series+R_parallel

T_out=-10
T_in=20
DT=T_in-T_out

A_wall=3*5

Q_tot=DT*A_wall/(Rtot*0.25)

print "\n The total heat transfer of the wall is: " +str(Q_tot)+" W"