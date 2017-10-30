# -*- coding: utf-8 -*-
import numpy as np

resistance_names = np.array(["R_i","R_f","R_p1","R_pl1","R_b","R_pl2","R_p2","R_o"])
resistances_types = np.array(["conv","cond_ser","cond_ser","cond_par","cond_par","cond_par","cond_ser","conv"])
resistances_h = np.array([10,None,None,None,None,None,None,25])
resistances_k =  np.array([None,0.026,0.22,0.22,0.72,0.22,0.22,None])
resistances_L = np.array([None,0.03,0.02,0.16,0.16,0.16,0.02,None])
resistances_A = np.array([0.25,0.25,0.25,0.015,0.22,0.015,0.25,0.25])
RValues= np.array(np.zeros(8))
#conductive resistance in series
RValues[resistances_types=="cond_ser"] = resistances_L[resistances_types=="cond_ser"]/(resistances_k[resistances_types=="cond_ser"]*resistances_A[resistances_types=="cond_ser"])
#convective resistances
RValues[resistances_types=="conv"] = 1.0 / (resistances_h[resistances_types=="conv"]*resistances_A[resistances_types=="conv"])
#conductive resistances in parallel
RValues[resistances_types=="cond_par"] = (resistances_L[resistances_types=="cond_par"]/ (resistances_k[resistances_types=="cond_par"]*resistances_A[resistances_types=="cond_par"]))**-1

R_tot=RValues.sum()

print "The total resistance is "+str(R_tot)+" °C/W"

T_i = 20
T_o = -10
Q_unit = (T_i-T_o)/R_tot

#wall
H_wall = 5
W_wall = 3
W_wall= float(W_wall)
A_wall = H_wall*W_wall

#unit
H_unit = 0.25
W_unit = 1
A_unit = H_unit*W_unit

#Heat transfer (wall)
Q_wall = Q_unit*A_wall/A_unit


print "the heat transfer through the unit results: " + str(Q_unit) + " W"
print "the heat transfer through the wall results: " + str(Q_wall) + " W"
