# -*- coding: utf-8 -*-
#Convective Resistances
R1 = [0.25,10] #Inner Convective Resistance; Area, h
R2 = [0.25,25] #Outer Convective Resistance; Area, h
#Series Conductive Resistances
R3 = [0.03,0.25,0.026] #Foam Conductive Resistance; Lenght, Area, k
R4 = [0.02,0.25,0.22] #Plaster 1 Conductive Resistance; Lenght, Area, k
R5 = [0.02,0.25,0.22] #Plaster 2 Conductive Resistance; Lenght, Area, k
#Parallel Conductive Resistances
R6 = [0.16,0.015,0.22] #Plaster 3 Conductive Resistance; Lenght, Area, k
R7 = [0.16,0.22,0.72] #Brick Conductive Resistance; Lenght, Area, k
R8 = [0.16,0.015,0.22] #Plaster 4 Conductive Resistance; Lenght, Area, k
#Lists of Resistances
Conv_Res = [R1,R2] #List of convective resistances
Cond_Res_Series = [R3,R4,R5] #List of conductive resistances in series
Cond_Res_Parallel = [R6,R7,R8] #List of conductive resistances in parallel
#Calculating Resistance
#Convective
print "Calculating Convective Resistance"
Tot_convres = 0
for anyres in Conv_Res:
    print "New Convective Resistance "
    print anyres
    A_anyres = anyres[0]
    h_anyres = anyres[1]
    Res = 1/(A_anyres*h_anyres)
    Tot_convres = Tot_convres+Res
    print "The calculated convective resistance is "+str(Res)+" °C/W"
    print "***************************************"
print "The total convective resistance is "+str(Tot_convres)+" °C/W"
print "************************************************************"
print "************************************************************"
#Conductive Series
print "Now let's calculate conductive resistance in series"
Tot_condseries = 0
for anyres in Cond_Res_Series:
    print "New Conductive Resistance"
    print anyres
    L_anyres = anyres[0]
    A_anyres = anyres[1]
    k_anyres = anyres[2]
    Res = L_anyres/(A_anyres*k_anyres)
    Tot_condseries = Tot_condseries+Res
    print "The calculated conductive resistance is "+str(Res)+" °C/W"
    print "***************************************"
print "The total conductive resistance in series is "+str(Tot_condseries)+" °C/W"
print "************************************************************"
print "************************************************************"
#Conductive Parallel
print "Now let's calculate conductive resistance in parallel"
Sum_condpar = 0
Tot_condpar = 0
for anyres in Cond_Res_Parallel:
    print "New conductive resistance is "
    print anyres
    L_anyres = anyres[0]
    A_anyres = anyres[1]
    k_anyres = anyres[2]
    Res = L_anyres/(A_anyres*k_anyres)
    Sum_condpar = Sum_condpar+(1/Res)
    print "The calculated conductive resistance is "+str(Res)+" °C/W"
    print "**********************************************************"
Tot_condpar = Tot_condpar+(1/Sum_condpar)
print "The total conductive resistance in parallel is "+str(Tot_condpar)+" °C/W"
print "************************************************************"
print "************************************************************"
Total_Resistance = Tot_convres+Tot_condseries+Tot_condpar
print "The total resistance is "+str(Total_Resistance)+" °C/W"
#Calculating heat exchanged
T1 = 20
T2 = -10
A_unit = 0.25
A_tot = 15
Q_unit = (T1-T2)/Total_Resistance
Q_wall = Q_unit*(A_tot/A_unit)
print "************************************************************"
print "************************************************************"
print "The total heat flux through the wall is "+str(Q_wall)+" W"