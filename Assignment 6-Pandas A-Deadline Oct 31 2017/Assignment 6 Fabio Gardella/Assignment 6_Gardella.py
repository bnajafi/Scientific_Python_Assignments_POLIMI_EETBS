import pandas as pd

#DEFINING RESISTANCES LISTS

R0_list = ["conv","Air",10,None,None,0.25,0,0]
R1_list = ["cond","Foam",None,0.026,0.03,0.25,0,0]
R2_list = ["cond","Plaster",None,0.22,0.02,0.25,0,0]
R3_list = ["cond","Plaster",None,0.22,0.16,0.015,0,0]
R4_list = ["cond","Brick",None,0.72,0.16,0.22,0,0]
R5_list = ["cond","Plaster",None,0.22,0.16,0.015,0,0]
R6_list = ["cond","Plaster",None,0.22,0.02,0.25,0,0]
R7_list = ["conv","Air",25,None,None,0.25,0,0]

column_names = ["Type","Material","h","k","L","A","RValue","UValue"]


#RESISTANCES IN SERIES ( CONDUCTIVE + CONVECTIVE )

Resistances_in_series_names = ["R0","R1","R2","R6","R7"]

Resistances_in_series_DF = pd.DataFrame([R0_list,R1_list,R2_list,R6_list,R7_list],index=Resistances_in_series_names,columns=column_names)

Resistances_in_series_DF["RValue"][Resistances_in_series_DF["Type"]=="conv"] = 1.0 / Resistances_in_series_DF["h"][Resistances_in_series_DF["Type"]=="conv"]

Resistances_in_series_DF["RValue"][Resistances_in_series_DF["Type"]=="cond"] = Resistances_in_series_DF["L"][Resistances_in_series_DF["Type"]=="cond"] / Resistances_in_series_DF["k"][Resistances_in_series_DF["Type"]=="cond"]

Resistances_in_series_DF["UValue"] = 1.0 / Resistances_in_series_DF["RValue"]

RSerTot = Resistances_in_series_DF["RValue"].sum()


#RESISTANCES IN PARALLEL

Resistances_in_parallel_names = ["R3","R4","R5"]

Resistances_in_parallel_DF = pd.DataFrame([R3_list,R4_list,R5_list],index=Resistances_in_parallel_names,columns=column_names)

Resistances_in_parallel_DF["RValue"] = Resistances_in_parallel_DF["L"] / Resistances_in_parallel_DF["k"]

Resistances_in_parallel_DF["UValue"] = 1.0 / Resistances_in_parallel_DF["RValue"]

UParTot = Resistances_in_parallel_DF["UValue"].sum()

RParTot = 1.0 / UParTot


#TOTAL RESISTANCE

RTot = RParTot + RSerTot


# HEAT FLUX CALCULATIONS

T1=20 
T2=-10
deltaT = T1 - T2

Awall = 15
Aelement = 0.25

Q = deltaT / RTot                                            #Heat flux of the single element

Qwall=Q*(Awall/Aelement)                                     #Heat flux of the entire wall


