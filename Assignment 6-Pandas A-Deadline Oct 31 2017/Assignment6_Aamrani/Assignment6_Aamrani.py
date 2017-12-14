# -*- coding: utf-8 -*-

import pandas as pd


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
Rtot = (RSeries_Tot)+(1/RParallel_Tot)

print "Thus the total resistance is equal to"+str(Rtot)+"°C/W" 



T1=20
T2 = -10

A = 0.25 

Q = (T1-T2)*A/(Rtot/4)
print "The total exchanged heat is "+str(Q)+ " W"