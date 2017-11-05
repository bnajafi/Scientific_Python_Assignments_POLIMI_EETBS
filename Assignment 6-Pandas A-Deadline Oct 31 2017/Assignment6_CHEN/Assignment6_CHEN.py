#Assignment6_Chen

import pandas as pd

#resistance in series
R1=["conv",10,None,None,15,0]
R2=["cond",None,0.03,0.026,15,0]
R3=["cond",None,0.02,0.22,15,0]
R4=["cond",None,0.02,0.22,15,0]
R5=["conv",25,None,None,15,0]

Resistance_names=["R1","R2","R3","R4","R5"]
columns_names=["types","h","L","k","Area","RValue"]
Resistance_DF=pd.DataFrame([R1,R2,R3,R4,R5],index=Resistance_names,columns=columns_names)

Resistance_DF["RValue"][Resistance_DF["types"]=="conv"]=1.0/Resistance_DF["h"][Resistance_DF["types"]=="conv"]/Resistance_DF["Area"][Resistance_DF["types"]=="conv"]
Resistance_DF["RValue"][Resistance_DF["types"]=="cond"]=Resistance_DF["L"][Resistance_DF["types"]=="cond"]/Resistance_DF["k"][Resistance_DF["types"]=="cond"]/Resistance_DF["Area"][Resistance_DF["types"]=="cond"]
Resistance_Series_tot=Resistance_DF["RValue"].sum()

#resistance in parallel

R6=["cond",None,0.16,0.22,1.5/25*15,0,0]
R7=["cond",None,0.16,0.72,22.0/25*15,0,0]
R8=["cond",None,0.16,0.22,1.5/25*15,0,0]

columns_names=["types","h","L","k","Area","RValue","Ufactor"]
Resistance_parallel=pd.DataFrame([R6,R7,R8],["R6","R7","R8"],columns=columns_names)

Resistance_parallel["RValue"]=Resistance_parallel["L"]/Resistance_parallel["k"]/Resistance_parallel["Area"]
Resistance_parallel["Ufactor"]=1.0/Resistance_parallel["RValue"]
Resistance_parallel_Utot=Resistance_parallel["Ufactor"].sum()
Resistance_parallel_RValue_tot=1.0/Resistance_parallel_Utot

Resistances_Rtot=Resistance_parallel_RValue_tot+Resistance_Series_tot

T1=20 #The indoor temperature
T2=-10 #The outdoor temperature
Q=(T1-T2)/Resistances_Rtot 

print Resistance_DF
print Resistance_parallel
print "so the overall resistance of the wall is: " + str(Resistances_Rtot) + " degC/W"
print "so the total heat loss of the wall is: "+ str(Q) + " W"