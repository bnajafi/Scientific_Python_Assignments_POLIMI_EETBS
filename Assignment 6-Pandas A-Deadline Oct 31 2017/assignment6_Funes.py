import pandas as pd

R1_list = ["conv","series","brick","Plaster",10,None,None,0.25,0] #type of heat transfer, h, k, L, Ro

R2_list = ["cond","series","brick","Plaster",None,0.026,0.03,0.25,0]

R3_list = ["cond","series","brick","Plaster",None,0.22,0.02,0.25,0]

R4_list = ["cond","parallel",None,"Plaster",None,0.22,0.16,0.15,0]

R5_list = ["cond","parallel","brick",None,None,0.72,0.16,0.22,0]

R6_list = ["cond","parallel",None,"Plaster",None,0.22,0.16,0.15,0]

R7_list = ["cond","series","brick","Plaster",None,0.22,0.02,0.25,0]

R8_list = ["conv","series","brick","Plaster",25,None,None,0.25,0]

ATot = 15.0
AUnit = 0.25
T81 = 20
T82 = -10
fins = 0.75

Resistances_names = ["Ri","Rf","Rp1", "Rpc1", "Rb", "Rpc2", "Rp2", "Ro"]
Columns_names = ["type of heat transfer","config","ConsiderBrick","ConsiderPlaster", "h", "k", "L", "Aunit","RVAlue"]

Resistances_DF = pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=Resistances_names, columns=Columns_names)

Resistances_DF["RVAlue"][Resistances_DF["type of heat transfer"]=="conv"]=1/(Resistances_DF["h"][Resistances_DF["type of heat transfer"]=="conv"]*Resistances_DF["Aunit"][Resistances_DF["type of heat transfer"]=="conv"])

Resistances_DF["RVAlue"][Resistances_DF["type of heat transfer"]=="cond"]=(Resistances_DF["L"][Resistances_DF["type of heat transfer"]=="cond"])/(Resistances_DF["k"][Resistances_DF["type of heat transfer"]=="cond"]*Resistances_DF["Aunit"][Resistances_DF["type of heat transfer"]=="cond"])

ResistTotSeries = Resistances_DF["RVAlue"][Resistances_DF["config"]=="series"].sum()

print "The equivalent resistance in series is :"+str(ResistTotSeries)

ResistTotParallel = 1/((1/Resistances_DF["RVAlue"][Resistances_DF["config"]=="parallel"]).sum())

print "The equivalent resistance in parallel is :"+str(ResistTotParallel)

ResistEquiv = ResistTotSeries+ResistTotParallel

print "The equivalent resistance of the wall is :"+str(ResistEquiv)

#ResistConsideringBrick = Resistances_DF["RVAlue"][Resistances_DF["ConsiderBrick"]=="brick"].sum()

#ResistConsideringPlaster = Resistances_DF["RVAlue"][Resistances_DF["ConsiderPlaster"]=="Plaster"].sum()

#ResistUnit = ResistConsideringBrick*(1-fins)+ResistConsideringPlaster*fins

#print "The total resistance is :"+str(ResistUnit)

#UTot = (1/ResistUnit)*(ATot/AUnit)

#Qwall = UTot*(T81-T82)

#print "The total heat tranfered through the wall is :"+str(Qwall)