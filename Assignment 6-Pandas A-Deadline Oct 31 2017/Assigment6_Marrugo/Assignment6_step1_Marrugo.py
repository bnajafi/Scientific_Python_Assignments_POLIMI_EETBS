# -*- coding: utf-8 -*-
#     Assigment 6 Calculation of the example D using pandas

print "Assigment 5 Calculation of the example D using pandas\n"

#  import library

import pandas as pd

#Convention resistance [Heat transfer coefficient, area]

Resistances_names=["R1in","R2","R3","R4","R5","R6","R7","R8out"]#Resistances names of the wall
Resistances_columns=["Type","Config","L","H","K","A","RValue"]

# Definition of resistances
R1in=["conv","Series",None,10,None,0.25,0]
R2=["cond","Series",0.03,None,0.026,0.25,0]
R3=["cond","Series",0.02,None,0.22,0.25,0]
R4=["cond","Parallel",0.16,None,0.22,0.015,0]
R5=["cond","Parallel",0.16,None,0.22,0.015,0]
R6=["cond","Parallel",0.16,None,0.72,0.22,0]
R7=["cond","Series",0.02,None,0.22,0.25,0]
R8out=["conv","Series",None,25,None,0.25,0]

#Creation of a 2D array
Resistances_Df=pd.DataFrame([R1in,R2,R3,R4,R5,R6,R7,R8out],index=Resistances_names,columns=Resistances_columns)


#Resistances_RValues= np.array(np.zeros(8))# Variable for store the resistances values
#Calculation of the conductive resistances
Resistances_Df["RValue"][Resistances_Df["Type"]=="cond"] = (Resistances_Df["L"][Resistances_Df["Type"]=="cond"])/((Resistances_Df["K"][Resistances_Df["Type"]=="cond"])*(Resistances_Df["A"][Resistances_Df["Type"]=="cond"]))
#Calculation of the convective resistances
Resistances_Df["RValue"][Resistances_Df["Type"]=="conv"] = 1.0 / ((Resistances_Df["A"][Resistances_Df["Type"]=="conv"])*(Resistances_Df["H"][Resistances_Df["Type"]=="conv"]))
#Total convection resistance
Resistances_convection=Resistances_Df["RValue"][Resistances_Df["Type"]=="conv"].sum()
#Total conduction resistances in series
Resistances_Series_conduction=(Resistances_Df["RValue"][Resistances_Df["Config"]=="Series"][Resistances_Df["Type"]=="cond"].sum())
#Calculation of the parallel resistances
Resistances_Df["RValue"][Resistances_Df["Config"]=="Parallel"]=1/(Resistances_Df["RValue"][Resistances_Df["Config"]=="Parallel"])
#Total conduction resistances in parallel
Resistances_Parallel_conduction=1/(Resistances_Df["RValue"][Resistances_Df["Config"]=="Parallel"].sum())
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
