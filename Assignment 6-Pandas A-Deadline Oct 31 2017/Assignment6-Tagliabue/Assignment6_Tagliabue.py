#Assignment 6
import pandas as pd
Awall=15
Ti=20
To=-10
Req=0
R1_list = ["cond","serie",None,0.03,0.026, 0,0.25]#type-h-lenght-k-r value-area
R2_list = ["cond","serie",None,0.04,0.22, 0,0.25]
R3_list = ["cond","parallel",None,0.16,0.22, 0,0.015]
R4_list = ["cond","parallel",None,0.16,0.72, 0,0.22]
R5_list = ["conv","serie",10,None,None, 0,0.25]
R6_list = ["conv","serie",25,None,None, 0,0.25]
resistances_names = ["R1","R2","R3","R4","R5","R6"]
columns_names=["type","ps","h","L","k","RValue","area"]
Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list],index=resistances_names,columns=columns_names)

Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/(Resistances_DF["h"]*Resistances_DF["area"])
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"]/(Resistances_DF["k"]*Resistances_DF["area"])

print ("This are the resistances values",Resistances_DF)
Rp=0
Rp=(1.0/Resistances_DF["RValue"][Resistances_DF["ps"]=="parallel"]).sum()
Req=(Resistances_DF["RValue"][Resistances_DF["ps"]=="serie"]).sum()+Rp
print ("The equivalent total resistance is Req=", Req)
Q=(Ti-To)/Req
print ("The rate of heat transfer is Q=", Q)

Qwall=Q*Awall/0.25

print ("The rate of heat transfer of the wall is Qwall=", Qwall)