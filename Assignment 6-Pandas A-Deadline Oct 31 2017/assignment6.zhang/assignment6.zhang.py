import pandas as pd
R1_list = ["conv",25,None,None, 0]
R2_list = ["cond",None,0.03,1.25, 0]
R3_list = ["cond",None,0.02,1.25, 0]
R4_list = ["cond",None,0.02,1.25, 0]
R5_list = ["cond",None,0.16,0.75, 0]
R6_list = ["cond",None,0.16,1.1, 0]
R7_list = ["cond",None,0.16,0.075, 0]
R8_list = ["conv",10,None,None, 0]

resistances_names = ["outdoor air","foam","plaster layer 1","plaster layer 2","1.5 cm thick plaster layer 1","brick","1.5 cm thick plaster layer 2","indoor air"]
columns_names=["type","h","L","k","RValue"]

Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resistances_names,columns=columns_names)
Resistances_DF["h"]
Resistances_DF.loc["outdoor air",:]
Resistances_DF["type"]=="conv"
Resistances_DF["h"]
Resistances_DF["h"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/Resistances_DF["h"][Resistances_DF["type"]=="conv"]
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"][Resistances_DF["type"]=="cond"]/Resistances_DF["k"][Resistances_DF["type"]=="cond"]

Resistances_Rtot=Resistances_DF["RValue"].sum()
T1 = 20 # The indoor temperatures 
T2 = 10 # The outdoor temperatures 

Q = (T1-T2)/Resistances_Rtot
Atot = 5*3
Qtot = Q*Atot
print "So the rate of heat transfer through the wall is:" + str(Qtot)+ "W"
