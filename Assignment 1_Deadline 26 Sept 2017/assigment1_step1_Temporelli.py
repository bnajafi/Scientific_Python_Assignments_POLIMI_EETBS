# -*- coding: utf-8 -*-
#Example D step1

#wall
H_wall = 5
W_wall = 3
W_wall= float(W_wall)
A_wall = H_wall*W_wall

#unit
H_unit = 0.25
W_unit = 1
A_unit = H_unit*W_unit

#indoor
h_i = 10
R_i = 1/(h_i*A_unit)

#outdoor
h_o = 25
R_o = 1/(h_o*A_unit)

#foam
L_f = 0.03
k_f = 0.026
R_f = L_f/(k_f*A_unit)

#Plaster
L_p = 0.02
k_p = 0.22
R_p = L_p/(k_p*A_unit)

#Plaster layer
H_pl = 0.015
A_pl = H_pl*W_unit
L_pl = 0.16
k_pl = 0.22
R_pl = L_pl/(k_pl*A_pl)

#brick

H_b = 0.22
A_b = H_b*W_unit
L_b = 0.16
k_b = 0.72
R_b = L_b/(k_b*A_b)

#parallel
R_parallel = (1/R_b + 2/R_pl)**(-1)

#R_tot

R_tot = R_i + R_f + 2*R_p + R_parallel + R_o

#Heat transfer (unit)

T_i = 20
T_o = -10
Q_unit = (T_i-T_o)/R_tot

#Heat transfer (wall)
Q_wall = Q_unit*A_wall/A_unit

print "the total resistance of the unit is: " + str(R_tot) + "°C/W"
print "the heat transfer through the unit results: " + str(Q_unit) + "W"
print "the heat transfer through the wall results: " + str(Q_wall) + "W"
