# -*- coding: utf-8 -*-
#R indoor
hi=float(raw_input("please insert the heat transfer coefficient of the inner side in W/m2°C: "))
H=float(raw_input("please insert the height of the unit in m: "))
w=float(raw_input("please insert the width of the unit in m: "))
A=w*H
Ri=1/(hi*A)
#R foam
Lf=float(raw_input("please insert the thickness of the foam in m: "))
kf=float(raw_input("please insert the conductivity of the foam in W/m*°C: "))
Rf=Lf/(kf*A)
#R plaster1
Lp1=float(raw_input("please insert the thickness of the plaster in m: "))
kp1=float(raw_input("please insert the conductivity of the plaster in W/m*°C: "))
Rp1=Lp1/(kp1*A)
#R plaster2
Rp2=Rp1
#R outdoor
h0=float(raw_input("please insert the heat transfer coefficient of the outer side in W/m2°C: "))
R0=1/(h0*A)
#R pc1
Lpc1=float(raw_input("please insert the thickness of the brick in m: "))
kpc1=float(raw_input("please insert the conductivity of the plaster in W/m*°C: "))
Hpc1=float(raw_input("please insert the height of the upper plaster in m: "))
wpc1=float(raw_input("please insert the width of the upper plaster in m: "))
Apc1=Hpc1*wpc1
Rpc1=Lpc1/(kpc1*Apc1)
# R plaster lower side
Rpc2=Rpc1
# R brick
Lb=float(raw_input("please insert the thickness of the brick in m: "))
kb=float(raw_input("please insert the conductivity of the brick in W/m*°C: "))
Hb=float(raw_input("please insert the height of the brick in m: "))
wb=float(raw_input("please insert the width of the brick in m: "))
Ab=Hb*wb
Rb=Lb/(kb*Ab)
# R parallel
Rpar=1/(1/Rb+1/Rpc1+1/Rpc2)
# R total
Rtot= Ri+Rf+Rp1+Rpar+Rp2+R0
Tindoor=float(raw_input("please insert the temperature indoor in °C: "))
Toutdoor=float(raw_input("please insert the temperature outdoor in °C: "))
Qunit=(Tindoor-Toutdoor)/Rtot
#heat transfer through the wall
Hwall=float(raw_input("please insert the height of the wall in m: "))
Wwall=float(raw_input("please insert the width of the brick in m: "))
Awall=Hwall*Wwall
Qwall=Qunit*Awall/A