#assignment 6 executing in pandas 
import pandas as pd

R1_list=["conv",10,None,None,0.25,0]
R2_list=["conv",25,None,None,0.25,0]
R3_list=["cond",None,0.03,0.026,0.25,0]
R4_list=["cond",None,0.02,0.22,0.25,0]
R5_list=["cond",None,0.02,0.22,0.25,0]
R6_list=["cond",None,0.16,0.22,0.015,0]
R7_list=["cond",None,0.16,0.22,0.015,0]
R8_list=["cond",None,0.16,0.72,0.22,0]\

resistances_names=["Rci","Rco","Rf","Rp1","Rp2","Rpc1","Rpc2","Rb"]
columns_names=["Resistance_type","h","L","k","A","RValue"]

Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resistances_names, columns=columns_names)

Resistances_DF["RValue"][Resistances_DF["Resistance_type"]=="conv"]=1./(Resistances_DF["h"][Resistances_DF["Resistance_type"]=="conv"]*Resistances_DF["A"][Resistances_DF["Resistance_type"]=="conv"]) 
Resistances_DF["RValue"][Resistances_DF["Resistance_type"]=="cond"]=Resistances_DF["L"][Resistances_DF["Resistance_type"]=="cond"]/(Resistances_DF["k"][Resistances_DF["Resistance_type"]=="cond"]*Resistances_DF["A"][Resistances_DF["Resistance_type"]=="cond"]) 

Series_R_DF=Resistances_DF.loc[:"Rp2","RValue"]
Parallel_R_DF=1./Resistances_DF.loc["Rpc1":,"RValue"]
res_series_total=Series_R_DF.sum()
res_parallel_total=1./Parallel_R_DF.sum()
res_total=round((res_series_total+res_parallel_total),2)
T1,T2,Unit=20,-10,(3*5)/0.25
Qtotal=int(Unit*((T1-T2)/res_total))

print("The total effective thermal resistance is: "+str(res_total)+" degC/W")
print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")