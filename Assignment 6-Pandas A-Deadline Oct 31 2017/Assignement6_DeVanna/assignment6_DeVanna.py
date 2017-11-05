import pandas as pd
AREA=0.25
R1_list = ["conv",10,None,None, 0]
R2_list = ["cond",None,0.026,0.03, 0]
R3_list = ["cond",None,0.22,0.02, 0]
R4_list = ["cond",None,0.22,0.02, 0]
R5_list = ["conv",25,None,None, 0]

#series
resistances_names = ["R1","R2","R3","R4","R5"]
columns_names=["type","h","k","L","RValue"]
Resistances_S=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list],index=resistances_names,columns=columns_names)
Resistances_S["RValue"][Resistances_S["type"]=="conv"]=1.0/(Resistances_S["h"][Resistances_S["type"]=="conv"]*AREA)
Resistances_S["RValue"][Resistances_S["type"]=="cond"]=Resistances_S["L"][Resistances_S["type"]=="cond"]/(Resistances_S["k"][Resistances_S["type"]=="cond"]*AREA)
Resistenza_serie_tot=Resistances_S["RValue"].sum()

#parallel
R6_list = ["cond",0.22,0.16,0.015, 0]
R7_list = ["cond",0.72,0.16,0.22, 0]
R8_list = ["cond",0.22,0.16,0.015, 0]
resistance_names1=["R6","R7","R8"]
columns_names1=["type","k1","L1","A","RValueP"]
Resistances_P=pd.DataFrame([R6_list,R7_list,R8_list],index=resistance_names1,columns=columns_names1)
Resistances_P["RValueP"][Resistances_P["type"]=="cond"]=Resistances_P["L1"][Resistances_P["type"]=="cond"]/(Resistances_P["k1"][Resistances_P["type"]=="cond"]*Resistances_P["A"][Resistances_P["type"]=="cond"])
Resistances_parallel_fianl = 1/(1/ Resistances_P["RValueP"]).sum()

RESTISTENZA_TOTALE=Resistances_parallel_fianl+Resistenza_serie_tot