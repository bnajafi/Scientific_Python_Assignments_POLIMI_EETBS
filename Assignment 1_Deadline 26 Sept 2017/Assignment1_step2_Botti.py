# -*- coding: utf-8 -*-
# Conductivity
k_b = float(raw_input("please enter the brick conductivity in W/m°C "))
k_p = float(raw_input("please enter the plaster conductivity in W/m°C "))
k_f = float(raw_input("please enter the foam conductivity in W/m°C "))
# Thickness
L_b = float(raw_input("please enter the brick thickness in m "))
L_p = float(raw_input("please enter the plaster thickness in m "))
L_f = float(raw_input("please enter the foam thickness in m "))
# Temperature
T1 = float(raw_input("please enter indoor temperature in °C "))
T2 = float(raw_input("please enter outdoor temperature in °C "))
# Area
A = float(raw_input("please enter unit area input in m^2 "))
Apc = float(raw_input("please enter plaster area input in m^2 "))
Ab = float(raw_input("please enter brick area input in m^2 "))
A_wall = float(raw_input("please enter wall area input in m^2 "))
# Convective Coefficients
h1 = float(raw_input("please insert inner convective coefficient in W/m^2 "))
h2 = float(raw_input("please insert outer convective coefficient in W/m^2 "))
# Resistance
R_i = 1/(h1*A) 
R_f = L_f/(k_f*A)
R_p1 = L_p/(k_p*A)
R_p2 = R_p1
R_0 = 1/(h2*A)
# calculating parallel resistance
R_pc1 = L_b/(k_p*Apc)
R_pc2 = R_pc1
R_b = L_b/(k_b*Ab)
R_parallel = 1/((1/R_pc1)+(1/R_pc2)+(1/R_b))
# calculating total resistance
R_tot = R_i+R_f+R_p1+R_p2+R_0+R_parallel
# Rate of heat transfer 
Q_unit = (T1-T2)/R_tot # Rate of heat transfer per unit
Q_wall = Q_unit*(A_wall/A) # Rate of heat transfer through the wall
print "The total resistance is "+str(R_tot)+" [°C/W]"
print "The rate of heat transfer through the wall is "+str(Q_wall)+" [W]"