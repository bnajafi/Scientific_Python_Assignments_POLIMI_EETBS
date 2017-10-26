import numpy as np

# Assignment 5, Step 1


resistance_names = np.array(["outdoor air","foam","plaster layer 1","plaster layer 2","1.5 cm thick plaster layer 1","brick","1.5 cm thick plaster layer 2","indoor air"])
resistances_types = np.array(["conv","cond","cond","cond","cond","cond","cond","conv"])
resistances_h = np.array([25,None,None,None,None,None,None,10])
resistances_k=  np.array([None,1.25,1.25,1.25,0.75,1.1,0.075,None])
resistances_L= np.array([None,0.03,0.02,0.02,0.16,0.16,0.16,None])
Resistances_RValues= np.array(np.zeros(8))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ resistances_k[resistances_types=="cond"]
Resistances_RValues[resistances_types=="conv"] = 1.0 / resistances_h[resistances_types=="conv"]
Resistances_Rtot=Resistances_RValues.sum()

print "SO the overall resistance is:" + str(Resistances_Rtot)+ "degC/W*m^2"

T1 = 20 # The indoor temperatures 
T2 = 10 # The outdoor temperatures 

Q = (T1-T2)/Resistances_Rtot
Atot = 5*3
Qtot = Q*Atot
print "So the rate of heat transfer through the wall is:" + str(Qtot)+ "W"
