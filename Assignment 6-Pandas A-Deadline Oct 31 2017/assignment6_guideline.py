
R1_list = ["conv",10,None,None, 0]
R2_list = ["cond",None,0.8,0.5, 0]
R3_list = ["cond",None,1.5,0.3, 0]
R4_list = ["cond",None,0.05,0.6, 0]
R5_list = ["conv",25,None,None, 0]

resistances_names = ["R1","R2","R3","R4","R5"]
columns_names=["type","h","L","k","RValue"]
#How to define a DataFrame , !!!! D and F are capital letters!!!!!

Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list],index=resistances_names,columns=columns_names)
Resistances_DF["h"]
Resistances_DF.loc["R1",:]
Resistances_DF["type"]=="conv"
Resistances_DF["h"]
Resistances_DF["h"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/Resistances_DF["h"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"][Resistances_DF["type"]=="cond"]/Resistances_DF["k"][Resistances_DF["type"]=="cond"]


