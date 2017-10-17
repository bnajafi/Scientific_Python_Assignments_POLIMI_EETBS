# -*- coding: utf-8 -*-
# first assignment step1
# data
Tint = 20 # [°C]
Text = -10 # [°C]
kf = 0.026 # thermal conductivity of the foam [W/m*°C]
kb = 0.72 # thermal conductivity of the brick [W/m*°C]
kp = 0.22 # thermal conductivity of the plaster [W/m*°C]
hint = 10 # internal convective coefficient [W/m2*°C]
hext = 25 # external convective coefficient [W/m2*°C]
H = 3 # height of the wall
W = 5 # width of the wall
A = H*W # total surface of the wall

# let's consider only a unit of the wall, formed by 0.25 m2

Lf = 0.03 # foam depth [m]
Af = 0.25 # foam surface [m2]
Lp = 0.02 # first and last part plaster depth [m]
Ap = 0.25 # first and last part plaster surface [m2]
Lp_b = 0.16 # intermediate part plaster depth [m]
Ap_b = 0.015 # intermediate part plaster surface [m2]
Lb = 0.16 # brick depth [m]
Ab = 0.22 # brick surface [m2]

# the equivalent electrical circuit can be schematized as a series of the 
# thermal resistance of the foam, the first part of the plaster, the parallel 
# between two parts of the platser and the brick, the last part of the plaster
# and the two convective resistance

Rf = Lf/(kf*Af)
Rp = Lp/(kp*Ap)
Rb = Lb/(kb*Ab)
Rp_b = Lp_b/(kp*Ap_b)
Rparallel = (1/Rb + 2/Rp_b)**(-1)
Rconv_int = 1/(hint*Af)
Rconv_ext = 1/(hext*Af)

# the total resistace

Rtot = Rconv_int + Rf + Rp + Rparallel + Rp + Rconv_ext

# heat flux per unit of wall

Q = (Tint - Text)/Rtot # [W]

# total heat flux trought the wall 

Qtot = Q*A/Af # [W]

print "the total heat flux through the wall results: " str(Qtot) "W"
