# -*- coding: utf-8 -*-
#First assignment - Example D, step2

W_wall = 3    #width of the wall
H_wall = 5    #height of the wall
A_wall = H_wall*W_wall     #area of the wall

#single unit of the wall
H_one = 0.25    #height of the single unit
W_one = 1      #width of the single unit
A_one = H_one*W_one    #area of the single unit

#indoor
h_in = float(raw_input( "Enter the indoor convective heat transfer coefficient in W/m2K "))
R_in = 1/(h_in*A_one)

#foam layer
L_foam = 0.03
k_foam = float(raw_input( "Enter the conductivity of the foam in W/mK "))
R_foam = L_foam/(k_foam*A_one)

#Plaster layer (vertical)
L_plV = 0.02
k_plV = float(raw_input( "Enter the conductivity of the plaster in W/mK "))
R_plV = L_plV/(k_plV*A_one)

#Plaster layer (horizontal)
H_plH = 0.015
A_plH = H_plH*W_one
L_plH = 0.16
k_plH = k_plV
R_plH = L_plH/(k_plH*A_plH)

#brick
H_b = 0.22
A_b = H_b*W_one
L_b = 0.16
k_b = float(raw_input( "Enter the conductivity of the brick in W/mK "))
R_b = L_b/(k_b*A_b)

#outdoor
h_out = float(raw_input( "Enter the outdoor convective heat transfer coefficient in W/m2K "))
R_out = 1/(h_out*A_one)

# equivalent parallel resistance
R_parallel = (1/R_b + 2/R_plH)**(-1)

#total resistance
R_tot = R_in + R_foam + 2*R_plV + R_parallel + R_out

#Heat transfer through the unit
T_in = 20     #inner air temperature
T_out = -10   #outer air temperature
Q_one = (T_in-T_out)/R_tot

#Heat transfer through the whole wall
Q_tot = Q_one*A_wall/A_one

print "The total resistance of the wall unit is " + str(R_tot) + " °C/W"
print "The heat transfer through the unit is " + str(Q_one) + " W"
print "The heat transfer through the whole wall is " + str(Q_tot) + " W"