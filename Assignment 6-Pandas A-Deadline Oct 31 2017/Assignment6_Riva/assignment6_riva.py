#ASSIGNMENT 6

import pandas as pd

#series

ind_s=["R1","R2","R3","R4","R5"]
columns_name=["type","L","k","h","Rvalue"]
area=0.25

R1_list=["conv",None,None,10,0]
R2_list=["cond",0.03,0.026,None,0]
R3_list=["cond",0.02,0.22,None,0]
R4_list=["cond",0.02,0.22,None,0]
R5_list=["conv",None,None,25,0]

Res_S=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list],index=ind_s,columns=columns_name)

Res_S["Rvalue"][Res_S["type"]=="conv"]=1/(Res_S["h"][Res_S["type"]=="conv"]*area)
Res_S["Rvalue"][Res_S["type"]=="cond"]=Res_S["L"][Res_S["type"]=="cond"]/(Res_S["k"][Res_S["type"]=="cond"]*area)

Res_S_final=Res_S["Rvalue"].sum()

print Res_S
print Res_S_final

#paraller

R6_list=["cond",0.22,0.16,0.015,0]
R7_list=["cond",0.72,0.16,0.22,0]
R8_list=["cond",0.22,0.16,0.015,0]

ind_p=["R6","R7","R8"]
columns_name_p=["type","k1","L1","A","RValueP"]

Res_P=pd.DataFrame([R6_list,R7_list,R8_list], index=ind_p, columns=columns_name_p)
Res_P["RValueP"][Res_P["type"]=="cond"]=Res_P["L1"][Res_P["type"]=="cond"]/(Res_P["k1"][Res_P["type"]=="cond"]*Res_P["A"][Res_P["type"]=="cond"])
Res_P_final=1/(1/ Res_P["RValueP"]).sum()

print Res_P
print Res_P_final
