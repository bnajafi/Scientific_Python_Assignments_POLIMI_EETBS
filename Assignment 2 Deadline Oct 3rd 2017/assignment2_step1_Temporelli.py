# -*- coding: utf-8 -*-
#assignment2_step1_Temporelli

#wall
H_wall = 5
W_wall = 3
W_wall= float(W_wall)
A_wall = H_wall*W_wall

#unit
H_unit = 0.25
W_unit = 1
A_unit = H_unit*W_unit

#conductive resistances in series (foam, plaster 1, plaster 2)
R_f = [0.25,0.03,0.026]
R_p1 = [0.25,0.02,0.22]
R_p2 = [0.25,0.02,0.22]
ListOfCondSeriesResistances = [R_f,R_p1,R_p2]
TotalCondSeriesResValues=0
for anyResistance in ListOfCondSeriesResistances:
    print "here is the new list of parameters of the resistance"
    print anyResistance
    L_anyResistance=anyResistance[1]
    A_anyResistance=anyResistance[0]
    k_anyResistance=anyResistance[2]
    RValue_anyResistance=L_anyResistance/(A_anyResistance*k_anyResistance)
    TotalCondSeriesResValues=TotalCondSeriesResValues+RValue_anyResistance
    print "so the calculated resistance is: " +str(RValue_anyResistance)
    print "**********"
    
print "The total conductive resistance of the resistances in series is "+str(TotalCondSeriesResValues) + " °C/W"

#conductive resistances in parallel (brick, plaster layer 1, plaster layer 2) 

R_b = [0.22,0.16,0.72]
R_pl1 = [0.015,0.16,0.22]
R_pl2 = [0.015,0.16,0.22]  

ListOfCondParallelResistances = [R_b,R_pl1,R_pl2]
TotalCondParallelResValues=0
for anyResistance in ListOfCondParallelResistances:
    print "here is the new list of parameters of the resistance"
    print anyResistance
    L_anyResistance=anyResistance[1]
    A_anyResistance=anyResistance[0]
    k_anyResistance=anyResistance[2]
    RValue_anyResistance=(L_anyResistance/(A_anyResistance*k_anyResistance))**-1
    TotalCondParallelResValues=TotalCondParallelResValues+RValue_anyResistance
    print "so the calculated resistance is: " +str(RValue_anyResistance)
    print "**********"
    
print "The total conductive resistance of the resistances in parallel is "+str(TotalCondParallelResValues**-1)+" °C/W" 

#convective resistanes (R_i, R_o)

R_i = [0.25,10]
R_o = [0.25,25]

ListOfConvectiveResistances = [R_i,R_o]
TotalConvectiveResValues=0
for anyResistance in ListOfConvectiveResistances:
    print "here is the new list of parameters of the resistance"
    print anyResistance
    A_anyResistance=anyResistance[1]
    h_anyResistance=anyResistance[0]
    RValue_anyResistance=(1/(A_anyResistance*h_anyResistance))
    TotalConvectiveResValues=TotalConvectiveResValues+RValue_anyResistance
    print "so the calculated resistance is: " +str(RValue_anyResistance)
    print "**********"
    
print "The total convective resistance is "+str(TotalConvectiveResValues)+" °C/W" 

R_tot = TotalCondSeriesResValues +  TotalCondParallelResValues**-1  +   TotalConvectiveResValues

print " The total resistance is "+str(R_tot)+" °C/W"

#Heat transfer (unit)

T_i = 20
T_o = -10
Q_unit = (T_i-T_o)/R_tot

#Heat transfer (wall)
Q_wall = Q_unit*A_wall/A_unit


print "the heat transfer through the unit results: " + str(Q_unit) + "W"
print "the heat transfer through the wall results: " + str(Q_wall) + "W"
