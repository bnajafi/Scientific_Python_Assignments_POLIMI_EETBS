# -*- coding: utf-8 -*-
print "Hi mate, welcome to this program for calculating the heat loss through a composite wall"

T1=float(raw_input("Let's start with the inside temperature of the building in degC "))
T2 = float(raw_input("Now enter the outside temperature of the building in degC "))

H1 = float(raw_input("Please enter the convection heat transfer of the inside temperature in W/m2 "))
H2 = float(raw_input("Don't forgert the convection heat transfer of the outside temperature in W/m2 "))

K1 = float(raw_input("Please enter the conductivity heat transfer coefficient of foam in W/m·degC ")) 
K2 = float(raw_input("Please enter the conductivity heat transfer coefficient of plaster in W/m·degC "))
K3 = float(raw_input("Please enter the conductivity heat transfer coefficient of brick in W/m·degC "))

B = float(raw_input("Please enter the length of brick in m "))

print "We are going to assume 1 m width of the wall to start all the calculations!"
L=float(raw_input("So.... Enter the height of the unit in m "))

F=(L-B)/2

#Calculation of heat transfer per unit/m

#Resistance calculations

#1st layer: Foam - Convection 
A = 1*L
R1 = 1/(H1*A)

#2nd layer: Foam - Conduction
L_f = 0.03
R2 = L_f/(K1*A)

#3rd layer: Plaster - Conduction
L_p = 0.02
R3 = L_p/(K2*A)

#4th layer: Parallel - Conduction
L_4layer = 0.16
R_b = L_4layer/(K3*B)
R_p = L_4layer/(K2*F)
R4 = (1/R_b)+2*(1/R_p)

#5th layer: Plaster 2 - Conduction
L_p = 0.02
R5 = L_p/(K2*A)

#6th layer: Plaster 2 - Convection
R6 = 1/(H2*A)

#TOTAL RESISTANCE
R_Total = R1+R2+R3+R4+R5+R6
print "The total resistance of the composite wall is "+str(R_Total)+ "ºC/W"

#HEAT TRANSFER LOSS PER UNIT
Q_unit = (T1-T2)/R_Total
print "The heat transfer loss per unit is "+str(Q_unit)+ " W/unit"

print "Now let's calculate the heat transfer loss for the whole wall"

H_w = float(raw_input("Please enter the high of the wall in m ")) 
W_w = float(raw_input("Please enter the wide of the wall in m ")) 

A_wall = H_w*W_w
Q_wall = Q_unit*A_wall/A
print "And we are done!!! .. The total heat loss of the composite wall is " +str(Q_wall)+ " W"