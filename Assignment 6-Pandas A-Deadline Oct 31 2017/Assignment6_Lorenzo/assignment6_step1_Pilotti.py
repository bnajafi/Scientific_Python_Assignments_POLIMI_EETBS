# Assignment 6

import pandas as pd


# Resistances in series
R_series_names=["Rin", "R1", "R2", "R6", "Rout"]
R_series_columns=["type", "h", "L", "k","Area", "Rvalue"]

Rin=["conv", 10, None, None, 0.25, 0]
R1=["cond", None, 0.03, 0.026,0.25, 0]
R2=["cond", None, 0.02, 0.22,0.25, 0]
R6=R2
Rout=["conv", 25, None, None, 0.25, 0]

R_series_DF=pd.DataFrame([Rin, R1, R2, R6, Rout], index=R_series_names, columns=R_series_columns)

R_series_DF["Rvalue"][R_series_DF["type"]=="conv"]=1.0/R_series_DF["h"][R_series_DF["type"]=="conv"]/R_series_DF["Area"][R_series_DF["type"]=="conv"]
R_series_DF["Rvalue"][R_series_DF["type"]=="cond"]=R_series_DF["L"][R_series_DF["type"]=="cond"]/R_series_DF["k"][R_series_DF["type"]=="cond"]/R_series_DF["Area"][R_series_DF["type"]=="cond"]

Rtot_series=R_series_DF["Rvalue"].sum()

# Resistance in parallel

R_parallel_names=["R3", "R4", "R5"]
R_parallel_columns=["type", "h", "L", "k","Area", "Rvalue", "Uvalue"]

R3=["cond", None, 0.16, 0.22, 0.015, 0, 0]
R4=["cond", None, 0.16, 0.72, 0.22, 0, 0]
R5=R3

R_parallel_DF=pd.DataFrame([R3, R4, R5], index=R_parallel_names, columns=R_parallel_columns)

R_parallel_DF["Rvalue"][R_parallel_DF["type"]=="cond"]=R_parallel_DF["L"][R_parallel_DF["type"]=="cond"]/R_parallel_DF["k"][R_parallel_DF["type"]=="cond"]/R_parallel_DF["Area"][R_parallel_DF["type"]=="cond"]

R_parallel_DF["Uvalue"][R_parallel_DF["type"]=="cond"]=1.0/R_parallel_DF["Rvalue"][R_parallel_DF["type"]=="cond"]

Rtot_parallel=R_parallel_DF["Uvalue"].sum()**-1

# Total resistance

Rtot=Rtot_parallel+Rtot_series # referred to 0.25 m2 of surface area.


 