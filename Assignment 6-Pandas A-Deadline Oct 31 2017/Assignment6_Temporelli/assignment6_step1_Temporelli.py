# -*- coding: utf-8 -*-
import pandas as pd

R_i = ["conv",10,None,None,0.25, 0] #all RValue are initilized to 0
R_f = ["cond_ser",None,0.03,0.026,0.25, 0]
R_p1 = ["cond_ser",None,0.02,0.22,0.25, 0]
R_pl1 = ["cond_par",None,0.16,0.22,0.015, 0]
R_b = ["cond_par",None,0.16,0.72,0.22, 0]
R_pl2 = ["cond_par",None,0.16,0.22,0.015, 0]
R_p2 = ["cond_ser",None,0.02,0.22,0.25, 0]
R_o = ["conv",25,None,None,0.25, 0]

resistances_names = ["R_i","R_f","R_p1","R_pl1","R_b","R_pl2","R_p2","R_o"]
columns_names=["type","h","L","k","A","RValue"]

#data frame construction

Resistances_DF=pd.DataFrame([R_i,R_f,R_p1,R_pl1,R_b,R_pl2,R_p2,R_o],index=resistances_names,columns=columns_names)
Resistances_DF["RValue"][Resistances_DF["type"]=="conv"]=1.0/(Resistances_DF["h"][Resistances_DF["type"]=="conv"]*Resistances_DF["A"][Resistances_DF["type"]=="conv"])
Resistances_DF["RValue"][Resistances_DF["type"]=="cond_ser"]=Resistances_DF["L"][Resistances_DF["type"]=="cond_ser"]/(Resistances_DF["k"][Resistances_DF["type"]=="cond_ser"]*Resistances_DF["A"][Resistances_DF["type"]=="cond_ser"])
Resistances_DF["RValue"][Resistances_DF["type"]=="cond_par"]=Resistances_DF["L"][Resistances_DF["type"]=="cond_par"]/(Resistances_DF["k"][Resistances_DF["type"]=="cond_par"]*Resistances_DF["A"][Resistances_DF["type"]=="cond_par"])

#columns selection

Rconv = Resistances_DF['RValue'][Resistances_DF["type"]=="conv"]
Rcond_ser = Resistances_DF['RValue'][Resistances_DF["type"]=="cond_ser"]
Rcond_par = (Resistances_DF['RValue'][Resistances_DF["type"]=="cond_par"])**-1

#Rtot calculation

Rtot_ser = Rconv.sum()+Rcond_ser.sum()
Rtot_par = Rcond_par.sum()
Rtot = Rtot_ser+Rtot_par
print "The total resistance is "+str(Rtot)+" °C/W"

#Heat transfer calculation (unit)

T_i = 20
T_o = -10
Q_unit = (T_i-T_o)/Rtot

#wall
H_wall = 5
W_wall = 3
W_wall= float(W_wall)
A_wall = H_wall*W_wall

#unit
H_unit = 0.25
W_unit = 1
A_unit = H_unit*W_unit

#Heat transfer calculation (wall)
Q_wall = Q_unit*A_wall/A_unit


print "the heat transfer through the unit results: " + str(Q_unit) + " W"
print "the heat transfer through the wall results: " + str(Q_wall) + " W"

