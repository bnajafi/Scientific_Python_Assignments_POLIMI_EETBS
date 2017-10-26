# -*- coding: utf-8 -*-
import numpy as np 
Rseries_names=np.array(["Rin","Rf","Rp1","Rp2","Rout"])
Rseries_types=np.array(["conv","cond","cond","cond","conv"])
Rseries_h=np.array([10,None,None,None,25])
Rseries_k=np.array([None,0.026,0.22,0.22,None])
Rseries_L=np.array([None,0.03,0.02,0.02,None])
Rseries_Rvalues=np.array(np.zeros(5))
Rseries_Rvalues[Rseries_types=="conv"]=1.0/Rseries_h[Rseries_types=="conv"]
Rseries_Rvalues[Rseries_types=="cond"]=Rseries_L[Rseries_types=="cond"]/(Rseries_k[Rseries_types=="cond"]*0.25)
Rseries_tot=Rseries_Rvalues.sum()
Rpar_names=np.array(["Rpc1","Rpc2","Rb"])
Rpar_k=np.array([0.22,0.22,0.72])
Rpar_L=np.array([0.16,0.16,0.16])
Rpar_A=np.array([0.015,0.015,0.22])
Rpar_Rvalues=np.array(np.zeros(5))
Upar=np.array(np.zeros(5))
Upar=(Rpar_k*Rpar_A)/Rpar_L
Upar_tot=Upar.sum()
Rpar_tot=1/Upar_tot
Rtot=Rseries_tot+Rpar_tot
print "The total resistance of the wall is "+str(Rtot)+"°C/W"
T1=20
T2=-10
A=15
Q=(T1-T2)*A/(Rtot*0.25)
print "The rate of heat transfered trought the wall is "+str(Q)+" W"