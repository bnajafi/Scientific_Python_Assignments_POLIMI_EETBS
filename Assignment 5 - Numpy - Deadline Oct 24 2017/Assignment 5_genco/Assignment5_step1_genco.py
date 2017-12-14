#Assignment 5

import numpy as np
#SERIE
Rlayer=np.array(["R1","R2","R3","R4","R5"])
Rtype=np.array(["conv","cond","cond","cond","conv"])
lenght=np.array([None,0.03,0.02,0.02,None])     
k=np.array([None, 0.026,0.22, 0.22, None])
h=np.array([10, None, None, None,  25])
Area=0.25
R=np.array(np.zeros(5))
R[Rtype=="cond"]=lenght[Rtype=="cond"]/(Area*k[Rtype=="cond"])
R[Rtype=="conv"]=1.0/(Area*h[Rtype=="conv"])
Rtot=R.sum()

#PARALLELO
RlayerP=np.array(["R6","R7","R8"])
lenghtP=0.16
kP=np.array([0.22,0.72,0.22])
AreaP=np.array([0.015, 0.22, 0.015])
RP=lenghtP/(kP*AreaP)
inv_RP=np.array(1/RP)
inv_RPtot=inv_RP.sum()
RPtot=1/inv_RPtot

Rtotal=Rtot+RPtot