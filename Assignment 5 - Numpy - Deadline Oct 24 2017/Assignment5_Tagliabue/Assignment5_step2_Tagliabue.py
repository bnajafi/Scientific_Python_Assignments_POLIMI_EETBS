# -*- coding: utf-8 -*-
#Assigment5_step3_Tagliabue--> redo step 3
import numpy as np
A=(0.8*50*2.5)#m2
tempvar=24#°C
resistances_names=np.array(["WoodLapSiding","Woodfiberboard","GypsumWall","Glassfiberinsulation","Woodstud","indoor","outdoor"])
resistances_types=np.array(["cond","cond","cond","cond","cond","conv","conv"])
resistances_fiber=np.array([True,True,True,True,False,True,True])
resistances_stud=np.array([True,True,True,False,True,True,True])
resistances_R=np.array([0.14,0.23,0.079,2.45,0.63,0.12,0.03])    

def function (r_fiber,r_stub,res_R):
    rb=ra=G=0
    ratio=0.75
    for r in res_R[(resistances_fiber)]:
        ra +=r
    for s in res_R[(resistances_stud)]:
        rb +=s 
    print ("rserie is ",rb)
    U=ratio*(1/rb)+(1-ratio)*(1/ra)
    return (U)
    
Ufactor= function (resistances_fiber,resistances_stud,resistances_R)
print ("The overall heat transfer coefficient is ", Ufactor)
Rtot= 1/Ufactor
print ("The overall thermal resistance is ", Rtot)
Q=(Ufactor*A*tempvar)
print ("The overall heat loss is ",Q)