# -*- coding: utf-8 -*-
#I'm solving the exercise considering the conductivity of the materials and the convective coeffcients as given by the problem
#so I wont't ask the user to introduce them and I'll use the same values of the step 1.

h1=10 #indoor convective coeffcient [W/(m2*°C)]
h2=25 #outdoor convective coeffcient [W/(m2*°C)]
Kb=0.72 #thermal conductivity of bricks [W/(m*°C)]
Kp=0.22 #thermal conductivity of plaster [W/(m*°C)]
Kf=0.026 #thermal conductivity of foam [W/(m*°C)]

Tinf1=float(raw_input("Enter indoor tenperature [°C]: ")) #indoor temperature  [°C]
Tinf2=float(raw_input("Enter outdoor tenperature [°C]: ")) #outdoor temperature [°C]

H1=float(raw_input("Enter the height of the considered unit [m]: ")) #height of the considered surface [m]
W1=float(raw_input("Enter the depth of the considered unit [m]: ")) #depth [m]
A1=H1*W1 #unit's surface [m2]
R1=1/(h1*A1) # indoor air thermoresistance [°C/W]
R2=1/(h2*A1) # outdoor air thermoresistance [°C/W]
print("R1="+str(R1)+" [°C/W] and R2="+str(R2)+" [°C/W]")

Lf=float(raw_input("Enter the thickness of the foam [m]: "))
Rf=Lf/(Kf*A1) #foam thermoresistance [°C/W]
print("Rf="+str(Rf)+" [°C/W]")

Lp1=float(raw_input("Enter the thickness of the first plaster layer [m]: "))
Rp1=Lp1/(Kp*A1) #thermoresistance of plaster layer 1 [°C/W]
print("Rp1="+str(Rp1)+" [°C/W]")

Lp2=float(raw_input("Enter the thickness of the second plaster layer [m]: "))
Rp2=Lp2/(Kp*A1) #thermoresistance of plaster layer 2 [°C/W]
print("Rp2="+str(Rp2)+" [°C/W]")

Lb=float(raw_input("Enter brick's thickness [m]: ")) #brick's thickness [m]
Hb=float(raw_input("Enter brick's height [m]: ")) #brick's height [m]
Ab=Hb*W1 # brick's surface [m2]
Rb=Lb/(Kb*Ab) #brick's thermoresistance [°C/W]
print("Rb="+str(Rb)+" [°C/W]")

Hc1=float(raw_input("Enter the height of the surface over the brick [m]: ")) #upper surface's height [m]
Ac1=W1*Hc1 #upper surface [m2]
Rc1=Lb/(Kp*Ac1)# upper thermoresistance [°C/W]
print("Rc1="+str(Rc1)+" [°C/W]")

Hc2=float(raw_input("Enter the height of the surface under the brick [m]: ")) #upper surface's height [m]
Ac2=W1*Hc2 #lower surface [m2]
Rc2=Lb/(Kp*Ac2)# lower thermoresistance [°C/W]
print("Rc2="+str(Rc2)+" [°C/W]")

Rpar=(1/Rb+1/Rc1+1/Rc2)**(-1) #parallel resistance of Rb,Rc1 and Rc2 [°C/W]
print("The resistances Rb,Rc1 and Rc2 are in parallel, so the equivalent resistance is Rpar=(1/Rb+1/Rc1+1/Rc2)^(-1)="+str(Rpar)+" [°C/W].")

Rtot=Rtot=R1+Rf+Rp1+Rp2+Rpar+R2 # total resistance of the unit [°C/W]
print("Because of the fact that all the resistances I found are in series, Rtot is given by the sum of all of them: Rtot="+str(Rtot)+" [°C/W].")

Qunit=(Tinf1-Tinf2)/Rtot #heat flow crossing the unit [W]
print("By using the formula Qunit=(Tinf1-Tinf2)/Rtot, the heat flow crossing the unit is: "+str(Qunit)+" [W]")

Hwall=float(raw_input("Enter wall's height [m]: ")) #wall's height [m]
Wwall=float(raw_input("Enter wall's depth [m]: ")) #wall's depth [m]
Awall=Hwall*Wwall #wall's surface [m2]
Qwall=Qunit*Awall/A1 #heat flow crossing the entire wall [W]
print("In the end, the total heat flow crossing the entire wall is Qwall=Qunit*Awall/Aunit="+str(Qwall)+" [W]")









