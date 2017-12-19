import pandas as pd
R1_list=["conv",10, None,None,0.25,0]
R2_list=["condser",None,0.03,0.026,0.25,0]
R3_list=["condser",None,0.02,0.22,0.25,0]
R4_list=["condser",None,0.02,0.22,0.25,0]
R5_list=["condpar",None,0.16,0.22,0.015,0]
R6_list=["condpar",None,0.16,0.72,0.22,0]
R7_list=["condpar",None,0.16,0.22,0.015,0]
R8_list=["conv",25,None,None,0.25,0]

resistance_names=["Rin","Rser1","Rser2","Rser3","Rpar1","Rpar2","Rpar3","Rout"]
column_names=["type","h","L","k","area","RValue"]

Res_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resistance_names,columns=column_names)

Res_DF["RValue"][Res_DF["type"]=="conv"]=1.0/(Res_DF["h"][Res_DF["type"]=="conv"]*Res_DF["area"][Res_DF["type"]=="conv"])

Res_DF["RValue"][Res_DF["type"]=="condser"]=Res_DF["L"][Res_DF["type"]=="condser"]/(Res_DF["k"][Res_DF["type"]=="condser"]*
Res_DF["area"][Res_DF["type"]=="condser"])

Res_DF["RValue"][Res_DF["type"]=="condpar"]=Res_DF["L"][Res_DF["type"]=="condpar"]/(Res_DF["k"][Res_DF["type"]=="condpar"]*
Res_DF["area"][Res_DF["type"]=="condpar"])

R_cond_ser=Res_DF["RValue"][Res_DF["type"]=="condser"].sum()

R_cond_par=((1.0/(Res_DF["RValue"][Res_DF["type"]=="condpar"])).sum())**-1

R_conv=Res_DF["RValue"][Res_DF["type"]=="conv"].sum()

Res_tot=R_cond_ser+R_cond_par+R_conv

print "The total resistance of the wall is: " +str(Res_tot)+ "C/W"





