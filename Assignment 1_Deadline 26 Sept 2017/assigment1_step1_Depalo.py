# -*- coding: utf-8 -*-
#First assignment - Example D, step1

W_wall = 3    #width of the wall
H_wall = 5    #height of the wall
A_wall = H_wall*W_wall     #area of the wall

#single unit of the wall
H_one = 0.25    #height of the single unit
W_one = 1      #width of the single unit
A_one = H_one*W_one    #area of the single unit

#indoor
h_in = 10    #inner convection heat transfer coefficient
R_in = 1/(h_in*A_one)

#foam layer
L_foam = 0.03    #foam length
k_foam = 0.026    #foam conductivity
R_foam = L_foam/(k_foam*A_one)    #foam resistance

#Plaster layer (vertical)
L_plV = 0.02    #plaster length
k_plV = 0.22    #plaster conductivity
R_plV = L_plV/(k_plV*A_one)     #plaster resistance

#Plaster layer (horizontal)
H_plH = 0.015    #plaster thickness
A_plH = H_plH*W_one    #plaster frontal area
L_plH = 0.16     #plaster length
k_plH = 0.22     #plaster conductivity
R_plH = L_plH/(k_plH*A_plH)     #plaster resistance

#brick
H_b = 0.22    #brick height
A_b = H_b*W_one     #brick area
L_b = 0.16    #brick length
k_b = 0.72    #brick conductivity
R_b = L_b/(k_b*A_b)     #brick resistance

#outdoor
h_out = 25     #outer convection heat transfer coefficient
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