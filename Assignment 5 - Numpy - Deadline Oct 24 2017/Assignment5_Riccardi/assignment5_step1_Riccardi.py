#assignment 5 - step 1
import numpy as np
#calculations for series resistances
resistance_names_Series = np.array(["OutsideAir","InsideAir","Foam","Plaster1","Plaster2"])
resistances_types_series = np.array(["conv","conv","cond","cond","cond"])
resistances_h = np.array([25.0,10.0,None,None,None])
resistances_k_series=  np.array([None,None,0.026,0.22,0.22])
resistances_L_series= np.array([None,None,0.03,0.02,0.02])
Resistances_RValues_series= np.array(np.zeros(5))
Resistances_RValues_series[resistances_types_series=="cond"] = resistances_L_series[resistances_types_series=="cond"]/ resistances_k_series[resistances_types_series=="cond"]
Resistances_RValues_series[resistances_types_series=="conv"] = 1.0 / resistances_h[resistances_types_series=="conv"]
Resistances_Rtot_series=Resistances_RValues_series.sum()
print ("the value per unit of area is :"+str(Resistances_Rtot_series)+" m2*K/W")
Aunit_series=0.25
Resistances_Rtot1_series=Resistances_Rtot_series/Aunit_series
print ("the value  :"+str(Resistances_Rtot1)+" K/W")

#calculations for parallel resistances
resistance_names_par = np.array(["Brick","Plaster3","Plaster4"])
resistances_k_par=  np.array([0.72,0.22,0.22])
resistances_L_par= np.array([0.16,0.16,0.16])
resistances_A_par=np.array([0.22,0.015,0.015])
Resistances_RValues_par= np.array(np.zeros(3))
Resistances_RValues_par = resistances_L_par/resistances_k_par
Resistances_RValues_par1=Resistances_RValues_par/resistances_A_par
Resistances_RValues_par_inv=Resistances_RValues_par1**-1
Resistances_Rtot_par=Resistances_RValues_par_inv.sum()**-1

Rtot_unit=Resistances_Rtot_par+Resistances_Rtot1_series
print ("The total resistance of the unit is: "+str(Rtot_unit)+" K/W")