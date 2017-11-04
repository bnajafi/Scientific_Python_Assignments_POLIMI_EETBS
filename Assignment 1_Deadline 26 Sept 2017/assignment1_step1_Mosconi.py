A= 0.25 #in m2
h1= 10 # in degC/(W*m2)
Ri=1/(h1*A) # indoor convective resistance in degC/W
kf = 0.026
Lf = 0.03
Rf= Lf/(kf*A) # foam conductive resistance in degC/W
kp =0.22
Lp1 =0.02
Rp1=Lp1/(A*kp) # first plaster side conductive resistance in degC/W
Lp2 = 0.02
Rp2=Lp2/(A*kp) # first plaster side conductive resistance in degC/W
h0= 25
R0=1/(h0*A) # outdoor convective resistancein degC/W
Lb = 0.16
t = 0.03 #thickness between two bricks in m
Rpc1= Lb/(kp*t/2) #conductive resistance of layer of plaster above the brick
Rpc2= Lb/(kp*t/2) #conductive resistance of layer of plaster under the brick
kb = 0.72
hb = 0.22
Rb= Lb/(kb*hb) #conductive resistance of brick in degC/W
R_parallel= (1/Rb+1/Rpc1+1/Rpc2)**(-1)
Rtot=Ri+Rf+Rp1+R_parallel+Rp2+R0 # equivalent thermal resistance in degC/W
Ti = 20
To = -10
Q_unit= (Ti-To)/Rtot # rate heat transfer of unit in W
h_wall=3
w_wall= 5
A_wall= h_wall*w_wall # area of the wall in m2
Q_wall= Q_unit*A_wall/A # rate of heat trasnfer through the wall in W

print("The equivalent thermal resistance of unit is "+str(Rtot) +"degC/K")
print("The rate of heat trasnfer through the wall is "+str(Q_wall) +"W")
