# -*- coding: utf-8 -*-
# Assignment 5 step 1

import numpy as np

# Layers in series

A = 0.25
resistances_series_name = np.array(["R1","R2","R3","R4","R5"])
resistances_series_type = np.array(["conv","cond","cond","cond","conv"])
resistances_series_l = np.array([None,0.03,0.02,0.02,None])
resistances_series_k = np.array([None,0.026,0.22,0.22,None])
resistances_series_h = np.array([10.0,None,None,None,25.0])
R_values_s = np.array(np.zeros(5))
R_values_s[resistances_series_type=="conv"] = 1.0/ (resistances_series_h[resistances_series_type=="conv"]*A)
R_values_s[resistances_series_type=="cond"] = resistances_series_l[resistances_series_type=="cond"]/ (resistances_series_k[resistances_series_type=="cond"]*A)
R_tot_series = R_values_s.sum()

# Layers in parallel

resistances_paral_l = np.array([0.16,0.16,0.16])
resistances_paral_k = np.array([0.22,0.72,0.22])
areas = np.array([0.015,0.22,0.015])
R_values_p = (resistances_paral_l/ (resistances_paral_k*areas))**-1
R_tot_parallel = 1.0/(R_values_p.sum())

# Total resistance of the wall

R_TOT = R_tot_series + R_tot_parallel

print 'The total resistance of the wall is '+str(R_TOT)+' m2*C°/W'
