#assignment 6

import pandas as pd

columns=["S-P","type","L", "k", "h", "Area", "Rvalue"]
index=["R1","R2","R3","R4","R5","R6","R7","R8"]
#Series
R1=["S","conv", None,None, 10,0.25, 0]
R2=["S","cond", 0.03,0.026, None,0.25, 0]
R3=["S","cond", 0.02,0.22, None,0.25, 0]
R4=["S","cond", 0.02,0.22, None,0.25, 0]
R5=["S","conv", None,None, 25, 0.25, 0]
R6=["P", None, 0.16, 0.22 , None, 0.015 , 0]
R7=["P", None, 0.16, 0.72 , None, 0.22 , 0]
R8=["P", None, 0.16, 0.22 , None, 0.015 , 0]

Resistances=pd.DataFrame ([R1,R2,R3,R4,R5,R6,R7,R8], index=index, columns=columns)

Resistances["Rvalue"][Resistances["type"]=="conv"]=1.0/(Resistances["h"][Resistances["type"]=="conv"]*Resistances["Area"][Resistances["type"]=="conv"])
Resistances["Rvalue"][Resistances["type"]=="cond"]=Resistances["L"][Resistances["type"]=="cond"]/(Resistances["k"][Resistances["type"]=="cond"]*Resistances["Area"][Resistances["type"]=="cond"])

Resistances["Rvalue"][Resistances["S-P"]=="P"]=1/(Resistances["L"][Resistances["S-P"]=="P"]/(Resistances["k"][Resistances["S-P"]=="P"]*Resistances["Area"][Resistances["S-P"]=="P"]))

Rtot=(Resistances["Rvalue"][Resistances["type"]=="conv"].sum())+(Resistances["Rvalue"][Resistances["type"]=="cond"].sum())+(1/(Resistances["Rvalue"][Resistances["S-P"]=="P"].sum()))

print Rtot

