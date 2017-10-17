h1 = 10 # the convection heat transfer coefficients on the inner side
A1 = 5*(0.22+0.015+0.015) # area of the indoor heat convection
h2 = 25 # the convection heat transfer coefficients on the outer sides 
A2 = 5*(0.22+0.015+0.015) # area of the outdoor heat convection
L3 = 0.03 # the thickness of foam
k3 = 0.026 # conductivity of foam
A3 = 5*(0.22+0.015+0.015) # area of the foam heat conduction
L4 =L8 =0.02 # the thickness of  plaster layers on each side of the brick
k4 =k5 =k7 =k8 =0.22 # the conduction heat transfer coefficients on the plaster layers
L5 =L7 =0.16 # the thickness of two 1.5 cm thick plaster layers 
A4 =A8 =1.25 # the area of plaster layers on each side of the brick
A5 =A7 =0.075 # the area of each 1.5 cm thick plaster layers
k6 = 0.72 # the conduction heat transfer coefficients on the brick
L6 = 0.16 # the thickness of the brick
A6 = 1.1 #  the conduction heat transfer coefficients on the brick
T1 = 20 # The indoor temperatures 
T2 = 10 # The outdoor temperatures 

R1 = 1/(h1*A1) # The resistance of the inner side
R2 = 1/(h2*A2) # The resistance of the outer sides 
R3 = L3/(k3*A3) # The resistance of the foam
R4 = L4/(k4*A4) # The resistance of the plaster layer 
R5 = L5/(k5*A5) # The resistance of the plaster layers
R6 = L6/(k6*A6) # The resistance of the brick
R7 = L7/(k7*A7) # The resistance of the plaster layers
R8 = L8/(k8*A8) # The resistance of the plaster layers

Rtot = R1+R2+R3+R4+1/(1/R5+1/R6+1/R7)+R8
Q = (T1-T2)/Rtot
Atot = 5*3
A = 5*(0.22+0.015+0.015)
Qtot = Q*Atot/A 
print Rtot
print Qtot