#-----------Using Pandas & Reapeating Assignment-5-------#

#---------------MUHAMMAD-ARSLAN-----------#

import pandas as pd


#--Defining Layers list with their corresponding values--

R1_list=["conv",10,None,None,0.25,0]
R2_list=["conv",25,None,None,0.25,0]
R3_list=["cond",None,0.03,0.026,0.25,0]
R4_list=["cond",None,0.02,0.22,0.25,0]
R5_list=["cond",None,0.02,0.22,0.25,0]
R6_list=["cond",None,0.16,0.22,0.015,0]
R7_list=["cond",None,0.16,0.22,0.015,0]
R8_list=["cond",None,0.16,0.72,0.22,0]

resistances_names=["Ri","Ro","Rf","Rp1","Rp2","Rpc1","Rpc2","Rb"]

columns_names=["Resistance_type","h","L","k","A","RValue"]

#--Producing A DataFrame--

Resistances_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resistances_names, columns=columns_names)

#--Calculating RValues of DataFrame--

Resistances_DF["RValue"][Resistances_DF["Resistance_type"]=="conv"]=1/(Resistances_DF["h"][Resistances_DF["Resistance_type"]=="conv"]*Resistances_DF["A"][Resistances_DF["Resistance_type"]=="conv"]) 
Resistances_DF["RValue"][Resistances_DF["Resistance_type"]=="cond"]=Resistances_DF["L"][Resistances_DF["Resistance_type"]=="cond"]/(Resistances_DF["k"][Resistances_DF["Resistance_type"]=="cond"]*Resistances_DF["A"][Resistances_DF["Resistance_type"]=="cond"]) 

#------Total Resistance values--------------#

Series_R_DF=Resistances_DF.loc[:"Rp2","RValue"]

Parallel_R_DF=1/Resistances_DF.loc["Rpc1":,"RValue"]

res_series_total=Series_R_DF.sum()

res_parallel_total=1/Parallel_R_DF.sum()

res_total=(res_series_total+res_parallel_total)

print("The total effective thermal resistance is: "+str(res_total)+" degC/W")

#----------Calculation of Q-total----#

T1,T2,Unit=20,-10,(3*5)/0.25

Qtotal=Unit*((T1-T2)/res_total)

print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")