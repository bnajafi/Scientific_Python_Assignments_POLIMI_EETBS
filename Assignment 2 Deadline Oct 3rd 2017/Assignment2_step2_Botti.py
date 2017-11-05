# -*- coding: utf-8 -*-
#Convective Resistances
R1 = {"name":"Inner Convective Resistance","Area":0.25,"h":10,"resvalue":0} 
R2 = {"name":"Outer Convective Resistance","Area":0.25,"h":25,"resvalue":0} 
#Series Conductive Resistances
R3 = {"name":"Foam Conductive Resistance","Lenght":0.03,"Area":0.25,"k":0.026,"resvalue":0}
R4 = {"name":"Plaster1 Conductive Resistance","Lenght":0.02,"Area":0.25,"k":0.22,"resvalue":0}
R5 = {"name":"Plaster2 Conductive Resistance","Lenght":0.02,"Area":0.25,"k":0.22,"resvalue":0}
#Parallel Conductive Resistances
R6 = {"name":"Plaster3 Conductive Resistance","Lenght":0.16,"Area":0.015,"k":0.22,"resvalue":0}
R7 = {"name":"Brick Conductive Resistance","Lenght":0.16,"Area":0.22,"k":0.72,"resvalue":0}
R8 = {"name":"Plaster4 Conductive Resistance","Lenght":0.16,"Area":0.015,"k":0.22,"resvalue":0}
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
    A_anyres = anyres["Area"]
    h_anyres = anyres["h"]
    name_anyres = anyres["name"]
    Res = 1/(A_anyres*h_anyres)
    anyres["resvalue"] = Res
    Tot_convres = Tot_convres+Res
    print "The calculated "+name_anyres+" is "+str(Res)+" °C/W"
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
    L_anyres = anyres["Lenght"]
    A_anyres = anyres["Area"]
    k_anyres = anyres["k"]
    name_anyres = anyres["name"]
    Res = L_anyres/(A_anyres*k_anyres)
    anyres["resvalue"] = Res
    Tot_condseries = Tot_condseries+Res
    print "The calculated "+name_anyres+" is "+str(Res)+" °C/W"
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
    L_anyres = anyres["Lenght"]
    A_anyres = anyres["Area"]
    k_anyres = anyres["k"]
    name_anyres = anyres["name"]
    Res = L_anyres/(A_anyres*k_anyres)
    anyres["resvalue"] = Res
    Sum_condpar = Sum_condpar+(1/Res)
    print "The calculated "+name_anyres+" is "+str(Res)+" °C/W"
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