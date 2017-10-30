# -*- coding: utf-8 -*-
#EXERCISE 6

#EXAMPLE D: HEAT LOSS THROUGH A COMPOSITE WALL

#SERIES CALCULATIONS
import pandas as pd

#Resistances in Series 
R1_list = ["conv", "series", 10, None, None, 0.25, 0]
R2_list = ["cond", "series", None, 0.026, 0.03, 0.25, 0]
R3_list = ["cond",  "series",None, 0.22, 0.02, 0.25, 0]
R4_list = ["cond",  "series",None, 0.22, 0.02, 0.25, 0]
R5_list = ["cond", "parallel", None, 0.72, 0.16, 0.22, 0]
R6_list = ["cond", "parallel", None, 0.22, 0.16, 0.015, 0]
R7_list = ["cond", "parallel", None, 0.22, 0.16, 0.015, 0]
R8_list = ["conv", "series", 25, None, None, 0.25, 0]

columns_names = ["type", "circuit", "h", "k", "L", "area", "Rvalue"]
resistances_names = ["Conv_In","Foam","Plaster_S1","PlasterS2","Brick", "Plaster_P1","Plaster_P2", "Conv_Out"]
Resistances = pd.DataFrame ([R1_list, R2_list, R3_list, R4_list, R5_list, R6_list, R7_list, R8_list], index= resistances_names, columns = columns_names)

Resistances["Rvalue"][Resistances["type"]=="cond"] = (Resistances["L"])/(Resistances["k"]*Resistances["area"])
Resistances["Rvalue"][Resistances["type"]=="conv"]= 1.0/(Resistances["h"]*Resistances["area"])

RSeries_Tot = Resistances["Rvalue"][Resistances["circuit"]=="series"].sum()
RParallel_Tot = (1/Resistances["Rvalue"][Resistances["circuit"]=="parallel"]).sum()


print Resistances 
print "\nThe conductive resistance in series is "+str(RSeries_Tot)+" °C/W"
print "The conductive resistance in parallel is "+str(1/RParallel_Tot)+" °C/W \n"


TOT_RES = (RSeries_Tot)+(1/RParallel_Tot)

print "So, the TOTAL RESISTANCE is "+str(TOT_RES)+" °C/W" 

print"******************************************************"  
print"******************************************************"  

print "Now, let's calculate the heat flux loss of the wall..."

T1=20
T2 = -10

Q_unit = (T1-T2)/TOT_RES
print"The heat transfer loss per unit "+str(Q_unit)+" W/unit"

print"....." 
print"....." 

print "Assuming a wall of 3 m of high and 5 m of wide... "
H_w = 3 # High of wall in m
W_w = 5 # Wide of wall in m
A = 0.25 

A_wall = H_w*W_w
Q_wall = Q_unit*A_wall/A
print "The TOTAL HEAT LOSS of the composite wall is "+str(Q_wall)+ " W"