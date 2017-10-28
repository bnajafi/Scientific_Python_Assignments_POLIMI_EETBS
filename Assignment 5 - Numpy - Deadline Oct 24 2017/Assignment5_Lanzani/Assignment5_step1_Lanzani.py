import numpy as np

Aw=0.25
resistances_series = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_A= np.array([0.25,0.25,0.25,0.25,0.25])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/(resistances_A[resistances_types=="cond"]*resistances_k[resistances_types=="cond"])
Resistances_RValues[resistances_types=="conv"] = 1.0 /(resistances_A[resistances_types=="conv"]*resistances_h[resistances_types=="conv"])
Rtot_series=Resistances_RValues.sum()

resistances_parallel=np.array(["R6","R7","R8"])
resistances_types_p = np.array(["cond","cond","cond"])
resistances_A_p= np.array([0.015,0.22,0.015])
resistances_k_p=  np.array([0.22,0.72,0.22])
resistances_L_p= np.array([0.16,0.16,0.16])
Resistances_RValues_p= np.array(np.zeros(3))
Resistances_RValues_p[resistances_types_p=="cond"] = resistances_L_p[resistances_types_p=="cond"]/(resistances_A_p[resistances_types_p=="cond"]*resistances_k_p[resistances_types_p=="cond"])
Resistances_UValues_p=np.array(np.zeros(3))
Resistances_UValues_p[resistances_types_p=="cond"]=1./Resistances_RValues_p[resistances_types_p=="cond"]
Utot_parallel=Resistances_UValues_p.sum()
Rtot_parallel=1/Utot_parallel

Rtot=Rtot_series+Rtot_parallel
print "Rtot is "+str(Rtot)

#Q
Aw=3*5
T1=20
T2=-10
Q=(T1-T2)/Rtot
A=0.25*1
Qw=Q*(Aw/A)
print 'Qw is '+ str(Qw)+ ' W'
