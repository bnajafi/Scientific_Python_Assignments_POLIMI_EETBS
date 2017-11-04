# -*- coding: utf-8 -*-
#Second assignment - Step 1

#Data, layers:

layer_1=[0.026, 0.03, 0.25]    #foam layer: (0) conductivity [W/m/°C], (1) thickness [m], (2) area of the unit [m**2]
layer_2=[0.22, 0.02, 0.25]     #1st vertical plaster layer
layer_3=layer_2                #2nd vertical plaster layer
layer_4=[0.22, 0.16, 0.015]    #1st horizontal plaster layer
layer_5=[0.72, 0.16, 0.22]     #brick layer
layer_6=layer_4                #2nd horizontal plaster layer
conv_1=[10, 0.25]              #internal convection: (0) convection coefficient [W/m**2], (1) area of the unit [m**2]
conv_2=[25, 0.25]              #external convection


#Conductive Resistance in series:

ListResSeries = [layer_1, layer_2, layer_3]    #list of conductive layers in series
totResSeries= 0
for anyResistance in ListResSeries:
    print "Here are the characteristics of the layer:"
    print anyResistance
    k_anyResistance = anyResistance[0]         #conductivity of the i-th layer
    L_anyResistance = anyResistance[1]         #thickness of the i-th layer
    A_anyResistance = anyResistance[2]         #area of the i-th layer
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)      #resistance of the i-th layer
    totResSeries = totResSeries+RValue_anyResistance                            #total conductive resistance in series 
    print "The calculated resistance of this layer is: "+str(RValue_anyResistance) + " °C/W."
    print "°°°°°°°°°°°°°°°°"
print "The total conductive resistance in series is: "+str(totResSeries) + " °C/W."
print "*******************"


#Conductive Resistance in parallel:

ListResParallel = [layer_4, layer_5, layer_6]    #list of conductive layers in parallel
totResParallel= 0
for anyResistance in ListResParallel:
    print "Here are the characteristics of the layer:"
    print anyResistance
    k_anyResistance = anyResistance[0]         #conductivity of the i-th layer
    L_anyResistance = anyResistance[1]         #thickness of the i-th layer
    A_anyResistance = anyResistance[2]         #area of the i-th layer
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)      #resistance of the i-th layer
    print "The calculated resistance of this layer is: "+str(RValue_anyResistance) + " °C/W."
    print "°°°°°°°°°°°°°°°°"
    totResParallel = totResParallel + 1/RValue_anyResistance                         
totResParallel= totResParallel**(-1)             #total conductive resistance in parallel
print "The total conductive resistance in parallel is: "+str(totResParallel) + " °C/W."
print "*******************"


#Convective Resistance:

ListResConv = [conv_1, conv_2]    #list of convective surfaces
totResConv= 0
for anyResistance in ListResConv:
    print "Here are the characteristics of the surface:"
    print anyResistance
    h_anyResistance = anyResistance[0]         #convection coefficient of the surface
    A_anyResistance = anyResistance[1]         #area of the surface
    RValue_anyResistance = 1/(A_anyResistance*h_anyResistance)      #resistance of the surface
    print "The calculated resistance of this surface is: "+str(RValue_anyResistance) + " °C/W."
    print "°°°°°°°°°°°°°°°°"
    totResConv = totResConv + RValue_anyResistance            #total convective resistance             
print "The total convective resistance is: "+str(totResConv) + " °C/W."
print "*******************"


#Total resistance:

TotRes=totResSeries+totResParallel+totResConv
print "The total resistance of the wall is: "+str(TotRes) + " °C/W."
print "*******************"


#Heat flux through the area unit:

T_in=20     #inner temperature [°C]
T_out=-10   #outer temperature
Q_unit=(T_in-T_out)/TotRes
print "The heat flux through the area unit is: "+str(Q_unit) + " W."
print "*******************"


#Heat flux through the whole wall:

A_tot=15       #total area of the wall [m**2]
A_unit=0.25    #area of the unit
Q_tot=Q_unit*A_tot/A_unit      #total heat flux
print "The heat flux through the whole wall is: "+str(Q_tot) + " W."