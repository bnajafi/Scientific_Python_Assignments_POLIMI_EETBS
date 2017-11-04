# -*- coding: utf-8 -*-
# calculation of heat transfer and total thermal resistance

#Foam and plaster and brick
H_wall=5 #length of the wall in m
W_wall=3 #wide of the wall in m
A_wall=0.25 #surface of the wall m2
A_pc1=0.015 #surface of cross section in m
Lf= 0.03 #thick foam in m
L_p1=0.02 #thick of the plaster in m
L_pc1=0.16 #cross section length in m
L_pc2=0.16 #cross section length in m
L_b=0.16 #length of the brick in m
Ab=0.22 #surface of the brick in m

#insert input
# conductivity of materials 
Kp= float(raw_input("Please input the conduction heat transfer coefficienc of plaster in W/m·°degC "))
kb= float(raw_input("Please input the conduction heat transfer coefficienc of brick in W/m·°degC "))
Kf= float(raw_input("Please input the conduction heat transfer coefficienc of FOAM in W/m·°degC "))

# temperature of inside and outside
T_in=20 #°degC
T_out=-10 ##°degC

#Convection heat transfer coefficents
h1= float(raw_input("Please input the convection heat transfer coefficient (inner) in W/m2 "))
h2= float(raw_input("Please input the convection heat transfer coefficient (outer) in W/m2 "))
#Calculate of the reisistances
Ri=1/(h1*A_wall) #convection resistance
Rf=Lf/(Kf*A_wall) #Thermal resistance of foam °degC/w 
Rp1=L_p1/(Kp*A_wall) #Thermal resistance inner plaster °degC/w 
Rp2=Rp1 #Thermal resistance plaster °degC/w 
Ro=1/(h2*A_wall) #Thermal resistance outer plaster °degC/w 
R_pc1=L_pc1/(kb*A_pc1) #Thermal resistance plaster cross section °degC/w
Rb=L_b/(kb*Ab)
R_parallel=((1/Rb)+(1/R_pc1)+(1/R_pc1))
Rtot=Ri+Rf+Rp1+R_parallel+Rp2+Ro
print "The total resistance is " + str(Rtot) + " ºC/W"

Qu=(T_in-T_out)/Rtot ##calculating the rate of heat transfer
print "The rate of heat transfer across one unit of the wall is " + str(Qu) + " W"

Qwall=Qu*(H_wall*W_wall/A_wall) # #calculating the rate of heat transfer
print "The rate of heat transfer across the whole wall is " + str(Qwall) + " W"