# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146
"""

import pandas as pd

# List and calculations of resistances

R1_list = ["conv",10,None,None, 0.25 ,0]
R2_list = ["cond",None,0.026,0.03, 0.25 ,0]
R3_list = ["cond",None,0.22,0.02, 0.25 ,0]
R4_list = ["cond",None,0.22,0.16, 0.015 ,0]
R5_list = ["cond",None,0.72,0.16, 0.22 ,0]
R6_list = ["conv",25,None,None, 0.25 ,0]

Resistances_Names = ["indoor","foam","side plaster","center plaster","brick","outdoor"]
Columns_Names=["type","h","k","L","A","RValue"]

Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list],index=Resistances_Names,columns=Columns_Names)


Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/(Resistances_DF["h"][Resistances_DF["type"]=="conv"]*Resistances_DF["A"][Resistances_DF["type"]=="conv"])
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"][Resistances_DF["type"]=="cond"]/(Resistances_DF["k"][Resistances_DF["type"]=="cond"]*Resistances_DF["A"][Resistances_DF["type"]=="cond"])

print "------------------------------------------------------------"
print "------------------------------------------------------------"
print Resistances_DF

Tot_R_Series = Resistances_DF.loc["indoor","RValue"] + Resistances_DF.loc["foam","RValue"] + 2 * Resistances_DF.loc["side plaster","RValue"] + Resistances_DF.loc["outdoor","RValue"]
Tot_R_Parallel =  1/(2/Resistances_DF.loc["center plaster","RValue"] + 1/ Resistances_DF.loc["brick","RValue"])

R_Wall_Unit = Tot_R_Parallel+Tot_R_Series

print "------------------------------------------------------------"
print "------------------------------------------------------------"
print " Resistance of the unit of the wall = " + str(round(R_Wall_Unit,4)) + " K/W"

# Heat transfer rate
T_in = 20  # [°C]
T_out = -10  # [°C]

Area_Unit = 1*0.25  # [m2]
Q_Unit = (T_in - T_out)/R_Wall_Unit  # [W]

Area_Wall = 3 * 5  # [m2]
Q_Wall =  Q_Unit * (Area_Wall/Area_Unit)  # [W]

print "\n Heat transfer rate = " + str(round(Q_Wall,4)) + " W"
print "------------------------------------------------------------"
print "------------------------------------------------------------"
