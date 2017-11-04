# -*- coding: utf-8 -*-
# Conductivity
k_b = 0.72 #conductivity of brick
k_p = 0.22 #conductivity of plaster
k_f = 0.026 #conductivity of foam
# Thickness
L_f = 0.03 #thickness of foam
L_p = 0.02 #thickness of plaster
L_b = 0.16 #thickness of brick
# Temperature
T1 = 20.0 #indoor temperature
T2 = -10.0 #outdoor temperature
# Heat transfer coefficient
h1 = 10 #inner heat transfer coefficient
h2 = 25 #outer heat transfer coefficient
# Area
A = 0.25 #unit area
Apc = 0.015 #plaster area
Ab = 0.22 #brick area
A_wall = 5*3 #area of the wall
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