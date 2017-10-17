#HEAT LOSS THROUGH A COMPOSITE WALL 

hi = float(raw_input("Please enter the convection heat transfer coefficient on the inner side in W/m2*degC "))
A = float(raw_input("please enter the area in m2 "))
Ri = 1/(hi*A) #Resistance of the inner environment
print "The resistance of the inner environment is "+str (Ri)+ " (degC/W)"

ho = float(raw_input("Please enter the convection heat transfer coefficient on the outer side in W/m2*degC "))
Ro = 1/(ho*A) #Resistance of the outer environment
print "The resistance of the outer environment is "+str (Ro)+ " (degC/W)"

kf = float(raw_input("Please enter the conductivity of the foam in W/m*degC "))
Lf = float(raw_input("please enter the thickness of the foam in m "))
Rf = Lf/(kf*A) #Resistance of the foam
print "The resistance of the foam is "+str (Rf)+ " (degC/W)"

kp = float(raw_input("Please enter the conductivity of the plaster in series in W/m*degC "))
Lp = float(raw_input("please enter the thickness of the plaster in series in m "))
Rp = Lp/(kp*A) #Resistance of the plaster in series
print "The resistance of the plaster in series is "+str (Rp)+ " (degC/W)"

Apc= float(raw_input("please enter the area of the plaster in the center in m2 "))
Lpc = float(raw_input("please enter the thickness of the plaster in parallel in m "))
Rpc = Lpc/(kp*Apc) #Resistance of the plaster in parallel
print "The resistance of the plaster in parallel is "+str (Rpc)+ " (degC/W)"

kb = float(raw_input("Please enter the conductivity of the brick in W/m*degC "))
Ab= float(raw_input("please enter the area of the brick in m2 "))
Rb = Lpc/(kb*Ab) #Resistance of the brick
print "The resistance of the brick is "+str (Rb)+ " (degC/W)"

Rpll = 1/((1/Rb)+(1/Rpc)+(1/Rpc)) #Equivalent resistance of the parallel system
print "The equivalent resistance in parallel is "+str(Rpll)+" (degC/W)"

Rtot = Rpll + Ri + Ro + 2*Rp + Rf #Total resistance of the wall
print "The total resistance of the wall is "+str (Rtot)+ " (degC/W)"

T81 = float(raw_input("Please enter the temperature of the inner environment "))
T82 = float(raw_input("Please enter the temperature of the outer environment "))
Qunit = (T81 - T82)/Rtot
print "The heat flux through ONE unit is "+str(Qunit)+ " (W)"

Awall = float(raw_input("Please enter the area of the wall in m2 "))
Qwall = Qunit*(Awall/A)
print "The total heat flux through the wall is "+str (Qwall)+ " W"
