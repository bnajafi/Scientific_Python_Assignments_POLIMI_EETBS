# -*- coding: utf-8 -*-
#Material conduvtivity
k_brick=float(raw_input("Please insert the brick's conductive heat transfer coefficient in W/m*°C"))
k_plaster=float(raw_input("Please insert the plaster's conductive heat transfer coefficient in W/m*°C"))
k_foam=float(raw_input("Please insert the foam's conductive heat transfer coefficient in W/m°*C"))

#Temperatures
T1=float(raw_input("Please insert the internal temperature in °C"))
T2=float(raw_input("Please insert the external temperature in °C"))

#Convection heat transfer coefficients
h1=float(raw_input("Please insert the internal convection heat transfer coefficient in W/m^2*°C"))
h2=float(raw_input("Please insert the external convection heat transfer coefficient in W/m^2*°C"))

#Dimensions
A1=float(raw_input("Please insert the area of the foam in m^2"))
A2=A1
A3=float(raw_input("Please insert the area of the plaster in m^2"))
A4=float(raw_input("Please insert the area of the brick in m^2"))
A5=A3
A6=A1
Awall=float(raw_input("Please insert the area of the wall in m^2"))

L1=float(raw_input("Please insert the thickness of the foam in m"))
L2=float(raw_input("Please insert the thickness of the plaster in m"))
L3=float(raw_input("Please insert the thickness of the brick in m"))
L4=L3
L5=L3
L6=L2

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
print"The total resistance is "+str(Rtot)+""
print"The heat flux trough the wall is "+str(Qwall)+""