# -*- coding: utf-8 -*-
Awall=3*5          #area of the wall
A1=0.25*1          #front area of a single unit in m2
Ab=0.22*1          #frontal area of the brick in m2
A3=0.015*1         #frontal area of the horizontal plaster layer in m2
kb=0.72            #conductivity of the brick in W/m
kp=0.22            #conductivity of the plaster layer in W/m
kf=0.026           #conductivity of the foam in W/m
T1=20              #indoor temperature in degC
T2=-10             #outdoor temperature in degC
h1=10              #inner convection heat transfer coefficient in W/m2
h2 =25             #outer convection heat transfer coefficient in W/m2
Lf=0.03            #Thickness of foam in m
Lp1=0.02           #Thickness of vertical plaster layer in m
Lp2=0.16           #Thickness of horizontal plaster layer in m = thickness of the brick in m


Ri=1/(h1*A1)       #calculating the first convective resistence
Rf=Lf/(kf*A1)      #calculating the resistence of the foam
Rp1=Lp1/(kp*A1)    #calculating the resistence of the vertical plaster layer
Rp2=Rp1            #resistence of the second plaster layer
Ri2=1/(h2*A1)      #calculating the second convective resistence
Rpc=Lp2/(kp*A3)    #calculating the resistence of the horizontal plaster layer
Rb=Lp2/(kb*Ab)     #calculating the resistence of the brick


Rparallel=(1/Rpc)+(1/Rb)+(1/Rpc)    #calculating the equivalent in parallel resistence 
Rtot=Ri+Rf+Rp1+Rparallel+Rp2+Ri2    #calculating the equivalent in series resistence 

Qu=(T1-T2)/Rtot                     #calculating the rate of heat transfer across one unit of the wall
Qwall=Qu*(Awall/A1)                 #calculating the rate of heat transfer across the whole wall


print "The total equivalent thermal resistence of the wall is " + str(Rtot) + " °C/W"
print "The rate of heat transfer across one unit of the wall is " + str(Qu) + " W"
print "The rate of heat transfer across the whole wall is " + str(Qwall) + " W"