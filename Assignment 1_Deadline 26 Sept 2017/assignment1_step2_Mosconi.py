A= float(raw_input ("please enter the area of a unit in m2 "))
h1= float(raw_input ("please enter the indoor convection heat transfer coefficient h1 in W/(m2*C) "))
Ri=1/(h1*A) # indoor convective resistance in degC/W
kf = float(raw_input ("please enter the indoor thermal conductivity kf of foam in W/(m*C) "))
Lf = float(raw_input ("please enter the length of foam layer in m "))
Rf= Lf/(kf*A) # foam conductive resistance in degC/W
kp = float(raw_input ("please enter the thermal conductivity kp of plaster in W/(m*degC) "))
Lp1 = float(raw_input ("please enter the length of the layer of plaster between foam and brick in m "))
Rp1=Lp1/(A*kp) # first plaster side conductive resistance in degC/W
Lp2 = float(raw_input ("please enter the length of the second layer of plaster between brick and outside in m "))
Rp2=Lp2/(A*kp) # first plaster side conductive resistance in degC/W
h0= float(raw_input ("please enter the outdoor convection heat transfer coefficient h0 in W/(m2*degC) "))
R0=1/(h0*A) # outdoor convective resistance in degC/W
Lb = float(raw_input ("please enter the length of the brick in m "))
t = float(raw_input ("please enter the thickness between two bricks in m "))
Rpc1= Lb/(kp*t/2) #conductive resistance of layer of plaster above the brick in degC/W
Rpc2= Lb/(kp*t/2) #conductive resistance of layer of plaster under the brick in degC/W
kb = float(raw_input ("please enter the thermal conductivity kb of brick in W/(m*degC) "))
hb = float(raw_input ("please enter the height of the brick in m "))
Rb= Lb/(kb*hb) #conductive resistance of brick in degC/W
R_parallel= (1/Rb+1/Rpc1+1/Rpc2)**(-1) 
Rtot=Ri+Rf+Rp1+R_parallel+Rp2+R0 # equivalent thermal resistance in degC/W
Ti = float(raw_input ("please enter the indoor temperature in C "))
To = float(raw_input ("please enter the outdoor temperature in C "))
Q_unit= (Ti-To)/Rtot # rate heat transfer of unit in W
h_wall= float(raw_input ("please enter the height of the wall in m "))
w_wall= float(raw_input ("please enter the width of the wall in m "))
A_wall= h_wall*w_wall # area of the wall in m2
Q_wall= Q_unit*A_wall/A # rate of heat trasnfer through the wall in W

print("The equivalent thermal resistance of unit is "+str(Rtot) +"degC/W")
print("The rate of heat transfer through the wall is "+str(Q_wall) +"W")
