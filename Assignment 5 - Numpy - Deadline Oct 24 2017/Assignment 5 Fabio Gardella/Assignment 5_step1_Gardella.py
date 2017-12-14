import numpy as np


#RESISTANCES IN SERIES ( CONDUCTIVE + CONVECTIVE )
 
resistance_series_names = np.array(["R0","R1","R2","R6","R7"])
resistances_series_types = np.array(["conv","cond","cond","cond","conv"])
resistances_series_h = np.array([10,None,None,None,25])     #Convective resistances coefficient array
resistances_series_k= np.array([None,0.026,0.22,0.22,None]) #Conductive resistances coefficient array
resistances_series_L= np.array([None,0.03,0.02,0.02,None])  #Conductive resistances lenght array

Area=0.25                                                   #Resistances area 

Resistances_Series_RValues= np.array(np.zeros(5))
Resistances_Series_RValues[resistances_series_types=="cond"] = resistances_series_L[resistances_series_types=="cond"]/ ( resistances_series_k[resistances_series_types=="cond"] * Area) #Resistances values of coduction types
Resistances_Series_RValues[resistances_series_types=="conv"] = 1.0 / ( resistances_series_h[resistances_series_types=="conv"] * Area ) #Resistances values of covection types

Resistance_Series_Rser = Resistances_Series_RValues.sum()   #Total resistance


#RESISTANCES IN PARALLEL

resistance_parallel_names = np.array(["R3","R4","R5"])
resistances_parallel_k = np.array([0.22,0.72,0.22])         #Conductive resistances coefficient array
resistances_parallel_A = np.array([0.015,0.22,0.015])       #Resistances areas array

Lenght = 0.16                                               #Resistances lenght 

Resistances_Parallel_RValues = np.array(np.zeros(3))

Resistances_Parallel_RValues = Lenght / ( resistances_parallel_k *resistances_parallel_A)
Ammittances_Parallel_UValues = 1.0 / Resistances_Parallel_RValues

Ammittance_Parallel_Utot = Ammittances_Parallel_UValues.sum()
Resistance_Parallel_Rpar = 1.0 / Ammittance_Parallel_Utot

#TOTAL RESISTANCE

Rtot = Resistance_Parallel_Rpar + Resistance_Series_Rser

# HEAT FLUX CALCULATIONS

T1=20 
T2=-10
deltaT = T1 - T2

Awall = 15
Aelement = 0.25

Q = deltaT / Rtot                                            #Heat flux of the single element

Qwall=Q*(Awall/Aelement)                                     #Heat flux of the entire wall


