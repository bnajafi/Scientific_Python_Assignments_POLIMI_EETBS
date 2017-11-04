# -*- coding: utf-8 -*-
#Name: Rachid Aamrani

#Data
Kb = 0.72 #Thermal conduttivity brick
Kf = 0.026 #Thermal conduttivity foam
Kp = 0.22 #Thermal conduttivity plaster
H1 = 10 #indoor convective coefficient
H2 = 25 #outdoor convective coefficient

Tinf1 = 20 #Indoor Temperature
Tinf2 = 10 #Outdoor Temperature

H1 = 0.25 #height
W1 = 1.0 #weight
A1 = H1*W1 #Area
Lf = 0.03 #foam thickness
Lp = 0.02 #Plaster thickness
Lb = 0.16 #brick thickness
Hb = 0.22 #brick height
Ab = Lb*Hb #brck area
Hu = 0.015 #height upper area
Au = Hu*W1 #upper area
Hw = 3 #height wall
Ww = 5 #weight wall
Aw = Hw*Ww #area wall


R1 = (1/(H1*A1)) #Convective thermal resistence inside wall
Rf = (Lf/(Kf*A1)) #foam thermoresistence
Rp1 = (Lp/(Kp*A1)) #plaster layer 1 thermoresistence
Rp2 = Rp1 #plaster layer 2 thermoresistence
R2 = (1/(H2*A1)) #convective thermal resistence outdoor 
Rb = (Lb/(Kb*Ab)) #brick thermoresistence
Ru1 = (Lb/(Kp*Au)) #upper thermoresistence
Ru2 = Ru1

T=(1/Rb)+(1/Ru1)+(1/Ru2)
Rpar = 1/T #parallel thermal resistence plaster and brick
Rtot = R1+R2+Rf+Rp1+Rp2+Rpar #total resistence

Qu = (Tinf1-Tinf2)/Rtot #unit heat
Qtot = Qu*Aw/A1 #total heat

print("The total resistence is " + str(Rtot) +" [°C/W]")
print("Therefore the unit heat exchanged is "+str(Qu) +"[W]"+"and the total heat exchanged is "+str(Qtot) +"[W]")
