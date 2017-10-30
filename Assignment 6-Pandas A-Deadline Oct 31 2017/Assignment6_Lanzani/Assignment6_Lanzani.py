import pandas as pd

R1=["conv","series",10,None,None,0.25,0]
R2=["cond","series",None,0.026,0.03,0.25,0]
R3=["cond","series",None,0.22,0.02,0.25,0]
R4=["cond","series",None,0.22,0.02,0.25,0]
R5=["conv","series",25.0,None,None,0.25,0]
R6=["cond","parallel",None,0.22,0.16,0.015,0]
R7=["cond","parallel",None,0.72,0.16,0.22,0]
R8=["cond","parallel",None,0.22,0.16,0.015,0]

columns_name=["type","position","h","k","L","A","RValue"]
Resistance_name=["R1","R2","R3","R4","R5","R6","R7","R8"]
Resistances_DF=pd.DataFrame([R1,R2,R3,R4,R5,R6,R7,R8],index=Resistance_name,columns=columns_name)

Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1./(Resistances_DF["h"][Resistances_DF["type"]=="conv"]*Resistances_DF["A"][Resistances_DF["type"]=="conv"])
Resistances_DF["RValue"][Resistances_DF["type"]=="cond"]=Resistances_DF["L"][Resistances_DF["type"]=="cond"]/(Resistances_DF["k"][Resistances_DF["type"]=="cond"]*Resistances_DF["A"][Resistances_DF["type"]=="cond"])

R_parallel=1./(sum(1.0/Resistances_DF["RValue"][Resistances_DF["position"]=="parallel"]))

R_series=sum(Resistances_DF["RValue"][Resistances_DF["position"]=="series"])

R_tot=sum(Resistances_DF["RValue"][Resistances_DF["position"]=="series"])+1./(sum(1.0/Resistances_DF["RValue"][Resistances_DF["position"]=="parallel"]))
print "R_tot is "+str(R_tot)
#Q
Aw=3*5
T1=20
T2=-10
Q=(T1-T2)/R_tot
A=0.25*1
Qw=Q*(Aw/A)
print 'Qw is '+ str(Qw)+ ' W'