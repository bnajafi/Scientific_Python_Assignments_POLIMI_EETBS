#Assignment 6 - Riccardi
import pandas as pd

Rout = ["conv",10.0,None,None,0.25, 0]
Rfoam = ["cond",None,0.03,0.026,0.25, 0]
Rplaster1_series = ["cond",None,0.02,0.22,0.25, 0]
Rplaster2_series = ["cond",None,0.02,0.22,0.25, 0]
Rin = ["conv",25.0,None,None,0.25, 0]

resistances_names = ["Rout","Rfoam","Rplaster1_series","Rplaster2_series","Rin"]
columns_names=["type","h","L","k","Area","RValue"]

Resistances_series=pd.DataFrame([Rout,Rfoam,Rplaster1_series,Rplaster2_series,Rin],index=resistances_names,columns=columns_names)
Resistances_series["RValue"][Resistances_series["type"]=="conv"]=1.0/Resistances_series["h"][Resistances_series["type"]=="conv"]/Resistances_series["Area"]
Resistances_series["RValue"][Resistances_series["type"]=="cond"]=Resistances_series["L"][Resistances_series["type"]=="cond"]/Resistances_series["k"][Resistances_series["type"]=="cond"]/Resistances_series["Area"]
Rtot_series=Resistances_series["RValue"].sum()

Rplaster1_par = ["cond",None,0.16,0.22,0.015, 0]
Rplaster2_par = ["cond",None,0.16,0.22,0.015, 0]
Rbrick = ["cond",None,0.16,0.72,0.22, 0]

resistances_names = ["Rbrick","Rplaster1_par","Rplaster2_par"]
columns_names=["type","h","L","k","Area","RValue"]

Resistances_par=pd.DataFrame([Rplaster1_par,Rplaster2_par,Rbrick],index=resistances_names,columns=columns_names)
Resistances_par["RValue"]=Resistances_par["L"]/Resistances_par["k"]/Resistances_par["Area"]
Rtot_par=((Resistances_par["RValue"]**-1).sum())**-1

Rtot_unit=Rtot_series+Rtot_par

print ("The total value of the resistance of the unit is: "+str(Rtot_unit)+" [K/W]")

