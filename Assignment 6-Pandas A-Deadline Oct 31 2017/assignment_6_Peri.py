# -*- coding: utf-8 -*-
import pandas as pd

#name=["type",h,thickness,k,r_value]
R1_series=["conv",10,None,None,0] 
R2_series=["cond",None,0.03,0.026,0]
R3_series=["cond",None,0.02,0.22,0]
R4_series=["cond",None,0.02,0.22,0]
R5_series=["conv",25,None,None,0]
A=0.25
resistance_names=["R1_s","R2_s","R3_s","R4_s","R5_s"]
column_names=["type","h","t","k","rvalue"]

#creates a dataframe
R_series_DF=pd.DataFrame([R1_series,R2_series,R3_series,R4_series,R5_series],index=resistance_names,columns=column_names) 

#calculates conv. resistances
R_series_DF["rvalue"][R_series_DF["type"]=="conv"]=1.0/(R_series_DF["h"][R_series_DF["type"]=="conv"]*A)

#calculates cond. resistance
R_series_DF["rvalue"][R_series_DF["type"]=="cond"]=R_series_DF["t"][R_series_DF["type"]=="cond"]/(R_series_DF["k"][R_series_DF["type"]=="cond"]*A)
#now let's sum them all
R_s=R_series_DF["rvalue"].sum()

#r_parallel

R1_paral=["cond",None,0.16,0.22,0.015,0]
R2_paral=["cond",None,0.16,0.72,0.22,0]
R3_paral=["cond",None,0.16,0.22,0.015,0]

resistance_names=["R1_p","R2_p","R3_p"]
column_names=["type","h","t","k","area","rvalue"]

R_paral_DF=pd.DataFrame([R1_paral,R2_paral,R3_paral],index=resistance_names,columns=column_names) 
R_paral_DF["rvalue"][R_paral_DF["type"]=="cond"]=R_paral_DF["t"][R_paral_DF["type"]=="cond"]/(R_paral_DF["k"][R_paral_DF["type"]=="cond"]*R_paral_DF["area"][R_paral_DF["type"]=="cond"])

G_paral_step1=1.0/(R_paral_DF["rvalue"]) 
G_paral_step2=G_paral_step1.sum()
R_paral=1.0/G_paral_step2

Rtot=R_paral+R_s


print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
print "the total thermal resistance of the wall is: "+str(Rtot)+" degC/W"
print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"

T_out=-10
T_in=20
DT=T_in-T_out

A_wall=3*5

Q_tot=DT*A_wall/(Rtot*0.25)

print "\n The total heat transfer of the wall is: " +str(Q_tot)+" W"
print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"

