# -*- coding: utf-8 -*-
# assignment3 
#Determine the overall unit thermal resistance
#and the factor U

material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
"wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
"gypsum_wallboard":0.079}

inseries=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
inparallel=["glass_fiber","wood_stud"]
air=["outside_surface_winter","inside_surface"]
series=inseries+air
firstratio=float(0.75)
secondratio=float(0.25)

R=0
resistence=[]
for anymaterial in inseries:
    Rvalue_layer_series= material_library_dictionary[anymaterial]
    R=R+Rvalue_layer_series
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

