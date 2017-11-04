# ASSIGNMENT 6 #

import pandas as pd

R1_list= ["conv","series",10,None,None,0.25,0,0]
Rf_list= ["cond","series",None,0.03,0.026,0.25,0,0]
Rp1_list= ["cond","series",None,0.02,0.22,0.25,0,0]
Rp2_list= ["cond","series",None,0.02,0.22,0.25,0,0]
Rpo1_list= ["cond","parallel",None,0.16,0.22,0.015,0,0]
Rpo2_list= ["cond","parallel",None,0.16,0.22,0.015,0,0]
Rb_list= ["cond","parallel",None,0.16,0.72,0.22,0,0]
R2_list= ["conv","series",25,None,None,0.25,0,0]


resistances_name= ["R1","Rf","Rp1","Rp2","Rpo1","Rpo2","Rb","R2"]
columns_name= ["type","type2","h","L","k","Area","Rvalue","Uvalue"]


Resistances_DF= pd.DataFrame([R1_list,Rf_list,Rp1_list,Rp2_list,Rpo1_list,Rpo2_list,Rb_list,R2_list],index= resistances_name,columns=columns_name) 

Resistances_DF["Rvalue"][Resistances_DF["type"]=="conv" ] = 1.0/(Resistances_DF["h"]*Resistances_DF["Area"])  # convective resistances' calculation

Resistances_DF["Rvalue"][Resistances_DF["type"]=="cond" ] = Resistances_DF["L"]/(Resistances_DF["k"]*Resistances_DF["Area"]) # conductive resistances' calculations 

Resistances_DF["Uvalue"] = 1.0/Resistances_DF["Rvalue"]  # U calculations


Rtot_series= Resistances_DF["Rvalue"][Resistances_DF["type2"]=="series" ].sum()  

Utot_parallel= Resistances_DF["Uvalue"][Resistances_DF["type2"]== "parallel"].sum()
Rtot_parallel= 1.0/Utot_parallel

R_tot = Rtot_series+Rtot_parallel

T_in = 20
T_out = -10
A_wall = 15

Q_wall = ((T_in-T_out)/R_tot)*(A_wall/0.25)

print "The total resistance of the wall is "+str(R_tot)+ " degC/W \n"
print "The rate of heat transfer through the wall is "+str(Q_wall)+ "W" 
