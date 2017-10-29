#Assignment 1 - Step 2 

#Rate of heat transfer through composite wall (values are given by the user) 

#dimenssions of wall that is considered
Height_of_wall=float(raw_input("Please enter the height of wall in [m] ")) 
Width_of_wall=float(raw_input("Please enter the width of wall in [m] "))

#dimenssions of bricks that are used 
H=float(raw_input("Please enter the height of brick in [cm] "))
d=float(raw_input("Please enter the depth of brick in [cm] "))

#thermal conductivity of brick
kb=float(raw_input("Please enter the average thermal conductivity of brick [W/m*degree C] ")) 

#plastic layers
tp=float(raw_input("Please enter the thickness of plastic layers that separates 2 bricks in [cm] "))
tp_side=float(raw_input("Please enter the thickness of plastic layers on each side of the brick in [cm] "))
kp=float(raw_input("Please enter the average thermal conductivity of plastic [W/m*degree C] "))

#foam 
tf=float(raw_input("Please enter the thickness of foam layer on the inner side of the wall in [cm] "))
kf=float(raw_input("Please enter the average thermal conductivity of foam [W/m*degree C] "))

#temperatures
T1=float(raw_input("Please enter the indoor temperature in [degree C] ")) 
T2=float(raw_input("Please enter the outdoor temperature in [degree C] "))

#convection heat transfer coefficients of outer and inner surface 
h1=float(raw_input("Please enter the conv. heat transfer coefficient on inner surface of the wall in [W/m2 degree C] "))
h2=float(raw_input("Please enter the conv. heat transfer coefficient on outer surface of the wall in [W/m2 degree C] "))

#For calculating values of resistances, the width of the wall is considered to be 1 m (Unit area)
#calculation of resistances 
height=H+tp  
Ri=100/(h1*height*1) #because height is given in cm
Rfoam=tf/(kf*height*1) #there is no need for conversition in m because height and tf are given in cm
Rpside=tp_side/(kp*height*1)
Rpcenter=(2*d)/(kp*tp*1) #2*d because A=tp/2 [m2]
Rb=d/(kb*H)
Ro=100/(h2*height)

#calculation of total resistance
Req=((Rpcenter**2)*Rb)/(Rpcenter**2+2*Rb*Rpcenter) #resistance of three layers that are paralel
Rtot=Ri+Rfoam+Rpside+Req+Rpside+Ro
print(" Total thermal resistance of a composite wall is "+str(Rtot)+ " [degree C/W] ")

#calculation of rate of heat transfer through the one unit of composite wall
Qunit=(T1-T2)/Rtot
print(" The rate of heat transfer through one unit of composite wall is "+str(Qunit)+" W")

#calculation of rate of heat transfer through the composite wall
proportion=(Height_of_wall*Width_of_wall)*100/height
Q=Qunit*proportion
print(" The rate of heat transfer through the entire wall is "+ str(Q) + " W")



