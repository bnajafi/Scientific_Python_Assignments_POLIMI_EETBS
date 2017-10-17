# -*- coding: utf-8 -*-
# TH.COND.
Kbr = float(raw_input("enter the brick conductivity in W/m°C "))
Kpla = float(raw_input(" enter the plaster conductivity in W/m°C "))
Kf = float(raw_input(" enter the foam conductivity in W/m°C "))

# LENGTH
Lbr = float(raw_input(" enter the brick length in m "))
Lver = float(raw_input(" enter the vertical plaster length in m "))
Lf = float(raw_input(" enter the foam length in m "))

# TEMP,
Tin = float(raw_input(" enter indoor temperature in °C "))
Tout = float(raw_input(" enter outdoor temperature in °C "))

# Area
Aunit = float(raw_input(" enter unit area input in m^2 "))
Apla = float(raw_input(" enter plaster area input in m^2 "))
Abr = float(raw_input(" enter brick area input in m^2 "))
Awall = float(raw_input(" enter wall area input in m^2 "))

# CONVECTION H.T.C 
Hin = float(raw_input(" insert inner convective h.t.coefficient in W/m^2 "))
Hout = float(raw_input(" insert outer convective h.t.coefficient in W/m^2 "))

# The Six Resistance
Ri = 1/(Hin*Aunit)  
Ro = 1/(Hout*Aunit)
Rf = Lf/(Kf*Aunit)   
Rbr = Lbr/(Kbr*Abr)  
Rvp = Lver/(Kpla*Aunit)  
Rhp= Lbr/(Kpla*Apla)

#Total Resistance
Rparallel = 1/((1/Rbr)+(1/Rhp)+(1/Rvp))
Rtot = Rparallel+Ri+Ro+Rf+Rvp+Rvp

#The Heat Transfer 
Qunit = (Tin -Tout)/ Rtot 
Qwall = Qunit * (Awall/Aunit)  

print "Total Resist.is"+str(Rtot)+" [°C/W]"
print "The rate of Heat trans. is "+str(Qwall)+" [W]"