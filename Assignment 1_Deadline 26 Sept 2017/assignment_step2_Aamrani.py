# -*- coding: utf-8 -*-

#Name: Rachid Aamrani

print("Dear user, please enter the data")

Kp = float(raw_input("Enter the convective thermal conductivity of plaster in [W/(m^2 °C)]: "))
Kb = float(raw_input("Enter the convective thermal conductivity of brick in in [W/(m^2 °C)]: "))
Kf = float(raw_input("Enter the convective thermal conductivity of foam in in [W/(m^2 °C)]: "))
H1 = float(raw_input("Enter the convective heat inlet coefficient in [W/(m^2 °C)]: "))
H2 = float(raw_input("Enter the convective heat outlet coefficient in [W/(m^2 °C)]: "))

T1 = float(raw_input("Enter the indoor temperature in [°C)]: "))
T2 = float(raw_input("Enter the outdoor temperature in [°C)]: "))

Lf = float(raw_input("Enter the foam thickness in [m]; "))
Lp = float(raw_input("Enter the plaster thickness in [m]: "))
Lb = float(raw_input("Enter the brick thickness in [m]: "))
Ww = float(raw_input("Enter the weight ot the wall in [m]: "))
Wh = float(raw_input("Enter the height of the wall in [m]: "))
Hb = 0.22 #height of brick
Hbp = 0.015
Wl = 1 #it is assumed 

Au = Ww*Wl #unit area
Atot = Ww*Wh 

Rin = (1/(H1*Au)) #indoor resistence
R1 = (Lf/(Kf*Au)) #Foam resistence
R2 = (Lp/(Kp*Au)) #plaster resistence
R3 = (Lb/(Kb*Hb)) ##brick resistence
R4 = (Lb/(Kp*Hbp))#plaster resistence
R5 = R4
R6 = R2
Rout = (1/(H2*Au))

Rtot = Rin+R1+R2+R3+R4+R5+R6+Rout

Qu = (T1-T2)/Rtot
Qtot = Qu*Atot/Au

print("According to data entered the thermal resistence is "+str(Rtot)+"[W/(m^2 °C)]"+"therefore the total heat exchanged is "+str(Qtot)+"[W]")


  