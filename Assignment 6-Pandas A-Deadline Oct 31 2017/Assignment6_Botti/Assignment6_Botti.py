# -*- coding: utf-8 -*-
import pandas as pd
# Definition of list of Resistances
R1_list = ["conv",10,None,None,0.25,0]
R2_list = ["condSer",None,0.03,0.026,0.25,0]
R3_list = ["condSer",None,0.02,0.22,0.25,0]
R4_list = ["condSer",None,0.02,0.22,0.25,0]
R5_list = ["condPar",None,0.16,0.22,0.015,0]
R6_list = ["condPar",None,0.16,0.72,0.22,0]
R7_list = ["condPar",None,0.16,0.22,0.015,0]
R8_list = ["conv",25,None,None,0.25,0]

resistances_names = ["R1","R2","R3","R4","R5","R6","R7","R8"]
columns_names = ["type","h","L","k","A","RValue"]

# Definition of DataFrame
Resistances_DF = pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list,],index=resistances_names,columns=columns_names)

# Calculating resistances values
Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/(Resistances_DF["h"][Resistances_DF["type"]=="conv"]*Resistances_DF["A"][Resistances_DF["type"]=="conv"])
Resistances_DF["RValue"][Resistances_DF["type"]=="condSer"]=Resistances_DF["L"][Resistances_DF["type"]=="condSer"]/(Resistances_DF["k"][Resistances_DF["type"]=="condSer"]*Resistances_DF["A"][Resistances_DF["type"]=="condSer"])
Resistances_DF["RValue"][Resistances_DF["type"]=="condPar"]=Resistances_DF["L"][Resistances_DF["type"]=="condPar"]/(Resistances_DF["k"][Resistances_DF["type"]=="condPar"]*Resistances_DF["A"][Resistances_DF["type"]=="condPar"])

# Calculating total conductive resistance in parallel
U_par = 1/Resistances_DF["RValue"][Resistances_DF["type"]=="condPar"]
R_par_tot = 1/U_par.sum()

# Calculating total conductive resistance in series
R_ser_tot = Resistances_DF["RValue"][Resistances_DF["type"]=="condSer"].sum()

# Calculating total convective resistance
R_conv_tot = Resistances_DF["RValue"][Resistances_DF["type"]=="conv"].sum()

# Calculating total resistance
R_total = R_ser_tot+R_conv_tot+ R_par_tot

print "The total resistance is "+str(R_total)+" °C/W"
T1 = 20
T2 = -10
A_unit = 0.25
A_tot = 15
Q_unit = (T1-T2)/R_total
Q_wall = Q_unit*(A_tot/A_unit)
print "The total heat flux through the wall is "+str(Q_wall)+" W"