#HEAT LOSS THROUGH A COMPOSITE WALL 

hi = 10
A = 0.25
Ri = 1/(hi*A) #Resistance of the inner environment
print "The resistance of the inner environment is "+str (Ri)+ " (degC/W)"

ho = 25
Ro = 1/(ho*A) #Resistance of the outer environment
print "The resistance of the outer environment is "+str (Ro)+ " (degC/W)"

kf = 0.026
Lf = 0.03
Rf = Lf/(kf*A) #Resistance of the foam
print "The resistance of the foam is "+str (Rf)+ " (degC/W)"

kp = 0.22
Lp = 0.02
Rp = Lp/(kp*A) #Resistance of the plaster in series
print "The resistance of the plaster in series is "+str (Rp)+ " (degC/W)"

Apc= 0.15
Lpc = 0.16
Rpc = Lpc/(kp*Apc) #Resistance of the plaster in parallel
print "The resistance of the plaster in parallel is "+str (Rpc)+ " (degC/W)"

kb = 0.72
Ab= 0.22
Rb = Lpc/(kb*Ab) #Resistance of the brick
print "The resistance of the brick is "+str (Rb)+ " (degC/W)"

Rpll = 1/((1/Rb)+(1/Rpc)+(1/Rpc)) #Equivalent resistance of the parallel system
print "The equivalent resistance in parallel is "+str(Rpll)+" (degC/W)"

Rtot = Rpll + Ri + Ro + 2*Rp + Rf #Total resistance of the wall
print "The total resistance of the wall is "+str (Rtot)+ " (degC/W)"

T81 = 20
T82 = -10
Qunit = (T81 - T82)/Rtot
print "The heat flux through ONE unit is "+str(Qunit)+ " (W)"

Awall = 15
Qwall = Qunit*(Awall/A)
print "The total heat flux through the wall is "+str (Qwall)+ " (W)"
