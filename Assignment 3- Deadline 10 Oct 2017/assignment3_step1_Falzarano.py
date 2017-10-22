# -*- coding: utf-8 -*-
Ti = 22
To = -2
A_wall = 50*2.5



#list of resistance of the different materials
R_materials = {"outside": 0.03, "woodbevel":0.14, "woodfiber": 0.23, "glassfiber":2.45, "stud": 0.63, "gypsum":0.079, "inside":0.12}
wall_ser = ["outside","woodbevel","woodfiber","gypsum","inside"]
wall_par = ["stud","glassfiber"]

#fraction area of the insulated wall and of the wall with stud
f_area_stud = 0.25
f_area_ins = 0.75


#total resistances in series
Rs_tot = 0
for n in wall_ser:
    Rs_tot = Rs_tot + R_materials[n]
    print ("this layer is: "+ n)
    print ("The value of R for this layer is: "+ str(R_materials[n]))

    
    
 
print ("The sum of the resistances in series is " + str(Rs_tot) + " m°C/W")
print (      )


#different resistances in the wall: stud and ins
R_values = []
for n in wall_par:
    R = Rs_tot + R_materials[n]
    print ("The resistance of the wall when there is " + (n) + " is " + str(R)+ " m°C/W")
    R_values.append(R)
print ()

#U coefficient
U_values = []
for n in R_values:
    U = 1/n
    U_values.append(U)

print ("The corresponding values of U are " + str(U_values))
print ()

#overall value of U
U_overall = U_values[0]*f_area_stud + U_values[1]*f_area_ins
print ("The overall value of U is " + str(U_overall))
print ()

Qwall = U_overall*A_wall*(Ti-To)*0.80
print ("The resulting value of Q is " + str(Qwall) + " W")
