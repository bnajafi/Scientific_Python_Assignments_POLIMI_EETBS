0.03# -*- coding: utf-8 -*-
#horizontal and vertical are inteded as seen in figure
Lf = float(raw_input("please enter the lenght in m of the foam layer "))
Lp = float(raw_input("please enter the horizontal lenght in m between foam and brick ")) #which in our case is equal to the lenght of the layer on the other side of the brick
Lbo = float(raw_input("please enter the horizontal lenght in m of the brick "))
Lbv = float(raw_input("please enter the vertical lenght in m of the brick "))
Lpv = float(raw_input("please enter the vertical lenght in m of the space between bricks filled with plaster layer "))
Tin = float(raw_input("now enter the internal temperature in degC "))
Tout = float(raw_input("now enter the external temperature in degC "))
hin = float (raw_input("now enter the internal convection heat transfer coefficient in W/(m2 degC) "))
hout = float (raw_input("now enter the external convection heat transfer coefficient in W/(m2 degC) "))
kf = float (raw_input("now enter the thermal conductivity of the foam in W/(m degC) "))
kp = float (raw_input("now enter the thermal conductivity of the plaster in W/(m degC) "))
kb = float (raw_input("now enter the thermal conductivity of the brick in W/(m degC) "))
H = float (raw_input("now enter the high of the wall in m "))
W = float (raw_input("now enter the widht of the wall in m "))
S = H*W #surface of the wall
A = (Lbv + Lpv)*1 # surface of the 1 meter long unit 
Rin = 1/(hin*A)
Rout = 1/(hout*A)
Rf = Lf/(kf*A)
Rp1 = Lp/(kp*A)
Rp2 = Rp1
Rpc1 = Lbo/(kp*(Lpv/2)) #area equals to lenght in a 1 meter unit
Rpc2 = Rpc1
Rb = Lbo/(kb*Lbv) #area equals to lenght in a 1 meter unit
Rpar = (1/Rpc1 + 1/Rpc2 + 1/Rb)**(-1)
Rtot = Rin + Rf + Rp1 + Rpar + Rp2 + Rout
print "the total resistance of the wall is "+str(Rtot)+ " (degC/W)"
Q = (Tin - Tout)/Rtot
print "the rate of heat transfer through the wall for each unit is "+str(Q)+ " (W)"
Qtot = (Q*S)/A
print "the total rate of heat transfer through the wall is "+str(Qtot)+ " (W)"