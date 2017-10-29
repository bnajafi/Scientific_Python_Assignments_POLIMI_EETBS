# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 1, step 2 - Heat transfer rate through a composite wall

Giorgio Moretti (10433550)

"""

# HEAT TRANSFER RATE THROUGH ONE UNIT OF THE WALL (length= 1 m)

print "\n NOW YOU WILL ENTER THE DATA FOR THE CALCULATION"

A_unit = float(raw_input("Enter the area of one unit of the wall in m^2 "))
T_in = float(raw_input("Enter the inner temperature in °C "))
T_out = float(raw_input("Enter the outer temperature in °C "))
h_in = float(raw_input("Enter the inner convective heat transfer coefficient in W/m^2°C "))
h_out = float(raw_input("Enter the outer convective heat transfer coefficient in W/m^2°C "))

R_in = 1/(h_in * A_unit)      # inner convective resistance [°C/W]
R_out = 1/(h_out * A_unit)   # outer convective resistance [°C/W]

print "\n THE WALL IS MADE BY PLASTER, BRICK AND RIGID FOAM"

kb = float(raw_input("Enter the conductivity of the brick in W/m°C "))
kp = float(raw_input("Enter the conductivity of the plaster in W/m°C "))            
kf = float(raw_input("Enter the conductivity of the foam in W/m°C "))          

Af = float(raw_input("Enter the area of the foam in m^2 "))
Lf = float(raw_input("Enter the thickness of the foam in m "))
Rf = Lf/(kf * Af)       # foam conductive resistance [°C/W]

Ap = float(raw_input("Enter the area of the side plaster in m^2 "))
Lp = float(raw_input("Enter the thickness of the side plaster in m^2 "))
Rp = Lp/(kp * Ap)       # side plaster conductive resistance [°C/W]

Apc = float(raw_input("Enter the area of the center plaster in m^2 "))
Lpc = float(raw_input("Enter the thickness of the center plaster in m^2 "))
Rpc = Lpc/(kp * Apc)    # center plaster resistance [°C/W]

Ab = float(raw_input("Enter the area of the brick in m^2 "))
Lb = float(raw_input("Enter the thickness of the brick in m^2 "))
Rb = Lb/(kb * Ab)       # brick resistance [°C/W]

# resistances in parallel
R_parallel = 1/Rpc + 1/Rb + 1/Rpc

# total resistance
R_tot = R_in + Rf + Rp + R_parallel + Rp + R_out

# unit heat transfer rate [W]
Qr_unit = (T_in - T_out)/R_tot

# HEAT TRANSFER RATE OF THE WHOLE WALL [W]
A_wall = float(raw_input("Enter the area of the wall in m^2 "))
Qr_wall =  Qr_unit * (A_wall/A_unit)

print "\n The total resistance of the unit is:   R_tot = " + str(R_tot) + " °C/W"
print "\n The unit heat transfer rate is:   Qr_unit = " + str(Qr_unit) + " W"
print "\n The heat transfer rate of the wall is:   Qr_wall = " + str(Qr_wall) + " W"