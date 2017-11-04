# Energy And Environmental Technologies For Building Systems : Assignment 02, Step-1
 
# Submitted By : IMAD AHMED
Y = 3 #y is the height of the wall in m
print "the height of the wall is "+str(Y)+ "m"
X = 5 #X is the width of the wall in m
print "the width of the wall is "+str(X)+ "m"
print " "
print "At first, we're going to calculate the rate of heat transfer through a unit of 0.25m high and 1m deep"
print " "
Tinfinity1 = 20.0 #Tinfinity1 corresponds to then indoor temperature
print "the indoor temperature T infinity1 is "+str(Tinfinity1)+ " degrees"
print " "
Tinfinity2 = -10.0 #Tinfinity2 corresponds to the outer temperature
print "the outer temperature T infinity2 is "+str(Tinfinity2)+ " degrees"
print " "

Ri= {"name":"inner convection","area":0.25,"h":10,"ResValue":0}
R1= {"name":"foam layer","area":0.25,"length":0.03,"k":0.026,"ResValue":0}
R2= {"name":"plaster layer1","area":0.25,"length":0.02,"k":0.22,"ResValue":0}
R3= {"name":"upper horizontal plaster","area":0.015,"length":0.16,"k":0.22,"ResValue":0}
R4= {"name":"brick","area":0.22,"length":0.16,"k":0.72,"ResValue":0}
R5= {"name":"lower horizontal plaster","area":0.015,"length":0.16,"k":0.22,"ResValue":0}
R6= {"name":"plaster layer2","area":0.25,"length":0.02,"k":0.22,"ResValue":0}
Ro= {"name":"outer convection","area":0.25,"h":25,"ResValue":0}

List_Of_Conv_Resist = [Ri,Ro]
ConvResist=0

for anyConvResistance in List_Of_Conv_Resist:

    A_anyConvResistance = anyConvResistance["area"]
    h_anyConvResistance = anyConvResistance["h"]
    RValue_anyConvResistance = 1/(A_anyConvResistance*h_anyConvResistance)
    anyConvResistance["ResValue"] = anyConvResistance["ResValue"] + RValue_anyConvResistance
    ConvResist = ConvResist+anyConvResistance["ResValue"]
    print "here is the new convection resistance: "
    print anyConvResistance
    print "***********"

print " "
print " "
List_Of_Cond_Resist_series = [R1,R2,R6]
CondSeriesResist=0

for anyCondSeriesResist in List_Of_Cond_Resist_series:
    
    L_anyCondSresistance = anyCondSeriesResist["length"]
    A_anyCondSresistance = anyCondSeriesResist["area"]
    K_anyCondSresistance = anyCondSeriesResist["k"]
    RValue_anyCondSresistance = L_anyCondSresistance/(A_anyCondSresistance*K_anyCondSresistance)
    anyCondSeriesResist["ResValue"] = anyCondSeriesResist["ResValue"] + RValue_anyCondSresistance
    CondSeriesResist = CondSeriesResist+anyCondSeriesResist["ResValue"]
    print "here is the new series conduction resistance: "
    print anyCondSeriesResist
    print "***********"
    
print " "
print " "    
List_Of_Cond_Resist_parallel = [R3,R4,R5]
CondParallelResist=0

for anyCondParallelResist in List_Of_Cond_Resist_parallel:

    L_anyCondPresistance = anyCondParallelResist["length"]
    A_anyCondPresistance = anyCondParallelResist["area"]
    K_anyCondPresistance = anyCondParallelResist["k"]
    RValue_anyCondPresistance = L_anyCondPresistance/(A_anyCondPresistance*K_anyCondPresistance)
    anyCondParallelResist["ResValue"] = anyCondParallelResist["ResValue"] + RValue_anyCondPresistance
    CondParallelResist = CondParallelResist+1/anyCondParallelResist["ResValue"]
    print "here is the new Parallel conduction resistance: "
    print anyCondParallelResist
    print "***********"
print" "
print" "
totCondParallelResist = 1/CondParallelResist

Rtot = totCondParallelResist+CondSeriesResist+ConvResist

print "Then, The total thermal resistance of the medium is "+str(Rtot)+ " degrees/W"
print " "
Q= (Tinfinity1-Tinfinity2)/Rtot 
print "This implies that the steady rate of heat transfer through the 0.25 m2 surface area is "+str(Q)+ " W"
print " "
Aw= 3*5 #Aw is the total area of the wall
Qtot= Q*Aw/Ri["area"]
print "Hence, the rate of heat trasnfer through the entire wall becomes "+str(Qtot)+ " W"

