# -*- coding: utf-8 -*-
#temperatures on the two sides of the wall
T_inf_1 = 20
T_inf_2 = -10

#length of foam layer
Lf = 0.03  

#length of of plastic layers on the sides of the brick
Lp1 = 0.02   
Lp2 = Lp1

#length of the brick
Lb = 0.16

#length of the plastic layer on top/bottom of the brick 
Lp3 = 0.16
Lp4 = Lp3

#Area values
A = 0.25    #area used for layers p1, p2, foam and for the computation of convective heat transfer
Ab = 0.22
Ap3 = 0.015
Ap4 = Ap3


#convective heat transfer coefficients
kb = 0.72
kp = 0.22
kf = 0.026

#conductive heat transfer coefficients
h1 = 10
h2 = 25


#resistances in series
R_conv_1 = 1/(h1*A)
R_conv_2 = 1/(h2*A)
R_f = Lf/(kf*A)
R_p1 = Lp1 /(kp*A)
R_p2 = R_p1

R_ser_tot = R_conv_1 + R_conv_2 + R_f + R_p1 + R_p2

#resistances in parallel
R_b = Lb/(kb*Ab)
R_p3 = Lp3/(kp*Ap3)
R_p4 = R_p3

a = 1/R_b
b = 1/R_p3

R_par_tot = 1/(a+2*b)


#total resistance

R_tot = R_par_tot + R_ser_tot

#total heat loss

Q = (T_inf_1 - T_inf_2)/R_tot

print ("The total thermal resistance of the unit is "+str(R_tot)+" °C/W")

print ("The total heat loss through the unit is " + str(Q) + " W")


#whole wall data
A_wall = 15

Q_wall = Q*A_wall/A

print ("The total heat loss through the wall is " + str(Q_wall) + " W")

