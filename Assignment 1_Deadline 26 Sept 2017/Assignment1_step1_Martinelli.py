# -*- coding: utf-8 -*-
#horizontal and vertical are inteded as seen in figure
H = 3.0
L = 5.0
Lf = 0.03 #foam layer lenght
Lp = 0.02 #plaster layer series lenght
Lb = 0.16 #brick's horizontal lenght
A = 0.25 #area of single unit, corresponds to the area of the series layers
Ab = 0.22 #area of the brick's parallel resistance
Ap = 0.015 #area of the plaster's parallel resistance
Tin = 20.0
Tout = -10.0
hin = 10.0
hout = 25.0
kf = 0.026
kp = 0.22
kb = 0.72
Rin = 1/(hin*A)
Rout = 1/(hout*A)
Rf = Lf/(kf*A)
Rp1 = Lp/(kp*A)
Rp2 = Rp1
Rpc1 = Lb/(kp*Ap) #area equals to lenght in a 1 meter unit
Rpc2 = Rpc1
Rb = Lb/(kb*Ab) #area equals to lenght in a 1 meter unit
Rpar = (1/Rpc1 + 1/Rpc2 + 1/Rb)**(-1)
Rtot = Rin + Rf + Rp1 + Rpar + Rp2 + Rout
print "the total resistance of the wall is "+str(Rtot)+ " (degC/W)"
Q = (Tin - Tout)/Rtot
print "the rate of heat transfer through the wall for each unit is "+str(Q)+ " (W)"
Qtot = (Q*H*L)/A
print "the total rate of heat transfer through the wall is "+str(Qtot)+ " (W)"