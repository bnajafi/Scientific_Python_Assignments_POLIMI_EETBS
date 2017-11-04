# -*- coding: utf-8 -*-
#Second assignment - Step 2

#Data, layers:

layer_1={'k':0.026, 'L':0.03, 'A':0.25}    #foam layer: k conductivity [W/m/°C], L thickness [m], A area of the unit [m**2]
layer_2={'k':0.22, 'L':0.02, 'A':0.25}     #1st vertical plaster layer
layer_3=layer_2                            #2nd vertical plaster layer
layer_4={'k':0.22, 'L':0.16, 'A':0.015}    #1st horizontal plaster layer
layer_5={'k':0.72, 'L':0.16, 'A':0.22}     #brick layer
layer_6=layer_4                            #2nd horizontal plaster layer
conv_1={'h':10, 'A':0.25}                  #internal convection: h convection coefficient [W/m**2], A area of the unit [m**2]
conv_2={'h':25, 'A':0.25}                  #external convection


#Conductive Resistance in series:

ListResSeries = [layer_1, layer_2, layer_3]    #list of conductive layers in series
totResSeries= 0
for anyResistance in ListResSeries:
    print "Here are the characteristics of the layer:"
    print anyResistance
    k_anyResistance = anyResistance['k']         #conductivity of the i-th layer
    L_anyResistance = anyResistance['L']         #thickness of the i-th layer
    A_anyResistance = anyResistance['A']         #area of the i-th layer
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
    k_anyResistance = anyResistance['k']         #conductivity of the i-th layer
    L_anyResistance = anyResistance['L']         #thickness of the i-th layer
    A_anyResistance = anyResistance['A']         #area of the i-th layer
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
    h_anyResistance = anyResistance['h']         #convection coefficient of the surface
    A_anyResistance = anyResistance['A']         #area of the surface
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