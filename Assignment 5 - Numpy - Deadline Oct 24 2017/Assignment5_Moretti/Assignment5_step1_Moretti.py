# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 5, step 1 - Redoing assignment 2 using numpy's arrays

Giorgio Moretti (10433550)

"""

import numpy as np

res_names = np.array(["indoor","foam","side plaster","center plaster","brick","outdoor"])
res_types = np.array(["conv","cond","cond","cond","cond","conv"])
res_h = np.array([10,None,None,None,None,25])
res_k = np.array([None,0.026,0.22,0.22,0.72,None])
res_L = np.array([None,0.03,0.02,0.16,0.16,None])
res_A = np.array([0.25,0.25,0.25,0.015,0.22,0.25])
Rvalues = np.array(np.zeros(6))
Rvalues[res_types == "cond"] = res_L[res_types == "cond"]/(res_k[res_types == "cond"]*res_A[res_types == "cond"])
Rvalues[res_types == "conv"] = 1.0/(res_h[res_types == "conv"]*res_A[res_types == "conv"])

res_mode = np.array(["series","series","series","parallel","parallel","series"])

res_series = np.append(Rvalues[res_mode == "series"],Rvalues[res_names == "side plaster"])
res_tot_series = res_series.sum()

res_parallel = np.append(Rvalues[res_mode == "parallel"],Rvalues[res_names == "center plaster"])
res_tot_parallel = 1.0/(1.0/res_parallel).sum()

R_TOT = round(res_tot_series + res_tot_parallel,4)

print "\n The total resistance of the wall is: R_WALL_TOT = " + str(R_TOT) + " °C/W"

T_in = 20  # [°C]
T_out = -10  # [°C]

A_unit = 1*0.25  # [m^2]
Qdot_unit = round((T_in - T_out)/R_TOT,4)  # unit heat transfer rate [W]

A_wall = 3*5  # [m^2]
Qdot_wall =  round(Qdot_unit * (A_wall/A_unit),4)  # [W]

print "\n The unit heat transfer rate is: Qdot_UNIT = " + str(Qdot_unit) + " W"
print "\n The heat transfer rate through the wall is: Qdot_WALL = " + str(Qdot_wall) + " W"

