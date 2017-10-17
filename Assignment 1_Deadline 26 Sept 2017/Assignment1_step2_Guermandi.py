# -*- coding: utf-8 -*-
#capital stands for vertical, lowercase means horizontal
#horizontal is intended as shown in the exercise
#follow this order: dimension, thermal properties----foam plaster bricks
H = float(raw_input("please enter the height of the wall [m] "))
L = float(raw_input("please enter the width of the wall [m] "))
Lf = float(raw_input("please enter the horizontal length of foam [m] "))
Lp = float(raw_input("please enter the horizontal length of plaster [m] "))
LP = float(raw_input("please enter the vertical length of plaster between two bricks [m] "))
Lb = float(raw_input("please enter the horizontal length of bricks [m] "))
LB = float(raw_input("please enter the vertical length of bricks [m] "))
print ("now I need to know the thermal properties")
hin = float(raw_input("please enter Hin, internal convection coefficient [w/(m^2 degrees)] "))
hout = float(raw_input("please enter Hout, external convection coefficient [W/(m^2 degrees)] "))
kf = float(raw_input("please enter the thermal conductivity of the foam [W/(m degrees)] "))
kp = float(raw_input("please enter the thermal conductivity of the plaster [W/(m degrees)] "))
kb = float(raw_input("please enter the thermal conductivity of the bricks [W/(m degrees)] "))
print ("is it cold outside?")
Tsup = float(raw_input("please enter the internal temperature ")) #ci starebbe un if che avverte che non c'è scambio di calore se le T° sono uguali
Tinf = float(raw_input("please enter the external temperature "))

A = L*H
a = LP+LB #area for a surface one meter long
Rfoam = Lf/(a*kf)
Rplaster = Lp/(a*kp)
#RR referred to parallel resistance, p for plaster, b for bricks
#the dominant lenght is the brick's one
RRp = 2*Lb/(kp*LP)
RRb = Lb/(kb*LB)
RR = (1/RRp + 1/RRb + 1/RRp)**(-1)
Rhin = 1/(hin*a)
Rhout = 1/(hout*a)
Rtot = Rhin + Rfoam + Rplaster + RR + Rplaster + Rhout
Q = (Tsup-Tinf)/Rtot
Qtot = Q*A/a
print ("Resistance of the wall is ")+str(Rtot)+(" C/W")
print ("heat transfer rate is ")+str(Qtot)+(" W")