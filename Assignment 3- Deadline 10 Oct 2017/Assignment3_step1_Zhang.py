Material_library = {"Wood bevel lapped siding":0.14,"Wood fiberboard sheeting,13mm":0.23,"Glass fiber insulation,90mm":2.45,"Wood stud,38mm*90mm":0.63,"Gypsum wallboard,13mm":0.079,"OutSurface 24km/h wind":0.03,"InsideSurface still air":0.12}

layers_wall_serie = ["Wood bevel lapped siding","Wood fiberboard sheeting,13mm","Gypsum wallboard,13mm"]
layers_wall_parallel = ["Glass fiber insulation,90mm","Wood stud,38mm*90mm"]
airOnTwoSides = ["OutSurface 24km/h wind","InsideSurface still air"]
layers_wall_complete = layers_wall_serie + airOnTwoSides + layers_wall_parallel
Rtotseries = 0
    
for anyLayer in layers_wall_serie:
        Rvalues_layers = Material_library[anyLayer]
        Rtotseries = Rtotseries+Rvalues_layers
        print"this layer is:"+ anyLayer
        print"the value of R for this layer is:"+str(Rvalues_layers)
        print"*******************************"
print"the total R value is:"+str(Rtotseries)+"(degC/W)"
print"*******************************"

Rtotpara = 0
for anyLayer in layers_wall_parallel:
        Rvalues_layers = Material_library[anyLayer]
        Rtotpara = Rtotpara+1/Rvalues_layers
        print"this layer is:"+ anyLayer
        print"the value of R for this layer is:"+str(Rvalues_layers)
        print"*******************************"
print"the total R value is:"+str(Rtotpara)+"(degC/W)"
print"*******************************"

Rtotair = 0
for anyLayer in airOnTwoSides:
        Rvalues_layers = Material_library[anyLayer]
        Rtotair = Rtotair+Rvalues_layers
        print"this layer is:"+ anyLayer
        print"the value of R for this layer is:"+str(Rvalues_layers)
        print"*******************************"
print"the total R value is:"+str(Rtotair)+"(degC/W)"
print"*******************************"

Rtot = Rtotair + Rtotpara + Rtotseries
Utot = 1/Rtot
print"the total R value is:"+str(Rtot)+"(degC/W)"
print"the total U value is:"+str(Utot)+"(W/degC)"
print"*******************************"



T1 = 22 #The indoor temperatures
T2 = -2 #The outdoor temperatures 
Atot = 5*2.5 #The area of wall
Q = (T1-T2)/Rtot
Qtot = Atot*Q
print"So the rate of heat transfer through the wall is:" + str(Qtot)+ "W"