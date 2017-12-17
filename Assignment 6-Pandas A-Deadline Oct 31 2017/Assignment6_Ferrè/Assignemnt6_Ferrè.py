# -*- coding: utf-8 -*-
import pandas as pd

R1_conv_list = ["conv",10,None,None,0.25, 0]
R2_serie_list = ["serie",None,0.026,0.03,0.25, 0]
R3_serie_list = ["serie",None,0.22,0.02,0.25, 0]
R4_serie_list = ["serie",None,0.22,0.02,0.25, 0]
R5_conv_list = ["conv",25,None,None,0.25, 0]
R1_parallel_list = ["parallel",None,0.22,0.16,0.015, 0]
R2_parallel_list = ["parallel",None,0.72,0.16,0.22, 0]
R3_parallel_list = ["parallel",None,0.22,0.16,0.015, 0]

resistences_name=["R1conv","R2serie","R3serie","R4serie","R1parallel","R2parallel","R3parallel","R5conv"]
colums_name=["type","h","k","L","A","RValue"]

Resistences_DF = pd.DataFrame([R1_conv_list,R2_serie_list,R3_serie_list,R4_serie_list,R1_parallel_list,R2_parallel_list,R3_parallel_list,R5_conv_list],index=resistences_name,columns=colums_name)

Resistences_DF["RValue"][Resistences_DF["type"]=="conv"]=1.0/(Resistences_DF["h"][Resistences_DF["type"]=="conv"]*Resistences_DF["A"][Resistences_DF["type"]=="conv"])
Resistences_DF["RValue"][Resistences_DF["type"]=="serie"]=Resistences_DF["L"][Resistences_DF["type"]=="serie"]/(Resistences_DF["k"][Resistences_DF["type"]=="serie"]*Resistences_DF["A"][Resistences_DF["type"]=="serie"])
Resistences_DF["RValue"][Resistences_DF["type"]=="parallel"]=Resistences_DF["L"][Resistences_DF["type"]=="parallel"]/(Resistences_DF["k"][Resistences_DF["type"]=="parallel"]*Resistences_DF["A"][Resistences_DF["type"]=="parallel"])

RValue_serie = Resistences_DF["RValue"][Resistences_DF["type"]=="serie"].sum() + Resistences_DF["RValue"][Resistences_DF["type"]=="conv"].sum()
RValue_parallel =(1/Resistences_DF["RValue"][Resistences_DF["type"]=="parallel"]).sum()

RValue_tot = RValue_serie+RValue_parallel
print "Total resistence is: " +str(RValue_tot) + "°C/W"