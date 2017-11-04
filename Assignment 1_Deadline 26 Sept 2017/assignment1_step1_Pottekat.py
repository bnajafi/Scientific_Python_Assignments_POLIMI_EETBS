Ti=20 #Indoor Temperature in deg
To=-10 #Outdoor Temperature in deg

hi=10 #Indoor convective heat treansfer coefficient in W/m2.degC
h0=25 #Outdoor convective heat transfer coefficient in W/m2.degC
Kf=0.026 #Conductive heat transfer coefficient of foam in W/m.degC
Kp=0.22 #Conductive heat transfer coefficient of Plaster in W/m.degC
Kb=0.72 #Conductive heat transfer coefficient of brick in W/m.degC

Lf=0.03 #Thickness of the foam in m
Lp=0.02 #Thickness of the plaster in m
Lb=0.16 #Thickness of the brick in m

H=0.25 #Height of the wall in the considered section
L=1 #assumed depth taking as unit m
Hb=0.22 #Height of brick in the considered section in m
Hp=0.015 #Height of plaster above and below the brick in the considered section in m

Hw=3 #Total height of the wall in m
Ww=5 #Total width of the wall in m

At=Hw*Ww #Total area of wall
Ao=H*L #Area of the wall in the considered section

#CALCULATION OF RESISTANCES

#series resistances
Ri=1/(hi*Ao) #Indoor Resistance 
Rf=Lf/(Kf*Ao) #Foam Resistance
Rp1=Lp/(Kp*Ao) #Resistance of plaster 
Rp2=Rp1 

#parallel resistances
Rpc1=Lb/(Kp*(Hp*L)) #Resistance of plaster above the brick
Rpc2=Rpc1 ##Resistance of plaster below the brick
Rb=Lb/(Kb*(Hb*L)) #Resistance of brick
Rpar=((1/Rpc1)+(1/Rb)+(1/Rpc2))

#total resistance sum of series and parallel
Rtot=Ri+Rf+Rp1+Rpar+Rp2

Qo=(Ti-To)/Rtot #Heat transfer through unit wall
Qt=(Qo*(At/Ao)) # Total Heat transfer of the wall

print 'The total thermal resistance is '+str(Rtot) +' degC/W' +' and the total heat transfer through the wall is '+str(Qt) +' W'