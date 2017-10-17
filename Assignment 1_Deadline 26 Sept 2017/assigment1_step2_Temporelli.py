# -*- coding: utf-8 -*-
#Example D step2

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
h_i = float(raw_input( "please enter the indoor convective heat transfer in W/m2K "))
R_i = 1/(h_i*A_unit)

#outdoor
h_o = float(raw_input( "please enter the outdoor convective heat transfer in W/m2K "))
R_o = 1/(h_o*A_unit)

#foam
L_f = 0.03
k_f = float(raw_input( "please enter the conductivity of the foam in W/mK "))
R_f = L_f/(k_f*A_unit)

#Plaster
L_p = 0.02
k_p = float(raw_input( "please enter the conductivity of the plaster in W/mK "))
R_p = L_p/(k_p*A_unit)

#Plaster layer
H_pl = 0.015
A_pl = H_pl*W_unit
L_pl = 0.16
k_pl = float(raw_input( "please enter the conductivity of the plaster layer in W/mK "))
R_pl = L_pl/(k_pl*A_pl)

#brick

H_b = 0.22
A_b = H_b*W_unit
L_b = 0.16
k_b = float(raw_input( "please enter the conductivityof the brick in W/mK "))
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

print "the total resistance of the unit is: " + str(R_tot) + " °C/W"
print "the heat transfer through the unit results: " + str(Q_unit) + " W"
print "the heat transfer through the wall results: " + str(Q_wall) + " W"
