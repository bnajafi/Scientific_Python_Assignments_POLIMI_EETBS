# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 5, step 2 - Redoing assignment 3 with numpy's arrays

Giorgio Moretti (10433550)

"""

import numpy as np 

materials = np.array(["outsideSurfaceWinter","insideSurface","woodBevelLappedSiding",
"woodFiberboard","glassFiberInsulation","woodStud","gypsumBoard"])
std_lengths = np.array([None,None,13,13,25,90,13])
std_R = np.array([0.030,0.12,0.14,0.23,0.70,0.63,0.079])

mode = np.array(["series","series","series","series","parallel","parallel","series"])

R_tot_series = np.array([std_R[mode == "series"]]).sum()
R_parallel = np.array([std_R[mode == "parallel"]])

R_wall = R_parallel + R_tot_series

percentage_ins = 0.75

R_TOT = round(R_wall[0,0]*percentage_ins + R_wall[0,1]*(1-percentage_ins),4)
U = round(1/R_TOT,4)

print "\n The overall thermal resistance is: R_TOT = " + str(R_TOT) + " m^2°C/W"
print "\n The global heat transfer coefficient of this wall is: U = " + str(U) + " W/m^2°C"
