#Assigment5_step2_Tagliabue -> redo assignment 2 using Numpy
import numpy as np
Ti=20
To=10
A=15
Req=0
#conduction L/kA - convection 1/hA
resistances_names=np.array(["foam","plasterv","plasterh","brick","indoor","outdoor"])
resistances_types=np.array(["cond","cond","cond","cond","conv","conv"])
resistances_parallelserie=np.array(["serie","serie","parallel","parallel","serie","serie"])
resistances_A=np.array([15,15,(3.0/0.25*0.03)*5,(3/0.25*0.22)*5,15,15])
resistances_h=np.array([None,None,None,None,10,20])
resistances_k=np.array([0.026,0.22,0.22,0.72,None,None])
resistances_L=np.array([0.03,0.04,0.16,0.16,None,None])
resistances_values= np.array(np.zeros(6))
resistances_values[(resistances_types == "cond")]=resistances_L[(resistances_types == "cond")]/(resistances_A[(resistances_types == "cond")]*resistances_k[(resistances_types == "cond")])
resistances_values[(resistances_types == "conv")]=1/(resistances_A[(resistances_types == "conv")]*resistances_h[(resistances_types == "conv")])
print ("This is the array with all the resistances values",resistances_values)
resistances_G=1/resistances_values[(resistances_parallelserie=="parallel")]
Rp=1/resistances_G.sum()
Req=resistances_values[(resistances_parallelserie == "serie")].sum()+Rp
print ("The equivalent total resistance is Req=", Req)
Q=(Ti-To)/Req
print ("The rate of heat transfer is Q=", Q)