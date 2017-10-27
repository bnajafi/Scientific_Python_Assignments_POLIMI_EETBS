# -*- coding: utf-8 -*-
import numpy as np

resistance_names = np.array(["Ri","Rf","Rp1","Rp2","Ro"])
resistances_types = np.array(["conv","cond_series","cond_series","cond_series","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
resistances_areas= np.array([0.25,0.25,0.25,0.25,0.25])
Resistances_RValues_series= np.array(np.zeros(5))

#Calculation of Resistance in Series
condition_conv=(resistances_types=="conv")
Resistances_RValues_series[condition_conv]= 1.0/(resistances_h[condition_conv]*resistances_areas[condition_conv]) 
condition_cond_series= (resistances_types=="cond_series") 
Resistances_RValues_series[condition_cond_series]= resistances_L[condition_cond_series]/(resistances_k[condition_cond_series]*resistances_areas[condition_cond_series])
Rtot_series= Resistances_RValues_series.sum()

#Calculation of Resistance in Parallel
resistance_names = np.array(["Rpo1","Rpo2","Rb"])
resistances_k= np.array([0.22,0.22,0.72])
resistances_L= np.array([0.16,0.16,0.16])
resistances_areas= np.array([0.015,0.015,0.22])
Resistances_RValues_parallel_rec=np.array(np.zeros(3))

condition_conv=(resistances_types=="cond_parallel")
Resistances_RValues_parallel_rec[0:3]=1/(resistances_L[0:3]/(resistances_k[0:3]*resistances_areas[0:3]))
Rtot_parallel_rec=Resistances_RValues_parallel_rec.sum()  
R_wall= Rtot_series+(1/Rtot_parallel_rec)
T0=20 #Indoor Temperature
T1=-10 #outdoor Temperature
W_Height=3 #Total Height of wall
W_Wide=5 #Total width of wall
A_total=W_Height*W_Wide #total area of wall
Q_wall = ((T0-T1)/R_wall)*(A_total/0.25)

print'Finally,the total thermal resistance is '+str(R_wall) +'(degC/W)'+' and Total heat transfer across the wall is '+str(Q_wall) +'(W)'
