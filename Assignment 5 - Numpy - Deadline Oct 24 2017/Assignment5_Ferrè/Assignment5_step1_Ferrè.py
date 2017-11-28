# -*- coding: utf-8 -*-
import numpy as np

#Series Layer
R_series_names = np.array(["R1","R2","R3","R4","R5"])
R_series_types = np.array(["conv","cond","cond","cond","conv"])
R_series_h = np.array([10,None,None,None,25])
R_series_k =  np.array([None,0.026,0.22,0.22,None])
R_series_L = np.array([None,0.03,0.02,0.02,None])
R_series_values= np.array(np.zeros(5))
A_serie=0.25
R_series_values[R_series_types=="cond"] = R_series_L[R_series_types=="cond"]/ (R_series_k[R_series_types=="cond"]*A_serie)
R_series_values[R_series_types=="conv"] = 1.0 / (R_series_h[R_series_types=="conv"]*A_serie)
R_series_tot=R_series_values.sum()

#Parallel layer
R_parallel_names = np.array(["R6","R7","R8"])
R_parallel_types = np.array(["cond","cond","cond"])
R_parallel_k =  np.array([0.22,0.72,0.22])
R_parallel_L = 0.16
R_parallel_A = np.array([0.015,0.22,0.015])
R_parallel = np.array(np.zeros(3))
R_parallel_value = np.array(np.zeros(3))
R_parallel[R_parallel_types=="cond"] = R_parallel_L / (R_parallel_k[R_parallel_types=="cond"] * R_parallel_A[R_parallel_types=="cond"] )
R_parallel_values = 1/R_parallel[R_parallel_types=="cond"]
R_parallel_tot=R_parallel_values.sum()

#Total resistence
R_tot=R_series_tot+R_parallel_tot
print "Total resistence is: " +str(R_tot) + "°C/W"