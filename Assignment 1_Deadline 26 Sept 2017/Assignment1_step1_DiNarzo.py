# -*- coding: utf-8 -*-
h1=10 #The convection heat transfer coefficients on the inner side
h2= 25 #The convection heat transfer coefficients on the outer side
T1= 20 #Indoor temperature
T2= -10 #Outdoor temperature
k1= 0.72 #Bricks
k2= 0.22 #Plastic layers
k3= 0.026 #Foam
L1= 0.03 #Thickness of foam
L2= 0.04 #Total thickness of plastic layers on both sides
L3= 0.16 #Thickness of brick
H1=0.22 #Height of the brick
H2=0.03 #Distance between bricks
#Assuming the width equal to 1m
H=H1+H2
Rconv1= 1.0/(h1*H) #Convection resistence of the inner side
R1=L1/(k3*H) #Resistence of the foam
R2=L2/(k2*H) #Resistence of the plastic layers
R3=L3/(k2*((H2/2))) #Resistence of the plastic layer over and below the brick
R4=L3/(k1*H1) #Resistence of the brick
Rconv2=1.0/(h2*H) #Convection resistence of the outer side
Rparall= (R3*R3*R4)/(R3*R4+R3*R4+R3*R3) #Overall resistence of the part in parallel
Rtot=Rconv1+R2+Rparall+Rconv2+R1
Q=(T1-T2)/Rtot #Q of the unit area
print ' '
print ('The total thermal resistence is equal to ') +str(Rtot) +(' °C/W')
print ' '
print ('The rate of heat transfer through the wall per unit area is ') +str(Q) + (' W')
Htot=3 #Total height
Ltot=5 #Total width
print ' '
Qtot=Q*Ltot*Htot/H #Q total
print ('The total rate of heat transfer through the wall is ') +str(Qtot) + (' W')