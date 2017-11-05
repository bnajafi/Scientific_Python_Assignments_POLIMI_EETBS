print "At first, we're going to calculate the rate of heat transfer through a unit of 0.25m high and 1m deep"
print " "
print "In order to calculate the rate of heat transfer through the wall we should first calculate the thermal resistance of each medium and then the total thermal resistance of the whole medium"
print " "
Ai = float(raw_input("please enter the surface area of the inner side in m^2 "))
h1 = float(raw_input("please enter the convection coefficient of the inner side in W/m^2.degC "))
Ri = 1/(h1*Ai) #Thermal Resistance of the inner side
print "The thermal resistance of the inner side is "+str (Ri)+ " (degC/W)"
print " "
A1 = float(raw_input("please enter the surface area of the foam layer in m^2 "))
Kf = float(raw_input("please enter the conduction coefficient of the foam layer in W/m.degC "))
L1 = float(raw_input("please enter the thickness of the foam layer in m "))
R1 = L1/(Kf*A1) #Thermal Resistance of the foam layer
print "The thermal resistance of the foam layer is "+str (R1)+ " (degC/W)"
print " "
A2 = float(raw_input("please enter the surface area of the plaster layer in m^2 "))
Kplast = float(raw_input("please enter the conduction coefficient of the plaster layer in W/m.degC "))
L2 = float(raw_input("please enter the thickness of the plaster layer in m "))
R2 = L2/(Kplast*A2) #Thermal Resistance of the plaster layer
print "The thermal resistance of the plaster layer is "+str (R2)+ " (degC/W)"
print " "
R6= R2 #R6 is the thermal resistance of the right plaster layer
print "Thermal resistance of the left and right side of the plaster layer is the same having the same thickness and conduction coefficient"
print " "
A3 = float(raw_input("please enter the surface area of the brick in m^2 "))
Kbrick = float(raw_input("please enter the conduction coefficient of the brick in W/m.degC "))
L3 = float(raw_input("please enter the thickness of the brick in m "))
R3 = L3/(Kbrick*A3) #Thermal Resistance of the brick
print "The thermal resistance of the brick is "+str (R3)+ " (degC/W)"
print " "
A4 = float(raw_input("please enter the surface area of the horizontal plaster layer in m^2 "))
L4 = float(raw_input("please enter the thickness of the horziontal plaster layer in m "))
R4 = L4/(Kplast*A4) #Thermal Resistance of the horizontal plaster layer
R5=R4 #R5 is the parallel thermal resistance of the lower horizontal plaster layer
print "The thermal resistance of the two identical horizontal parallel plaster layer is "+str (R4)+ " (degC/W)"
print " "
Ao = float(raw_input("please enter the surface area of the outer side in m^2 "))
h2 = float(raw_input("please enter the convection coefficient of the outer side in W/m^2.degC "))
Ro = 1/(h2*Ao) #Thermal Resistance of the outer side
print "The thermal resistance of the outer side is "+str (Ro)+ " (degC/W)"
print " "
Rtot= Ri+R1+R2+1/(1/R3+1/R4+1/R5)+R6+Ro #Rtot is the total resistance of the whole heat trasnfer
print "Then, The total thermal resistance of the medium is "+str(Rtot)+ " degC/W"
print " "
print "in order to calculate the rate of heat trasnfer of the 0.25 m^2 unit you need to enter the inner and outer temperature"
print " "
Tinfinity1 = float(raw_input("please enter the temperature of the inner side side in degC "))
Tinfinity2 = float(raw_input("please enter the temperature of the outer side side in degC "))
Q= (Tinfinity1-Tinfinity2)/Rtot 
print "so the steady rate of heat transfer through the 0.25 m^2 surface area is "+str(Q)+ " W"
print " "
Aw = float(raw_input("please enter the surface area of the wall in m^2 in order to calculate the rate of heat trasnfer through the wall "))
print " "
Qtot= Q*Aw/Ai
print "Hence, the rate of heat trasnfer through the entire wall becomes "+str(Qtot)+ " W"
