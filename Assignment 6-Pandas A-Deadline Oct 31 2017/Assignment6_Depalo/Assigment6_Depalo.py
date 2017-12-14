# -*- coding: utf-8 -*-
#Assignment 6

import pandas as pd

R1_list = ["conv",10,None,None, 0]
R2_list = ["cond",None,0.03,0.026, 0]
R3_list = ["cond",None,0.02,0.22, 0]
R4_list = ["cond",None,0.02,0.22, 0]
R5_list = ["conv",25,None,None, 0]

resistances_names = ["R1","R2","R3","R4","R5"]
columns_names=["type","h","L","k","RValue"]

Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list],index=resistances_names,columns=columns_names)

print Resistances_DF

Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/Resistances_DF["h"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"][Resistances_DF["type"]=="cond"]/Resistances_DF["k"][Resistances_DF["type"]=="cond"]

R6_list = [0.16,0.22,0.015,0]
R7_list = [0.16,0.72,0.22,0]
R8_list = [0.16,0.22,0.015,0]

resistances_names = ["R6","R7","R8"]
columns_names=["L","k","A","RValue"]

ResistancesParallel_DF=pd.DataFrame([R6_list,R7_list,R8_list],index=resistances_names,columns=columns_names)

print '\n\n'
print ResistancesParallel_DF
print '\n\n'

ResistancesParallel_DF["RValue"]=ResistancesParallel_DF["L"]/ResistancesParallel_DF["k"]/ResistancesParallel_DF["A"]

Resistances_Rtot_Series=Resistances_DF["RValue"].sum()

A_unit=0.25
A_tot=15

Resistances_midstep=(1/ResistancesParallel_DF["RValue"])
Resistances_Rtot_Parallel=(Resistances_midstep.sum())**(-1)

Resistances_Rtot=Resistances_Rtot_Parallel+Resistances_Rtot_Series/A_unit

T_in=20
T_out=-10
Qtot=A_tot/A_unit*(T_in-T_out)/Resistances_Rtot

print "Total resistance: " + str(Resistances_Rtot) + ' m^2*K/W.\n\n'
print "Total heat flux: " + str(Qtot) + ' W.\n'