# -*- coding: utf-8 -*-
Ri1 = {"name":"conv1","area":0.25,"convectivity":10}                                  #convectivity 1 
Rf = {"name":"foam","area":0.25,"lenght":0.03,"conductivity":0.026}                   #foam 
Rp1 = {"name":"plaster1","area":0.25,"lenght":0.02,"conductivity":0.22}               #plaster layer 1
Rpc1 = {"name":"horizontalplaster","area":0.015,"lenght":0.16,"conductivity":0.22}    #horizontal plaster layer 1
Rb = {"name":"brick","area":0.22,"lenght":0.16,"conductivity":0.72}                   #brick
Rpc2 = Rpc1                                                                           #horizontal plaster layer 2
Rp2 = Rp1                                                                             #plaster layer 2
Ri2 = {"name":"conv2","area":0.25,"convectivity":25}                                  #convectivity 2


ConductiveResistancesSeries = [Rf,Rp1,Rp2]              #list of resistences in serires
ConductiveResistancesParallel = [Rpc1, Rb, Rpc2]        #list of resistences in parallel
ConvectiveResistances = [Ri1, Ri2]                      #list of convective resistences in serires


ResValue1 = 0
for AnyConductiveResistence in ConductiveResistancesSeries:
    ConductiveResistence = AnyConductiveResistence["lenght"]/(AnyConductiveResistence["area"]*AnyConductiveResistence["conductivity"])
    ResValue1 = ResValue1 + ConductiveResistence
print "The equivalent in series resistence is " + str(ResValue1) + " °C/W"


ResValue = 0
for AnyConductiveResistence in ConductiveResistancesParallel:
    InverseConductiveResistence = (AnyConductiveResistence["conductivity"]*AnyConductiveResistence["area"])/AnyConductiveResistence["lenght"]
    ResValue = ResValue + InverseConductiveResistence
ResParallel = 1/ResValue
print "The equivalent in paralle resistence is " + str(ResParallel) + " °C/W"


ResValue2 = 0
for AnyConventiveResistence in ConvectiveResistances:
    ConvectiveResistence = 1/(AnyConventiveResistence["convectivity"]*AnyConventiveResistence["area"])
    ResValue2 = ConvectiveResistence + ResValue2
print "The equivalent convective resistence is " + str(ResValue2) + " °C/W"


TotalResistence=ResValue1 + ResParallel + ResValue2
print "The total equivalent resistence is " + str(TotalResistence) + " °C/W"


T1=20              #indoor temperature in °C
T2=-10             #outdoor temperature in °C
Awall=3*5          #area of the wall
A1=0.25*1          #front area of a single unit in m2
Qu=(T1-T2)/TotalResistence          
Qwall=Qu*(Awall/A1)

print "The rate of heat transfer across one unit of the wall is " + str(Qu) + " W"
print "The rate of heat transfer across the whole wall is " + str(Qwall) + " W"