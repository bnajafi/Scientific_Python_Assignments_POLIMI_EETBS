10# -*- coding: utf-8 -*-

#EXAMPLE D: HEAT LOSS THROUGH A COMPOSITE WALL

#SERIES CALCULATION
import numpy as np

resistance_names = np.array(["Conv_In","Foam","Plaster_S1","PlasterS2","Conv_Out"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
resistances_A= np.array([0.25,0.25,0.25,0.25,0.25])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ (resistances_k[resistances_types=="cond"]*resistances_A[resistances_types=="cond"])
Resistances_RValues[resistances_types=="conv"] = 1.0 / (resistances_h[resistances_types=="conv"]*resistances_A[resistances_types=="conv"])
Resistances_Tot=Resistances_RValues.sum() #Per unit area


#PARALLEL CALCULATIONS

import numpy as np

resist_par_names = np.array(["Brick","Plaster_P1","Plaster_P2"])
resist_par_k=  np.array([0.72,0.22,0.22])
resist_par_L= np.array([0.16,0.16,0.16])
resist_par_A= np.array([0.22,0.015,0.015])
Resist_par_RValues= np.array(np.zeros(3))
Resist_par_RValues = resist_par_L/ (resist_par_k*resist_par_A)
Resist_par_inve=1/Resist_par_RValues #Inverse of each value
Resist_par_tot = Resist_par_inve.sum()


print "The conductive resistance in series is "+str(Resistances_Tot)+" °C/W"
print "The conductive resistance in parallel is "+str(1/Resist_par_tot)+" °C/W"

TOT_RES = (Resistances_Tot)+(1/Resist_par_tot)

print "So, the TOTAL RESISTANCE is "+str(TOT_RES)+" °C/W" 

print"******************************************************"  
print"******************************************************"  

print "Now, let's calculate the heat flux loss of the wall..."

T1=20
T2 = -10

Q_unit = (T1-T2)/TOT_RES
print"The heat transfer loss per unit "+str(Q_unit)+" W/unit"

print"....." 
print"....." 

print "Assuming a wall of 3 m of high and 5 m of wide... "
H_w = 3 # High of wall in m
W_w = 5 # Wide of wall in m
A = 0.25 

A_wall = H_w*W_w
Q_wall = Q_unit*A_wall/A
print "The TOTAL HEAT LOSS of the composite wall is "+str(Q_wall)+ " W"