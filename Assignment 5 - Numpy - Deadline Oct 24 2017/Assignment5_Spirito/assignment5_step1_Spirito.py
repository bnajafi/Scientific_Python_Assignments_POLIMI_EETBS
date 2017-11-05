# -*- coding: utf-8 -*-
# Assignment 5 - Part 1 #
 
 #CALCULATE THE TOTAL WALL RESISTANCE AND THE HEAT TRANSFER RATE THROUGH THE WALL#
  
import numpy as np

resistance_names = np.array(["R1","Rf","Rp1","Rp2","R2"])
resistances_types = np.array(["conv","cond_series","cond_series","cond_series","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
resistances_areas= np.array([0.25,0.25,0.25,0.25,0.25])
Resistances_RValues_series= np.array(np.zeros(5))
 
# Rconv=1/h , Rcond= L/K

#CALCOLO LA SOMMA DELLE RESISTENZE IN SERIE

condition_conv=(resistances_types=="conv")

Resistances_RValues_series[condition_conv]= 1.0/(resistances_h[condition_conv]*resistances_areas[condition_conv]) 

condition_cond_series= (resistances_types=="cond_series") #conductive resistances in series

Resistances_RValues_series[condition_cond_series]= resistances_L[condition_cond_series]/(resistances_k[condition_cond_series]*resistances_areas[condition_cond_series])

Rtot_series= Resistances_RValues_series.sum()

#CALCOLO LA SOMMA DELLE RESISTENZE IN PARALLELO

resistance_names = np.array(["Rpo1","Rpo2","Rb"])
resistances_k= np.array([0.22,0.22,0.72])
resistances_L= np.array([0.16,0.16,0.16])
resistances_areas= np.array([0.015,0.015,0.22])
Resistances_RValues_parallel_rec=np.array(np.zeros(3))

condition_conv=(resistances_types=="cond_parallel")


Resistances_RValues_parallel_rec[0:3]=1/(resistances_L[0:3]/(resistances_k[0:3]*resistances_areas[0:3])) #cioè devo fare la stessa operazione su tutte e tre, che sono dello stesso tipo

Rtot_parallel_rec=Resistances_RValues_parallel_rec.sum()  

Rwall= Rtot_series+(1/Rtot_parallel_rec)

T_in = 20
T_out = -10
A_wall = 15

Q_wall = ((T_in-T_out)/Rwall)*(A_wall/0.25)

print "The total resistance of the wall is "+str(Rwall)+ " degC/W \n"
print "The rate of heat transfer through the wall is "+str(Q_wall)+ "W" 
