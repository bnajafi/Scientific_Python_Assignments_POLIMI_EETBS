# -*- coding: utf-8 -*-
#Step 2 Example D-Heat loss through a composite wall
L1=0.03 #thickness of the foam
L2=0.02 #thickness of plaster between brick and foam or brick and outer side
L3=0.16 #thickness of brick 
A1=0.22+0.015+0.015 #unit area of foam, inner and outer plaster
A2=0.22 #unit area of brick
A3=0.03 #unit area of plaster above or below
T1=20 #the indoor temperature
T2=-10 #the outdoor temperature
h=3 #the height of the wall
w=5 #the width of the wall
k1=float(raw_input ("please enter the conductivity of foam in  W/m⋅degreeC"))
k2=float(raw_input ("please enter the conductivity of plaster in  W/m⋅degreeC"))
k3=float(raw_input ("please enter the conductivity of brick in  W/m⋅degreeC"))
h1=float(raw_input ("please enter the convection heat transfer coefficients on the inner side in  W/m2"))
h2=float(raw_input ("please enter the convection heat transfer coefficients on the outer side in  W/m2"))
R0=1/(h1*A1) #convection resistance of inner side
print "The convection resistance of inner side  is " + str(R0) + " degC/W"
R1=L1/(k1*A1) #resistance of the foam
print "The foam resistance  is " + str(R1) + " degC/W"
R2=L2/(k2*A1) #resistance of the inner plaster
print "The inner plaster resistance  is " + str(R2) + " degC/W"
R31=L3/(k2*A3) #resistance of the plaster above the brick
R32=L3/(k3*A2) #resistance of the brick
R33=R31 #resistance of the plaster below the brick
R3=(R31*R32*R33)/(R32*R33+R31*R33+R31*R32) #resistance of the brick and plasters above and below
print "The resistance of the brick and plasters above and below  is " + str(R3) + " degC/W"
R4=R2 #resistance of the outer plaster
print "The outer plaster resistance  is " + str(R4) + " degC/W"
R5=1/(h2*A1) #convection resistance of outer side
print "The convection resistance of outer side  is " + str(R5) + " degC/W"
R6=R0+R1+R2+R3+R4+R5 #total resistance
print "The total resistance  is " + str(R6) + " degC/W"
Q0=(T1-T2)/R6 #the unit heat loss
print "The unit heat loss  is " + str(Q0) + " W"
Q=Q0*((h*w)/A1) #the heat loss
print "The heat loss  is " + str(Q) + " W"