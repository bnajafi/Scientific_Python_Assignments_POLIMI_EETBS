# -*- coding: utf-8 -*-
#temperatures on the two sides of the wall
T_inf_1 = 20
T_inf_2 = -10

#IN SERIES
#Conductive Resistances = [Area, Length, Conductivity]

Rf = [0.25, 0.03, 0.026]    #foam layer
Rp1 = [0.25, 0.02, 0.22]    #plastic layer 1
Rp2 = [0.25, 0.02, 0.22]    #plastic layer 2

s = [Rf, Rp1, Rp2]          #list of resistances []

Rs_tot = 0

for i in s:
    Rs = i[1]/(i[0]*i[2])
    Rs_tot = Rs_tot + Rs
    
print ("The total value of the conductive resistances in series is " + str(Rs_tot)+" °C/W")            #total conductive resistance in series


#Convective resistance = [Area, coefficient h]
R_conv_1 = [0.25, 10]
R_conv_2 = [0.25, 25]

c = [R_conv_1, R_conv_2]
Rc_tot = 0

for i in c:
    Rc = 1/(i[0]*i[1])
    Rc_tot = Rc_tot + Rc
    
print ("The total value of the convective resistances is " + str(Rc_tot)+" °C/W")


#IN PARALLEL
#Conductive resistances = [Area, Length, Conductivity]

Rb = [0.22, 0.16, 0.72]           #brick layer
Rp3 = [0.015, 0.16, 0.22]         #plastic layer 3
Rp4 = [0.015, 0.16, 0.22]         #plastic layer 4

p = [Rb, Rp3, Rp4]
Rp_inv_tot = 0

for i in p:
    Rp = i[1]/(i[0]*i[2])
    Rp_inv = 1/Rp
    Rp_inv_tot = Rp_inv_tot + Rp_inv

Rp_tot = 1/(Rp_inv_tot)
print ("The total value of the resistances in parallel is " + str(Rp_tot)+" °C/W")
print ( )
#total resistance list

R_tot = [Rs_tot, Rc_tot, Rp_tot]


#total heat loss

Q = (T_inf_1 - T_inf_2)/(sum(R_tot[0:]))

print ("The total thermal resistance of the unit is "+str(sum(R_tot[0:]))+" °C/W")

print ("The total heat loss through the unit is " + str(Q) + " W")


#wall data = [area of an element, height of the entire wall, width of the entire wall)
Wall = [0.25, 3, 5]

Q_wall = Q*Wall[1]*Wall[2]/Wall[0]

print ("The total heat loss through the wall is " + str(Q_wall) + " W")
