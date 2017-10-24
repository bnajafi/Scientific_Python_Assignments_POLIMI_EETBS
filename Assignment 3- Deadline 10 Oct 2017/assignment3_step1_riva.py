# -*- coding: utf-8 -*-
#ASSIGNMENT 3 

material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
"wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
"gypsum_wallboard":0.079}

inseries=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
inparallel=["glass_fiber","wood_stud"]
air=["outside_surface_winter","inside_surface"]
series=inseries+air
firstratio=0.75 #from data
secondratio=0.25 #from data

R=0
for anymaterial in series:
    Rvalue_layer_series=material_library_dictionary[anymaterial]
    R=R+Rvalue_layer_series

resistence=[]
for anymaterial in inparallel:
    Rvalue_layer_parallel= material_library_dictionary[anymaterial]
    resistence.append(R+Rvalue_layer_parallel)    

A=resistence[0]
B=resistence[1]

print ("the thermal resistences of the FIRST parallel layer is ")+str(A)+" m^2/(deg*W)"
print ("the thermal resistences of the SECOND parallel layer is ")+str(B)+" m^2/(deg*W)"

U1=1/resistence[0]
U2=1/resistence[1]

Utot=(U1*firstratio)+(U2*secondratio)
Rt=1/Utot

print ("the U1 is ")+str(U1)+" W/(deg*m)"
print ("the U2 ")+str(U2)+" W/(deg*m)"
print ("the UTOT is ")+str(Utot)+" W/(deg*m)"
print ("the Rt is ")+str(Rt)+"m^2/(deg*W)"

