# -*- coding: utf-8 -*-
print "Hi, welcome to this program for calculating the heat loss through a composite wall"

B=0.22 #Length of brick in m
F=0.015 #Lengh of foam in m
K1 = 0.026 #Conduction heat transfer coefficienc of FOAM in W/m·°C
K2 = 0.22 #Conduction heat transfer coefficienc of PLASTER in W/m·°C
K3 = 0.72 #Conduction heat transfer coefficienc of BRICK in W/m·°C

H1 = 10 #Convection heat transfer coefficient (inside) in W/m2
T1= 20 #Temperature of inside in °C
H2 = 40 #Convection heat transfer coefficient (outside) in W/m2
T2= -10 #Temperature of outside in °C

#Calculation of heat transfer per unit/m
print "We are going to assume 1 m of width for simplifying calculations"

#Resistance calculations

#1st layer: Foam - Convection 
L = B+2*F
A = 1*L
R1 = 1/(H1*A)
print (R1)

#2nd layer: Foam - Conduction
L_f = 0.03
R2 = L_f/(K1*A)
print(R2)

#3rd layer: Plaster - Conduction
L_p = 0.02
R3 = L_p/(K2*A)
print(R3)

#4th layer: Parallel - Conduction
L_4layer = 0.16
R_b = L_4layer/(K3*B)
R_p = L_4layer/(K2*F)
R4 = (1/R_b)+2*(1/R_p)
print(R4)

#5th layer: Plaster 2 - Conduction
L_p = 0.02
R5 = L_p/(K2*A)
print(R5)

#6th layer: Plaster 2 - Convection
R6 = 1/(H2*A)
print(R6)

#TOTAL RESISTANCE
R_Total = R1+R2+R3+R4+R5+R6
print "The Total Resistance of the wall is "+str(R_Total)+" degC/W"

#HEAT TRANSFER LOSS PER UNIT
Q_unit = (T1-T2)/R_Total
print"The heat transfer loss per unit "+str(Q_unit)+" W/unit"

H_w = 3 # High of wall in m
W_w = 5 # Wide of wall in m

A_wall = H_w*W_w
Q_wall = Q_unit*A_wall/A
print "The Total Heat Loss of the composite wall is "+str(Q_wall)+ " W"