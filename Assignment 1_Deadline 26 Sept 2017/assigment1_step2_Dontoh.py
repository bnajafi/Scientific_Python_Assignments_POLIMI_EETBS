# -*- coding: utf-8 -*-
# Calcutation of total thermal resistance and heat transfer across a wall
# PLEASE INPUT VALUES TO CALCULATE 

K1 = float(raw_input("Please input the conduction heat transfer coefficienc of FOAM in W/m·°degC "))
K2 = float(raw_input("Please input the conduction heat transfer coefficienc of PLASTER in W/m·degC "))
K3 = float(raw_input("Please input the conduction heat transfer coefficienc of BRICK in W/m·degC "))
H1 = float(raw_input("Please input the convection heat transfer coefficient (into) in W/m2 "))
H2 = float(raw_input("Please input the convection heat transfer coefficient (outer) in W/m2 "))

L=3 #Length of wall in m
W=5 #width of wall in m
B=0.25 #Length of unit composite in m
BB=0.22 #Length of brick in m
BP=0.015 #Length of plaster in parallel in m
T1= 20 #Temperature around the foam in degC
T2= -10 #Temperature of outside wall in degC
# assume 1 m width for the unit/m

# Calculation of resistance across the unit
R1=1/(H1*B*1) #thermal resistance (convection)

#thermal resistance (conduction)
L_f=0.03 # in m
R2=L_f/(K1*B*1) # thermal resistance of foam

L_P=0.02 # in m, vertical plaster
R3=L_P/(K2*B*1) # thermal resistance of vertical plaster

L_p=0.16 # in m, plasters in parallel
R4=L_p/(K2*BP*1) # thermal resistance of horizontal plaster
R5=L_p/(K2*BP*1) # thermal resistance of horizontal plaster
R6=L_p/(K3*BB*1) # thermal resistance of brick
Rp=((1/R4)+(1/R5)+(1/R6))
Rpp=1/Rp # thermal resistance across the parallel brick and horizontal plaster

R7=L_P/(K2*B*1)
R8=1/(H2*B*1)#thermal resistance (convection)
Rtot=R1+R2+R3+Rpp+R7+R8


print "From your input, the total thermal resistance of the unit block is "+str(Rtot)+" degC/W"

#Calculation of heat transfer
Qunit=(T1-T2)/Rtot
Aunit=B*1 # Areal of unit
Awall=L*W # Area of wall
Qwall=(Qunit*Awall)/Aunit
print "From your input, the total heat transfer across the unit block is " +str(Qunit)+ " W" " hence the total heat transfer across the wall is " +str(Qwall)+ " W"
