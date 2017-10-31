import pandas as pd

H = 3.0
L = 5.0 #wall dimensions

Tin = 20.0
Tout = -10.0 #temperatures
A_S = 0.25

#series calculations

Rin = ["conv",10,None,None,0]
Rfoam = ["cond",None,0.03,0.026,0]
Rplaster = ["cond",None,0.02,0.22,0]
Rout = ["conv",25,None,None,0]
resistances_names_series = ["In","foam","plaster","plaster","Out"]
columns_names = ["type","h","L","k","RValue"]

Resistances_DF_series = pd.DataFrame([Rin,Rfoam,Rplaster,Rplaster,Rout],index=resistances_names_series,columns=columns_names)

Resistances_DF_series["RValue"][Resistances_DF_series["type"]=="conv"] = 1.0/(Resistances_DF_series["h"][Resistances_DF_series["type"]=="conv"]*A_S)
Resistances_DF_series["RValue"][Resistances_DF_series["type"]=="cond"] = Resistances_DF_series["L"][Resistances_DF_series["type"]=="cond"]/(Resistances_DF_series["k"][Resistances_DF_series["type"]=="cond"]*A_S)
Rtot_series = Resistances_DF_series["RValue"].sum()

#parallel calculations

Rplaster_par = [0.22,0.16,0.015,0]
Rbrick_par = [0.72,0.16,0.22,0]
resistances_names_par = ["plaster","brick","plaster"]
columns_names_par = ["k","L","A","Rvalue"]

Resistances_DF_par = pd.DataFrame([Rplaster_par,Rbrick_par,Rplaster_par],index=resistances_names_par,columns=columns_names_par)
Resistances_DF_inv = pd.DataFrame([Rplaster_par,Rbrick_par,Rplaster_par],index=resistances_names_par,columns=columns_names_par)

Resistances_DF_par["RValue"] = Resistances_DF_par["L"]/(Resistances_DF_par["k"]*Resistances_DF_par["A"])
Resistances_DF_inv["RValue"] = 1/Resistances_DF_par["RValue"]

Rtot_parallel = (Resistances_DF_inv["RValue"].sum())**(-1)

Rtot= Rtot_series + Rtot_parallel
print "the total resistance is: " + str(Rtot) + " (degC/W)"

Q = (Tin - Tout)/Rtot
print "the rate of heat transfer through the wall for each unit is "+str(Q)+ " (W)"
Qtot = (Q*H*L)/0.25
print "the total rate of heat transfer through the wall is "+str(Qtot)+ " (W)" 