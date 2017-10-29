# -*- coding: utf-8 -*-
#              Assigment 2 Calculation of the example D using list

print "Assigment 2 Calculation of the example D using list\n"

#  Parameters

#Convention resistance [Heat transfer coefficient, area]

R1in=[10,0.25]#Resistance for convection of of foam layer
R8out=[25,0.25]#Resistance for convection of of plaster layer

TConv=0#Variable for the total of convenction resistances
ListRConv=[R1in,R8out]#List with lists of the convenction resistances

for res in ListRConv:
    k=res[0]#assignation of conductivity
    A=res[1]#assiganation of area
    Rconv= 1/(k*A)#calculation of the convenction resistance
    TConv+=Rconv#calculation of the total convenction resistances
print "The total convenction resistance is ",TConv,"ºC/W \n"

#Conduction resistances in series [Length, conductivity, area]

R2=[0.03,0.026,0.25]# Resistance of conduction of the foam
R3=[0.02,0.22,0.25]# Resistance of conduction of the vertical plaster
R7=R3#Resistance for the second vertical plaster

TCondS=0#Variable for the total of conduction resistances in series
ListRCondS=[R2,R3,R7]#List with lists of the convenction resistances in series
for res in ListRCondS:
    L=res[0]#assiganation of length
    k=res[1]#assignation of conductivity
    A=res[2]#assiganation of area
    Rcond=L/(k*A)#calculation of the conduction resistance
    TCondS+=Rcond#calculation of the total conduction resistances in series
print "The total conduction resistance in series is ",TCondS,"ºC/W \n"

#Conduction resistances in parallel [Length, conductivity, area]

R4=[0.16,0.22,0.015]# Resistance of conduction of the horizontal plaster
R5=R4# Resistance of conduction of second horizontal plaster
R6air=[0.16,0.72,0.22]# Resistance of conduction of air gap on the brick

TCondP=0#Variable for the total of conduction resistances in parallel
ListRCondP=[R4,R5,R6air]#List with lists of the convenction resistances in parallel
for res in ListRCondP:
    L=res[0]#assiganation of length
    k=res[1]#assignation of conductivity
    A=res[2]#assiganation of area
    Rcond=1/(L/(k*A))#calculation of the conduction resistance
    TCondP+=Rcond#calculation of the total conduction resistances in parallel
TCondP=1/TCondP
print "The total conduction resistance in parallel is ",TCondP,"ºC/W \n"

# Total thermal resistance of the wall 
Rtotal=TConv+TCondS+TCondP# The total resistance
print "The total thermal resistance is ",Rtotal,"ºC/W \n"
#           Calculation of the heat transfer of the wall
#
wall=[20,-10,3,5,0.25]#wall inputs [Temperature in, Temperature out, high, wide, area ]
Qb=(wall[0]-wall[1])/Rtotal# Rate of heat transfer of one brick in [W]
Nb=(wall[2]*wall[3])/wall[4]# Number of bricks in the wall
Qtotal=Qb*Nb# Rate of heat tranfer of the wall in [W]
#
print "The heat transfer through the wall is "+str(Qtotal)+" W"