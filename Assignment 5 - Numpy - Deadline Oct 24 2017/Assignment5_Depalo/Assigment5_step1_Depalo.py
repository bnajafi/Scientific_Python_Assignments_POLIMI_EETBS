# -*- coding: utf-8 -*-
#Assignment 5 - Step 1

import numpy as np
 
resistance_names_series = np.array(["R1","R2","R3","R4","R8"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ resistances_k[resistances_types=="cond"]
Resistances_RValues[resistances_types=="conv"] = 1.0 / resistances_h[resistances_types=="conv"]
Resistances_Rtot_Series=Resistances_RValues.sum()

A_unit=0.25
A_tot=15       #total area of the wall [m**2]

resistance_names_parallel = np.array(["R5","R6","R7"])
resistances_k=np.array([0.22,0.72,0.22])
resistances_L=np.array([0.16,0.16,0.16])
resistances_A=np.array([0.015,0.22,0.015])
Resistances_RValues=np.array(np.zeros(3))
Resistances_RValues=resistances_L/(resistances_k*resistances_A)
Resistances_midstep=(1/Resistances_RValues)
Resistances_Rtot_Parallel=(Resistances_midstep.sum())**(-1)

Resistances_Rtot=Resistances_Rtot_Parallel+Resistances_Rtot_Series/A_unit

T_in=20     #inner temperature [°C]
T_out=-10   #outer temperature

Qtot=A_tot/A_unit*(T_in-T_out)/Resistances_Rtot