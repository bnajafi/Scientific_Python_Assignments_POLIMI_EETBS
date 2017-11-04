# -*- coding: utf-8 -*-
#     Assigment 5 Calculation of the example D using numpy

print "Assigment 5 Calculation of the example D using numpy\n"

#  import library

import numpy as np

#Convention resistance [Heat transfer coefficient, area]

Resistances_names=np.array(["R1in","R2","R3","R4","R5","R6","R7","R8out"])#Resistances names of the wall
Resistances_types=np.array(["conv","cond","cond","cond","cond","cond","cond","conv"])#Types resistances of the wall
Resistances_config=np.array(["Series","Serie","Serie","Parallel","Parallel","Parallel","Serie","Series"])#Configuration of the resistances on the wall

Resistances_L=np.array([None,0.03,0.02,0.16,0.16,0.16,0.02,None])# length of the resistances
Resistances_H=np.array([10,None,None,None,None,None,None,25])# Conduction coefficient
Resistances_K=np.array([None,0.026,0.22,0.22,0.22,0.72,0.22,None])# Conduction coefficient
Resistances_A=np.array([0.25,0.25,0.25,0.015,0.015,0.22,0.25,0.25])# Areas for the resistances 

Resistances_RValues= np.array(np.zeros(8))# Variable for store the resistances values
#Calculation of the conductive resistances
Resistances_RValues[Resistances_types=="cond"] = Resistances_L[Resistances_types=="cond"]/ (Resistances_K[Resistances_types=="cond"]*Resistances_A[Resistances_types=="cond"])
#Calculation of the convective resistances
Resistances_RValues[Resistances_types=="conv"] = 1.0 / (Resistances_A[Resistances_types=="conv"]*Resistances_H[Resistances_types=="conv"])
#Total convection resistance
Resistances_convection=Resistances_RValues[Resistances_types=="conv"].sum()
#Total conduction resistances in series
Resistances_Series_conduction=Resistances_RValues[Resistances_config=="Serie"].sum()
#Calculation of the parallel resistances
Resistances_RValues[Resistances_config=="Parallel"]=1/(Resistances_RValues[Resistances_config=="Parallel"])
#Total conduction resistances in parallel
Resistances_Parallel_conduction=1/(Resistances_RValues[Resistances_config=="Parallel"].sum())
#Total resistance
R_total=Resistances_Series_conduction + Resistances_Parallel_conduction + Resistances_convection

wall=[20,-10,3,5,0.25]#wall inputs [Temperature in, Temperature out, high, wide, area ]
Qb=(wall[0]-wall[1])/R_total# Rate of heat transfer of one brick in [W]
Nb=(wall[2]*wall[3])/wall[4]# Number of bricks in the wall
Qtotal=Qb*Nb# Rate of heat tranfer of the wall in [W]

print "The total convenction resistance is ",Resistances_convection,"ºC/W \n"
print "The total conduction resistance in series is ",Resistances_Series_conduction,"ºC/W \n"
print "The total conduction resistance in parallel is ",Resistances_Parallel_conduction,"ºC/W \n"
print "The total thermal resistance is ",R_total,"ºC/W \n"
print "The heat transfer through the wall is "+str(Qtotal)+" W"
