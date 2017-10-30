import pandas as pd
R1_list = ["series","conv",10,None,None, 0.25, 0]
R2_list = ["series","cond",None,0.03,0.026, 0.25, 0]
R3_list = ["series","cond",None,0.02,0.22, 0.25, 0]
R4_list = ["series","cond",None,0.02,0.22, 0.25, 0]
R5_list = ["series","conv",25,None,None, 0.25, 0]
R6_list = ["parallel","cond",None,0.16,0.22, 0.015, 0]
R7_list = ["parallel","cond",None,0.16,0.22, 0.015, 0]
R8_list = ["parallel","cond",None,0.16,0.72, 0.22, 0]

resistances_names = ["R1","R2","R3","R4","R5","R6","R7","R8"]
columns_names=["type1","type2","h","L","k","A","RValue"]
Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resistances_names,columns=columns_names)
Resistances_DF["RValue"][Resistances_DF["type2"]=="conv"]=1.0/(Resistances_DF["h"][Resistances_DF["type2"]=="conv"]*Resistances_DF["A"])
Resistances_DF["RValue"][Resistances_DF["type2"]=="cond"]=Resistances_DF["L"]/(Resistances_DF["k"]*Resistances_DF["A"])
inv_Rpar=1.0/(Resistances_DF["RValue"][Resistances_DF["type2"]=="cond"][Resistances_DF["type1"]=="parallel"])
Rpar=inv_Rpar.sum()
Rser=Resistances_DF["RValue"][Resistances_DF["type1"]=="series"].sum()
Rtot=Rser+Rpar
print "The total resistance of the wall is: "+str(Rtot)
Area=15.0
DT=30
Qwall=Area/0.25*DT/Rtot
print "so the heat transfer through the wall is: " +str(Qwall)