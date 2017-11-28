import pandas as pd

R_in = ["conv","series",10,None,None,0.25,0,0]
R_foam = ["cond","series",None,0.03,0.026,0.25,0,0]
R_plaster1_series = ["cond","series",None,0.02,0.22,0.25,0,0]
R_plaster1_parallel = ["cond","parallel",None,0.16,0.22,0.015,0,0]
R_brick = ["cond","parallel",None,0.16,0.72,0.22,0,0]
R_plaster2_parallel = ["cond","parallel",None,0.16,0.22,0.015,0,0]
R_plaster2_series = ["cond","series",None,0.02,0.22,0.25,0,0]
R_out = ["conv","series",25,None,None,0.25,0,0]

ResistancesNames = ["R_in","R_foam","R_plaster1_series","R_plaster1_parallel","R_brick","R_plaster2_parallel","R_plaster2_series","R_out"]
columnsNames = ["type1","type2","h","L","k","Area","RValue","UValue"]

Resistances_DF = pd.DataFrame([R_in,R_foam,R_plaster1_series,R_plaster1_parallel,R_brick,R_plaster2_parallel,R_plaster2_series,R_out],
index=ResistancesNames,columns=columnsNames)

Resistances_DF["RValue"][Resistances_DF["type1"]=="conv"] = 1.0/(Resistances_DF["h"]*Resistances_DF["Area"]) #convective resistances

Resistances_DF["RValue"][Resistances_DF["type1"]=="cond"] = Resistances_DF["L"]/(Resistances_DF["k"]*Resistances_DF["Area"]) #conductive resistances

Resistances_DF["UValue"] = 1.0/Resistances_DF["RValue"]

Rtot_series = Resistances_DF["RValue"][Resistances_DF["type2"]=="series"].sum()

Utot_parallel = Resistances_DF["UValue"][Resistances_DF["type2"]=="parallel"].sum()

Rtot_parallel = 1.0/Utot_parallel

Rtot = Rtot_series + Rtot_parallel

T_in = 20
T_out = -10
A_wall = 15
Q_wall = ((T_in-T_out)/Rtot)*(A_wall/0.25)

print "the total resistance of the wall is " + str(Rtot) + "degC/W "
print "the heat transfer rate through the wall is " + str(Q_wall) + "W"