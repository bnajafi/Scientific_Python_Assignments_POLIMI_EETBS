import numpy as np

resistance_names = np.array([  "Ri",  "Rf", "Rp1", "Rpc1", "Rb", "Rpc2", "Rp2", "Ro"])
resistances_types = np.array(["conv","cond","cond","cond","cond","cond","cond","conv"])
resistances_h = np.array([      10,   None,  None,  None,  None,  None,  None,   25])
resistances_k=  np.array([    None,  0.026,  0.22,  0.22,  0.72,  0.22,  0.22,  None])
resistances_L= np.array([     None,   0.03,  0.02,  0.16,  0.16,  0.16,  0.02,  None])
resistances_A= np.array([     0.25,   0.25,  0.25,  0.15,  0.22,  0.15,  0.25,  0.25])
ATot = 15.0
T81 = 20
T82 = -10
Resistances_RValues= np.array(np.zeros(8))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ (resistances_A[resistances_types=="cond"]*resistances_k[resistances_types=="cond"])
Resistances_RValues[resistances_types=="conv"] = 1.0 / (resistances_A[resistances_types=="conv"]*resistances_h[resistances_types=="conv"])

Resistances_Parallel = np.array(Resistances_RValues[3:6])
Resistance_Tot_Parallel = 1/((1/Resistances_Parallel).sum())

print "The equivalent resistance in parallel is :"+str(Resistance_Tot_Parallel)

index_arrays = np.array([True,True,True,False,False,False,True,True])
Resistances_Series = np.array(Resistances_RValues[index_arrays])
Resistance_Tot_Series = Resistances_Series.sum()

print "The equivalent resistance in series is :"+str(Resistance_Tot_Series)

Resistances_Tot = Resistance_Tot_Series + Resistance_Tot_Parallel

print "The total resistance is :"+str(Resistances_Tot)

Qunit = ((T81-T82)/Resistances_Tot)

Qwall = Qunit*(ATot/0.25)

print "The total heat tranfered through the wall is :"+str(Qwall)