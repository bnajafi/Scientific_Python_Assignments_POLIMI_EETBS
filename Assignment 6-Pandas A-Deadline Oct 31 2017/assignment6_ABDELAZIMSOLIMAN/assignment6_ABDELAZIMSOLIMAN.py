import pandas as pd 
#Resist.LIst
R1_list=["conv",10,None,None,0.25,0]
R2_list=["conv",25,None,None,0.25,0]
R3_list=["cond",None,0.03,0.026,0.25,0]
R4_list=["cond",None,0.02,0.22,0.25,0]
R5_list=["cond",None,0.02,0.22,0.25,0]
R6_list=["cond",None,0.16,0.22,0.015,0]
R7_list=["cond",None,0.16,0.22,0.015,0]
R8_list=["cond",None,0.16,0.72,0.22,0]
resist_names=["Rci","Rco","Rf","Rp1","Rp2","Rpc1","Rpc2","Rb"]
columns_names=["Resistance_type","h","L","k","A","RValue"]
 
Resist_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resist_names, columns=columns_names)


Resist_DF["RValue"][Resist_DF["Resistance_type"]=="conv"]=1./(Resist_DF["h"][Resist_DF["Resistance_type"]=="conv"]*Resist_DF["A"][Resist_DF["Resistance_type"]=="conv"]) 
Resist_DF["RValue"][Resist_DF["Resistance_type"]=="cond"]=Resist_DF["L"][Resist_DF["Resistance_type"]=="cond"]/(Resist_DF["k"][Resist_DF["Resistance_type"]=="cond"]*Resist_DF["A"][Resist_DF["Resistance_type"]=="cond"]) 
 #TOTAL RESIST.
Ser_R_DF=Resist_DF.loc[:"Rp2","RValue"]
Para_R_DF=1./Resist_DF.loc["Rpc1":,"RValue"]
res_ser_total=Ser_R_DF.sum()
res_para_total=1./Para_R_DF.sum()
res_total=round((res_ser_total+res_para_total),2)
#H.TRANS
T1,T2,Unit=20,-10,(3*5)/0.25
Qtotal=int(Unit*((T1-T2)/res_total))