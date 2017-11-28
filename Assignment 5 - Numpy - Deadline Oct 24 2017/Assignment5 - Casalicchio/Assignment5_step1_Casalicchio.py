# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146
"""

import numpy as np

# List and calculations of resistances
Names = np.array(["indoor","foam","side plaster","center plaster","brick","center plaster","side plaster","outdoor"])
Types = np.array(["conv","cond","cond","cond","cond","cond","cond","conv"])
h = np.array([10,None,None,None,None,None,None,25]) #h [W/m2K]
k = np.array([None,0.026,0.22,0.22,0.72,0.22,0.22,None]) #k [W/mK]
L = np.array([None,0.03,0.02,0.16,0.16,0.16,0.02,None]) #length [m]
A = np.array([0.25,0.25,0.25,0.015,0.22,0.015,0.25,0.25]) #area [m2]
Order = np.array(["series","series","series","parallel","parallel","parallel","series","series"])
Resist = np.array([0,0,0,0,0,0,0,0.])

Resist[Types == "conv"] = 1.0/(h[Types == "conv"]*A[Types == "conv"])
Resist[Types == "cond"] = L[Types == "cond"]/(k[Types == "cond"]*A[Types == "cond"])

R_Series = (Resist[Order == "series"])
Tot_R_Series = R_Series.sum()

R_Parallel = (Resist[Order == "parallel"])
Tot_R_Parallel = 1.0/((1.0/R_Parallel).sum())

R_Wall_Unit = Tot_R_Parallel+Tot_R_Series

print "-----------------------------------------------------------------"
print " The resistance of the unit of the wall is: " + str(round(R_Wall_Unit,4)) + " K/W"

# Heat transfer rate
T_in = 20  # [°C]
T_out = -10  # [°C]

Area_Unit = 1*0.25  # [m2]
Q_Unit = (T_in - T_out)/R_Wall_Unit  # [W]

Area_Wall = 3 * 5  # [m2]
Q_Wall =  Q_Unit * (Area_Wall/Area_Unit)  # [W]

print "\n The heat transfer rate is: " + str(round(Q_Wall,4)) + " W"
print "-----------------------------------------------------------------"
