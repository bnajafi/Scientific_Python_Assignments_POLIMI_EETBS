print "At first, we're going to calculate the rate of heat transfer through a unit of 0.25m high and 1m deep"
print " "
print "In order to do that, we should first calculate the thermal resistance of each medium and then the total thermal resistance of the whole medium"
print " "

Ri= {"name":"inner convection","area":0,"h":0,"ResValue":0}
R1= {"name":"foam layer","area":0,"length":0,"k":0,"ResValue":0}
R2= {"name":"vertical plaster layer1","area":0,"length":0,"k":0,"ResValue":0}
R3= {"name":"upper horizontal plaster layer","area":0,"length":0,"k":0,"ResValue":0}
R4= {"name":"brick","area":0,"length":0,"k":0,"ResValue":0}
R5= {"name":"lower horizontal plaster layer","area":0,"length":0,"k":0,"ResValue":0}
R6= {"name":"vertical plaster layer2","area":0,"length":0,"k":0,"ResValue":0}
Ro= {"name":"outer convection","area":0,"h":0,"ResValue":0}


List_Of_Conv_Resist = [Ri,Ro]
ConvResist=0

for anyConvResistance in List_Of_Conv_Resist:

    print "The name of the convection resistive layer is "+str(anyConvResistance["name"])
    print " "
    A_anyConvResistance = float(raw_input("please enter the surface area of this layer in m^2:    "))
    anyConvResistance["area"]=A_anyConvResistance+anyConvResistance["area"]
    print " "
    h_anyConvResistance = float(raw_input("please enter the heat trasnfer convection coefficient of this layer in W/m^2.degC:    "))
    anyConvResistance["h"]=h_anyConvResistance+anyConvResistance["h"]
    print " "
    RValue_anyConvResistance = 1/(A_anyConvResistance*h_anyConvResistance)
    anyConvResistance["ResValue"]=anyConvResistance["ResValue"]+RValue_anyConvResistance
    ConvResist = ConvResist+anyConvResistance["ResValue"]
    print anyConvResistance
    print "***********"
    
print " "
print " "


List_Of_Cond_Resist_series = [R1,R2,R6]
CondSeriesResist=0

for anyCondSeriesResist in List_Of_Cond_Resist_series:
    
    print "The name of the series conduction resistive layer is "+str(anyCondSeriesResist["name"])
    print " "
    L_anyCondSresistance = float(raw_input("please enter the thickness of this layer in m:    "))
    anyCondSeriesResist["length"]=L_anyCondSresistance+anyCondSeriesResist["length"]
    print " "
    A_anyCondSresistance = float(raw_input("please enter the surface area of this layer in m^2:    "))
    anyCondSeriesResist["area"]=A_anyCondSresistance+anyCondSeriesResist["area"]
    print " "
    K_anyCondSresistance = float(raw_input("please enter the heat trasnfer conduction coefficient of this layer in W/m.degC:    "))
    anyCondSeriesResist["k"]=K_anyCondSresistance+anyCondSeriesResist["k"]
    print " "
    RValue_anyCondSresistance = L_anyCondSresistance/(A_anyCondSresistance*K_anyCondSresistance)
    anyCondSeriesResist["ResValue"]=anyCondSeriesResist["ResValue"]+RValue_anyCondSresistance
    CondSeriesResist = CondSeriesResist+anyCondSeriesResist["ResValue"]
    print anyCondSeriesResist
    print "***********"
    
print " "
print " " 

  
List_Of_Cond_Resist_parallel = [R3,R4,R5]
CondParallelResist=0

for anyCondParallelResist in List_Of_Cond_Resist_parallel:
    
    print "The name of the parallel conduction resistive layer is "+str(anyCondParallelResist["name"])
    print " "
    L_anyCondPresistance = float(raw_input("please enter the thickness of this layer in m:    "))
    anyCondParallelResist["length"]=L_anyCondPresistance+anyCondParallelResist["length"]
    print " "
    A_anyCondPresistance = float(raw_input("please enter the surface area of this layer in m^2:    "))
    anyCondParallelResist["area"]=A_anyCondPresistance+anyCondParallelResist["area"]
    print " "
    K_anyCondPresistance = float(raw_input("please enter the heat trasnfer coefficient of this layer in W/m.degC:    "))
    anyCondParallelResist["k"]=K_anyCondPresistance+anyCondParallelResist["k"]
    print " "
    RValue_anyCondPresistance = L_anyCondPresistance/(A_anyCondPresistance*K_anyCondPresistance)
    anyCondParallelResist["ResValue"]=anyCondParallelResist["ResValue"]+RValue_anyCondPresistance
    CondParallelResist = CondParallelResist+1/anyCondParallelResist["ResValue"]
    print anyCondParallelResist
    print "***********"
print" "
print" "
totCondParallelResist = 1/CondParallelResist



Rtot = totCondParallelResist+CondSeriesResist+ConvResist


print "Then, The total thermal resistance of the medium is "+str(Rtot)+ " degC/W"
print " "
print "in order to calculate the rate of heat trasnfer of the 0.25 m^2 unit you need to enter the inner and outer temperature"
print " "
Tinfinity1 = float(raw_input("please enter the temperature of the inner side in degC:    "))
Tinfinity2 = float(raw_input("please enter the temperature of the outer side in degC:    "))
print " "
Q= (Tinfinity1-Tinfinity2)/Rtot 
print "so the steady rate of heat transfer through the 0.25 m^2 surface area is "+str(Q)+ " W"
print " "
Aw = float(raw_input("please enter the surface area of the wall in m^2 in order to calculate the rate of heat trasnfer through the wall:   "))
print " "
Qtot= Q*Aw/Ri["area"]
print "Hence, the rate of heat trasnfer through the entire wall becomes "+str(Qtot)+ " W"
