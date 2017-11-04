# -*- coding: utf-8 -*-
import numpy as np
resistance_name = np.array(["R1","R2","R3","R4","R5","R6","R7","R8"])
resistance_types = np.array(["conv","condSer","condSer","condSer","condPar","condPar","condPar","conv"])
resistances_h = np.array([10,None,None,None,None,None,None,25]) # Convection heat transfer coefficients
resistances_A = np.array([0.25,0.25,0.25,0.25,0.015,0.22,0.015,0.25]) # Area
resistance_k = np.array([None,0.026,0.22,0.22,0.22,0.72,0.22,None]) # Conduction heat transfer coefficients
resistance_L = np.array([None,0.03,0.02,0.02,0.16,0.16,0.16,None]) # Length
Resistances_Rvalue = np.array(np.zeros(8))
Resistances_Rvalue[(resistance_types == "conv")] = 1.0/(resistances_h[(resistance_types == "conv")]*resistances_A[(resistance_types == "conv")])
Resistances_Rvalue[(resistance_types == "condSer")] = resistance_L[(resistance_types == "condSer")]/(resistance_k[(resistance_types == "condSer")]*resistances_A[(resistance_types == "condSer")])
Resistances_Rvalue[(resistance_types == "condPar")] = resistance_L[(resistance_types == "condPar")]/(resistance_k[(resistance_types == "condPar")]*resistances_A[(resistance_types == "condPar")])
Resistances_Par = Resistances_Rvalue[np.array([False,False,False,False,True,True,True,False])]
U_par = 1/Resistances_Par
R_par_tot = 1/U_par.sum()
Resistances_Series = Resistances_Rvalue[np.array([True,True,True,True,False,False,False,True])]
R_total = Resistances_Series.sum() + R_par_tot
print "The total resistance is "+str(R_total)+" °C/W"
T1 = 20
T2 = -10
A_unit = 0.25
A_tot = 15
Q_unit = (T1-T2)/R_total
Q_wall = Q_unit*(A_tot/A_unit)
print "The total heat flux through the wall is "+str(Q_wall)+" W"