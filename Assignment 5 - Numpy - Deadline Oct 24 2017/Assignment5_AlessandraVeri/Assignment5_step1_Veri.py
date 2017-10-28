# -*- coding: utf-8 -*-
import numpy as np

#R series
res_series_names = np.array(["R1","R2","R3","R4","R5"])
res_series_types = np.array(["conv","cond","cond","cond","conv"])
res_series_h = np.array([10,None,None,None,25])
res_series_k=  np.array([None,0.026,0.22,0.22,None])
res_series_L= np.array([None,0.03,0.02,0.02,None])
res_series_A=0.25
Awall=15
Res_series_RValues= np.array(np.zeros(5))
Res_series_RValues[res_series_types=="cond"] = res_series_L[res_series_types=="cond"]/ res_series_k[res_series_types=="cond"]/res_series_A
Res_series_RValues[res_series_types=="conv"] = 1.0 / res_series_h[res_series_types=="conv"]/res_series_A
Res_series_Rtot=Res_series_RValues.sum()
print "R value of resistances in series is: " +str(Res_series_Rtot)
#R parallel
res_par_names = np.array(["R6","R7","R8"])
res_par_k=  np.array([0.22,0.22,0.72])
res_par_L= np.array([0.16,0.16,0.16])
res_par_A=np.array([0.015,0.015,0.22])
Res_par_RValues= np.array(np.zeros(3))
Res_par_RValues=res_par_L/res_par_k/res_par_A
inv_res_par=1/Res_par_RValues
sum_inv=inv_res_par.sum()
Res_par_Rtot=1/(sum_inv)
print "R value of resistances in parallel is: " +str(Res_par_Rtot)
#total Resistance
Rtot=Res_series_Rtot+ Res_par_Rtot
print "total resistance of the wall is: "+str(Rtot)