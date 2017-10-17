# -*- coding: utf-8 -*-
w=float(raw_input("please insert the width of the unit in m"))
H=float(raw_input("please insert the height of the unit in m")) 
A=w*H
hi=float(raw_input("please insert the heat transfer coefficient of the inner side in W/m*°C"))
Ri=1/(A*hi)
kf=float(raw_input("please insert the heat transfer coefficient of the foam in W/m*°C"))
Lf=float(raw_input("please insert the thickness of the foam in m"))
Rf=Lf/(A*kf)
h0=float(raw_input("please insert the heat transfer coefficient of the external side in W/m*°C"))
R0=1/(A*h0)
kp1=float(raw_input("please insert the heat transfer coefficient of the plastic in W/m*°C"))
Lp1=float(raw_input("please insert the thickness of the first plastic layer in m"))
Rp1=Lp1/(A*kp1)
Rp2=Rp1
kpc1=float(raw_input("please insert the heat transfer coefficient of the plastic layer on the sides of the brick in W/m*°C"))
Lpc1=float(raw_input("please insert the thickness of the plastic layer on the sides of the brick in m"))
Hpc1=float(raw_input("please insert the height of the plastic layer on the side of the brick in m"))
Apc1=Hpc1*w
Rpc1=Lpc1/(Apc1*kpc1)
Rpc2=Rpc1
kb=float(raw_input("please insert the heat transfer coefficient of the brick in W/m*°C"))
Lb=float(raw_input("please insert the thickness of the brick in m"))
Hb=float(raw_input("please insert the height of the brick in m"))
Ab=Hb*w
Rb=Lb/(Ab*kb)
Rpar=1/(1/Rb+1/Rpc1+1/Rpc2)
Rtot=Ri+Rp1+Rp2+R0+Rpar+Rf
Ti=float(raw_input("please insert the inner temperature in °C"))
T0=float(raw_input("please insert the external temperature in °C"))
Qunit=(Ti-T0)/Rtot
wwall=float(raw_input("please insert the width of the wall in m"))
Hwall=float(raw_input("please insert the height of the wall in m")) 
Awall=wwall*Hwall
Qwall=Qunit*Awall/A
print ("the resistance is" + str(Rtot)+"m°C/W")
print("the rate of heat tranfer trought the wall is"+str(Qwall)+"W")