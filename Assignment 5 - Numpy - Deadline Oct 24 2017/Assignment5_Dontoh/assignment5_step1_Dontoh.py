# Using Numpy to calculate the resistance

import numpy as np

A_wall = 15   # Area of wall [m^2]
A_unit = 0.25     # Unit area ((H_brick+T_p2*2)*W_wall) 

T_1 = 20 # Indoor temperature [degC]
T_2 = -10 # Outdoor temperature [degC]

Resistance_list = np.array(["R_1","R_2","R_f","R_p1","R_p2","R_c1","R_c2","R_b"])
Resistance_types = np.array(["conv","conv","cond","cond","cond","cond","cond","cond"])
Resistance_h = np.array([10,25,None,None,None,None,None,None])
Resistance_k = np.array([None,None,0.026,0.22,0.22,0.22,0.22,0.72])
Resistance_L = np.array([None,None,0.03,0.02,0.02,0.16,0.16,0.16])
resistances_A= np.array([0.25,0.25,0.25,0.25,0.25,0.015,0.015,0.22])
Resistances_RValues = np.array(np.zeros(8))
Resistances_RValues[Resistance_types=="cond"] = Resistance_L[Resistance_types=="cond"]/ (Resistance_k[Resistance_types=="cond"]
                                                *resistances_A[Resistance_types=="cond"])
Resistances_RValues[Resistance_types=="conv"] = 1.0 / (Resistance_h[Resistance_types=="conv"]
                                                    *resistances_A[Resistance_types=="conv"])

#for series layers ["R_1","R_f","R_p1","R_p2","R_2"]
RLayers_series = ["R_1","R_2","R_f","R_p1","R_p2"]
RValues_series = Resistances_RValues[0:5]
Rtot_Series = RValues_series.sum()

#Parallel
RLayers_parallel = ["R_c1","R_c2","R_b"]
RValues_parallel =  1/Resistances_RValues[5:]
Rtot_parallel =1/ RValues_parallel.sum() 

#Total resistance
R_tot = round(Rtot_Series+Rtot_parallel,4)

# Heat transfer
Q_unit = (T_1 - T_2) / R_tot #total heat transfer through the wall per unit width [W]
Q_wall = round((Q_unit * (A_wall/A_unit))) #total heat transfer through the wall [W]
print '*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
print 'The total thermal resistance is '+str(R_tot)+ ' degC/W'
print 'The rate of heat transfer through the wall is '+str(Q_wall)+ ' W'
