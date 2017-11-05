# -*- coding: utf-8 -*-
import pandas as pd
Rin_list=(["series","conv",10,None,None,0.25,0,0])
Rf_list=(["series","cond",None,0.03,0.026,0.25,0,0])
Rp1_list=(["series","cond",None,0.02,0.22,0.25,0,0])
Rp2_list=(["series","cond",None,0.02,0.22,0.25,0,0])
Rout_list=(["series","conv",25,None,None,0.25,0,0])
Rb_list=(["parallel","cond",None,0.16,0.72,0.22,0,0])
Rpc1_list=(["parallel","cond",None,0.16,0.22,0.015,0,0])
Rpc2_list=(["parallel","cond",None,0.16,0.22,0.015,0,0])
resistance_names=["Rin","Rf","Rp1","Rp2","Rout","Rb","Rpc1","Rpc2"]
columns_names=["ser/par","type","h","l","k","A","Rvalue","Uvalue"]
Resistances_DF=pd.DataFrame([Rin_list,Rf_list,Rp1_list,Rp2_list,Rout_list,Rb_list,Rpc1_list,Rpc2_list],index=resistance_names,columns=columns_names)
Resistances_DF["Rvalue"][Resistances_DF["type"]=="conv"]=1/(Resistances_DF["h"][Resistances_DF["type"]=="conv"]*Resistances_DF["A"])
Resistances_DF["Rvalue"][Resistances_DF["type"]=="cond"]=Resistances_DF["l"][Resistances_DF["type"]=="cond"]/(Resistances_DF["k"][Resistances_DF["type"]=="cond"]*Resistances_DF["A"])
Resistances_DF["Uvalue"]=1/Resistances_DF["Rvalue"]
RseriesTot=Resistances_DF["Rvalue"][Resistances_DF["ser/par"]=="series"].sum()
RparallelTot=1/(Resistances_DF["Uvalue"][Resistances_DF["ser/par"]=="parallel"].sum())
Rtot=RseriesTot+RparallelTot
print Resistances_DF
print "The total resistance of the wall is "+str(Rtot)+"°C/W"
T1=20
T2=-10
A=15
Q=(T1-T2)*A/(Rtot*0.25)
print "The rate of heat transfered trought the wall is "+str(Q)+" W"