# -*- coding: utf-8 -*-
# horizontal and vertical intended as seen in figure
H = 3 #wall's height
L = 5 #wall's width
A = 0.25 #area correspondig to single layer
Tin = 20 #internal temperature
Tout = -10 #external temperature
hin = 10 #convection heath transfer coefficient, in W/(m^2 C°)
hout = 25 #outer
kb = 0.72 #brick's thermal conductivity
kp = 0.22 #plaster thermal conductivity in W/(m C°)
Lb = 0.16 #spessore bricks
Lp = 0.02
kf = 0.026 #foam
Lf = 0.03 #foam's Thickness
Abr = 0.22 #brick's area for parallel resistance
Apl = 0.015 #plaster's area for parallel resistance
Rin = 1/(hin*A)
Rout = 1/(hout*A)
Rfoam = Lf/(kf*A)
Rplaster = Lp/(kp*A)
Rbricks = Lb/(kb*A)
Rbrpar = Lb/(kb*Abr) #parallel resistance bricks
Rplpar = Lb/(kp*Apl) #parallel resistance plaster. #La lunghezza dei mattoni è quella determinante
Rpar = (1/Rbrpar + 1/Rplpar + 1/Rplpar)**(-1)
Rtot = Rin + Rfoam + Rplaster + Rpar + Rplaster + Rout
print ("total resistance is ")+str(Rtot)+ (" C°/W")
Qtot = ((Tin - Tout)/Rtot)*H*L/A
print ("the rate of heat through the wall is ")+str(Qtot)+(" W")