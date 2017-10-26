import numpy as np

resistance_names = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
AREA=0.25
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/(resistances_k[resistances_types=="cond"]*AREA)
Resistances_RValues[resistances_types=="conv"] = 1.0 /(resistances_h[resistances_types=="conv"]*AREA)
Resistances_Rtot=Resistances_RValues.sum()

resistance_names = np.array(["R6","R7","R8"])
resistances_types1 = np.array(["cond","cond","cond"])
resistances_k1=  np.array([0.22,0.72,0.22])
resistances_L1= np.array([0.16,0.16,0.16])
resistances_A=np.array([0.015,0.22,0.015])

Resistances_RValues1= np.array(np.zeros(3))
Resistances_RValues1[resistances_types1=="cond"] = resistances_L1[resistances_types1=="cond"]/(resistances_k1[resistances_types1=="cond"]*resistances_A[resistances_types1=="cond"])
Resistances_parallel_fianl= np.array(np.zeros(3))
Resistances_parallel_fianl = (1/ Resistances_RValues1[resistances_types1=="cond"]).sum()

RESISTENZA_TOTALE= Resistances_parallel_fianl+Resistances_Rtot 