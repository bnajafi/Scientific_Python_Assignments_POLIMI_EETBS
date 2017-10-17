# -*- coding: utf-8 -*-
#              Assigment 2 Calculation of the example D using dictionary

print "Assigment 2 Calculation of the example D using dictionary\n"

#  Parameters

#Convention resistance [Heat transfer coefficient, area]
R1={"name": "R_In_foam","conductivity":10,"area":0.25,"Resvalue":0}#Resistance for convection of of foam layer
R8={"name": "R_Out_plaster","conductivity":25,"area":0.25,"Resvalue":0}#Resistance for convection of of plaster layer

TConv=0#Variable for the total of convenction resistances
ListRConv=[R1,R8]#List with the dictionaries of the convenction resistances

for res in ListRConv:
    k=res["conductivity"]#assignation of conductivity
    A=res["area"]#assiganation of area
    Rconv= 1/(k*A)#calculation of the convenction resistance
    TConv+=Rconv#calculation of the total convenction resistances
    res["Resvalue"]=Rconv#store the resistance value
    print "the resistance ",res["name"],"has a value of ",Rconv,"ºC/W \n"
print "The total convenction resistance is ",TConv,"ºC/W \n"

#Conduction resistances in series [Length, conductivity, area]
R2={"name": "R_Foam","Length":0.03,"conductivity":0.026,"area":0.25,"Resvalue":0}# Resistance of conduction of the foam
R3={"name": "R_vertical_Plaster","Length":0.02,"conductivity":0.22,"area":0.25,"Resvalue":0}# Resistance of conduction of the vertical plaster
R7=R3#Resistance for the second vertical plaster

TCondS=0#Variable for the total of conduction resistances in series
ListRCondS=[R2,R3,R7]#List with the dictironaries of the convenction resistances in series
for res in ListRCondS:
    L=res["Length"]#assiganation of length
    k=res["conductivity"]#assignation of conductivity
    A=res["area"]#assiganation of area
    Rcond=L/(k*A)#calculation of the conduction resistance
    TCondS+=Rcond#calculation of the total conduction resistances in series
    res["Resvalue"]=Rcond#store the resistance value
    print "the resistance ",res["name"],"has a value of ",Rcond,"ºC/W \n"
print "The total conduction resistance in series is ",TCondS,"ºC/W \n"

#Conduction resistances in parallel [Length, conductivity, area]
R4={"name": "R_Horizontal_Plaster","Length":0.16,"conductivity":0.22,"area":0.015,"Resvalue":0}# Resistance of conduction of the horizontal plaster
R5=R4# Resistance of conduction of second horizontal plaster
R6={"name": "R_Air_Gap","Length":0.16,"conductivity":0.72,"area":0.22,"Resvalue":0}# Resistance of conduction of air gap on the brick

TCondP=0#Variable for the total of conduction resistances in parallel
ListRCondP=[R4,R5,R6]#List with lists of the convenction resistances in parallel
for res in ListRCondP:
    L=res["Length"]#assiganation of length
    k=res["conductivity"]#assignation of conductivity
    A=res["area"]#assiganation of area
    Rcond=1/(L/(k*A))#calculation of the conduction resistance
    TCondP+=Rcond#calculation of the total conduction resistances in parallel
    res["Resvalue"]=Rcond#store the resistance value
    print "the resistance ",res["name"],"has a value of ",Rcond,"ºC/W \n"
TCondP=1/TCondP
print "The total conduction resistance in parallel is ",TCondP,"ºC/W \n"

# Total thermal resistance of the wall 
Rtotal=TConv+TCondS+TCondP# The total resistance
print "The total thermal resistance is ",Rtotal,"ºC/W \n"

#           Calculation of the heat transfer of the wall
#
wall={"name":"wall","Tin":20,"Tout":-10,"High":3,"wide":5,"Area":0.25}#wall inputs [Temperature in, Temperature out, high, wide, area ]
Qb=(wall["Tin"]-wall["Tout"])/Rtotal# Rate of heat transfer of one brick in [W]
Nb=(wall["High"]*wall["wide"])/wall["Area"]# Number of bricks in the wall
Qtotal=Qb*Nb# Rate of heat tranfer of the wall in [W]
#
print "The heat transfer through the wall is "+str(Qtotal)+" W"
