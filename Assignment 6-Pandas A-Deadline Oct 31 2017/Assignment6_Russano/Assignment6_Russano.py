# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.6 Date: 29/10/2017
#One dimensional problem:
#Example D: Heat loss through a composite wall
#Solution by Pandas:                                                    

#Import pandas:
import pandas as pd
#I initialize the list of resistances:
R1_list = ["conv",10,None,None,0.25,0]
R2_list = ["condser",None,0.03,0.026,0.25,0]
R3_list = ["condser",None,0.02,0.22,0.25,0]
R4_list = ["condser",None,0.02,0.22,0.25,0]
R5_list = ["condpar",None,0.16,0.22,0.015,0]
R6_list = ["condpar",None,0.16,0.72,0.22,0]
R7_list = ["condpar",None,0.16,0.22,0.015,0]
R8_list = ["conv",25,None,None,0.25,0]
#Resistances in series:
resistance_names = ["Rin","Rser1","Rser2","Rser3","Rpar1","Rpar2","Rpar3","Rout"]
column_names=["type","h","L","k","Area","RValue"]
#I define the DataFrame:
Res_DF=pd.DataFrame([R1_list,R2_list,R3_list,R4_list,R5_list,R6_list,R7_list,R8_list],index=resistance_names,columns=column_names)
#Now i calculate R-values of convective and conductive resistances (in series and in parallel):
Res_DF["RValue"][Res_DF["type"]=="conv"]=1.0/(Res_DF["h"][Res_DF["type"]=="conv"]*Res_DF["Area"][Res_DF["type"]=="conv"])
Res_DF["RValue"][Res_DF["type"]=="condser"]=Res_DF["L"][Res_DF["type"]=="condser"]/(Res_DF["k"][Res_DF["type"]=="condser"]*
Res_DF["Area"][Res_DF["type"]=="condser"])
Res_DF["RValue"][Res_DF["type"]=="condpar"]=Res_DF["L"][Res_DF["type"]=="condpar"]/(Res_DF["k"][Res_DF["type"]=="condpar"]
*Res_DF["Area"][Res_DF["type"]=="condpar"])

#Calculating of the conductive resistance in series:
R_cond_ser=Res_DF["RValue"][Res_DF["type"]=="condser"].sum()
#Calculating of the conductive resistance in parallel:
R_cond_par=((1.0/(Res_DF["RValue"][Res_DF["type"]=="condpar"])).sum())**-1
#Calculating of the convective resistance:
R_conv=Res_DF["RValue"][Res_DF["type"]=="conv"].sum()
#The total resistance is:
Res_tot=R_cond_ser+R_cond_par+R_conv
print "The total resistance of the wall is:" +str(Res_tot)+ "°C/W"
#Defining the temperature:
T1 = 20
T2 = -10
A_unit = 0.25
A_tot = 15
Q_unit = (T1-T2)/Res_tot
Q_wall = Q_unit*(A_tot/A_unit)
print "The total heat flux through the wall is "+str(Q_wall)+" W"












