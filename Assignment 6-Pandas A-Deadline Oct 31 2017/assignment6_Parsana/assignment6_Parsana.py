# -*- coding: utf-8 -*-
#Assignment:6
#Name:Shashwat Parsana

import pandas as pd

#Define the lists
List_Res1 = ["conv","series", 10, None, None, 0.25, 0]
List_Res2 = ["cond","series", None, 0.026, 0.03, 0.25, 0]
List_Res3= ["cond","series",None, 0.22, 0.02, 0.25, 0]
List_Res4 = ["cond","series",None, 0.22, 0.02, 0.25, 0]
List_Res5 = ["cond","parallel", None, 0.72, 0.16, 0.22, 0]
List_Res6 = ["cond","parallel", None, 0.22, 0.16, 0.015, 0]
List_Res7 = ["cond","parallel", None, 0.22, 0.16, 0.015, 0]
List_Res8 = ["conv","series", 25, None, None, 0.25, 0]

name_column=["type","SP_type","h","k","L","A","Res_value"]
name_resistance=["indoor","foam","Plaster_1","Plaster_2","Brick","Plaster_11","Plaster_22","outdoor"]

#DataFrame
resistance_DF=pd.DataFrame([List_Res1,List_Res2,List_Res3,List_Res4,List_Res5,List_Res6,List_Res7,List_Res8], index=name_resistance, columns=name_column)

#Finding R values for each material
resistance_DF["Res_value"][resistance_DF["type"]=="cond"]=(resistance_DF["L"])/(resistance_DF["k"]*resistance_DF["A"])
resistance_DF["Res_value"][resistance_DF["type"]=="conv"]=1.0/(resistance_DF["h"]*resistance_DF["A"])

#Summing Series and Parallel Resistances
series_Rtot=resistance_DF["Res_value"][resistance_DF["SP_type"]=="series"].sum()
parallel_Rtot_temp=(1/resistance_DF["Res_value"][resistance_DF["SP_type"]=="parallel"]).sum()
parallel_Rtot=1/parallel_Rtot_temp

Rtot=series_Rtot+parallel_Rtot

print '\n'
print resistance_DF
print '\n'
print 'The resistance in Series is '+str(series_Rtot)+' [degC/W]'
print 'The resistance in Parallel is '+str(parallel_Rtot)+ ' [degC/W]'
print 'Adding both the resistances,we get the total resistance which is '+str(Rtot)+' [degC/W]'

#Indoor Outdoor Temp.
T1=20
T2 = -10
#Additonal data and calculations for Q of wall
Q=(T1-T2)/Rtot
wall_height=3
wall_width=5
wall_A=0.25

wall_Q=Q*wall_height*wall_width/wall_A

print '\n'
print "After calculations,total heat loss from that specific wall is "+str(wall_Q)+ " [W]"
print '\n'