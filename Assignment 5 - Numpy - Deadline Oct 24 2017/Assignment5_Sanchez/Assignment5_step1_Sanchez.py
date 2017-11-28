import numpy as np

def series_array():
    resistance_names = np.array(["R1","R2","R3","R4","R5"])
    resistances_types = np.array(["conv","cond","cond","cond","conv"])
    resistances_h = np.array([10,None,None,None,25])
    resistances_k=  np.array([None,0.026,0.22,0.22,None])
    resistances_L= np.array([None,0.03,0.02,0.02,None])
    Resistances_RValues= np.array(np.zeros(5))
    area=0.25
    Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ (resistances_k[resistances_types=="cond"]*area)
    Resistances_RValues[resistances_types=="conv"] = 1.0 / (resistances_h[resistances_types=="conv"]*area)
    Resistances_Rtot=Resistances_RValues.sum()
    return Resistances_Rtot
    

def parallel_array():
    resistance_names = np.array(["R1","R2", "R3"])
    area=np.array([0.015,0.22, 0.015])
    resistances_k=  np.array([0.22,0.72,0.22])
    resistances_L= 0.16
    Resistances_RValues= np.array(np.zeros(3))
    Resistances_RValues = resistances_k*area/resistances_L
    Resistances_Rtot_temp=Resistances_RValues.sum()
    Resistancesp_Rtot=1/Resistances_Rtot_temp
    return Resistancesp_Rtot
    
Rt=parallel_array()+series_array()

