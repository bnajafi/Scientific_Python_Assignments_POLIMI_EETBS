# -*- coding: utf-8 -*-
#Conductivity of materials
k_brick=0.72
k_plaster=0.22
k_foam=0.026

#Temperatures
T1=20 
T2=-10

#Convection heat transfer coefficients
h1=10
h2=25

#Dimensions
Awall=15
A1=0.25
A2=0.25
A3=0.015
A4=0.22
A5=0.015
A6=0.25

L1=0.03
L2=0.02
L3=0.16
L4=0.16
L5=0.16
L6=0.02

#Thermal resistances
R0=1/(h1*A1)
R1=L1/(k_foam*A1)
R2=L2/(k_plaster*A2)
R3=L3/(k_plaster*A3)
R4=L4/(k_brick*A4)
R5=L5/(k_plaster*A5)
R6=L6/(k_plaster*A6)
R7=1/(h2*A1)

Rtot=R0+R1+R2+(1/((1/R3)+(1/R4)+(1/R5)))+R6+R7

#Heat flux per unit of area
Q=(T1-T2)/Rtot

#Heat flux of the entire wall
Qwall=Q*(Awall/A1)

print"The total resistance is "+str(Rtot)+"°C/W"
print"The heat flux trough the wall is "+str(Qwall)+"W"
