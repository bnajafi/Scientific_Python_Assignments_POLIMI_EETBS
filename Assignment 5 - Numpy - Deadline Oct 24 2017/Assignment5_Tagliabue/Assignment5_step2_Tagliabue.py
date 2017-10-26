# -*- coding: utf-8 -*-
#Assigment5_step3_Tagliabue--> redo step 3
import numpy as np
A=(0.8*50*2.5)#m2
tempvar=24#°C
resistances_names=np.array(["WoodLapSiding","Woodfiberboard","GypsumWall","Glassfiberinsulation","Woodstud","indoor","outdoor"])
resistances_types=np.array(["cond","cond","cond","cond","cond","conv","conv"])
resistances_parallelserie=np.array(["serie","serie","serie","parallel","parallel","serie","serie"])
resistances_R=np.array([0.14,0.23,0.079,2.45,0.63,0.12,0.03])
resistances_G=1/resistances_R[(resistances_parallelserie=="parallel")]         
def function (r_parallelserie,res_R):
    rb=ra=G=0
    ratio=0.75
    for r in res_R[(r_parallelserie=="parallel")]:
        G=(1/r+G)
    ra=1/G    
    print ("rparal is ",ra)
    rb=0 
    for s in res_R[(r_parallelserie=="serie")]:
        rb=rb+s  
    print ("rserie is ",rb)
    U=ratio*(1/rb)+(1-ratio)*(1/ra)
    return (U)
Ufactor= function (resistances_parallelserie,resistances_R)
print ("The overall heat transfer coefficient is ", Ufactor)
Rtot= 1/Ufactor
print ("The overall thermal resistance is ", Rtot)
Q=(Ufactor*A*tempvar)
print ("The overall heat loss is ",Q)