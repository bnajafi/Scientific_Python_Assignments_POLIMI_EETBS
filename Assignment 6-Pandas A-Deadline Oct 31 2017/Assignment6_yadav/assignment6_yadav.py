# -*- coding: utf-8 -*-
import pandas as pd


Resistances_DF_s= pd.DataFrame([["conv","cond","cond","cond","conv"],[10,None,None,None,25],[None,0.026,0.22,0.22,None],[None,0.03,0.02,0.02,None],[0.25,0.25,0.25,0.25,0.25],[0,0,0,0,0]],index=["types","h","k","L","A","Rvalue1"],columns=["R1","R2","R3","R4","R5"])
Resistances_DF_s
##Resistances_DF_s.loc["h",:]
###Resistances_DF_s=pd.DataFrame(pd.zeros(5))
Resistances_DF_s.loc["Rvalue1"][Resistances_DF_s.loc["types"]=="conv"]=1.0/(Resistances_DF_s.loc["h"][Resistances_DF_s.loc["types"]=="conv"]*Resistances_DF_s.loc["A"][Resistances_DF_s.loc["types"]=="conv"])
Resistances_DF_s.loc["Rvalue1"][Resistances_DF_s.loc["types"]=="cond"]=Resistances_DF_s.loc["L"][Resistances_DF_s.loc["types"]=="cond"]/(Resistances_DF_s.loc["k"][Resistances_DF_s.loc["types"]=="cond"]*Resistances_DF_s.loc["A"][Resistances_DF_s.loc["types"]=="cond"])
Resistances_DF_s
###Resistances_Rtot1=Resistances_DF_s.sum()

Tot_R_Series = Resistances_DF_s.loc["Rvalue1","R1"] + Resistances_DF_s.loc["Rvalue1","R2"] + 2 * Resistances_DF_s.loc["Rvalue1","R3"] + Resistances_DF_s.loc["Rvalue1","R4"]


Resistances_DF_p= pd.DataFrame([["cond","cond","cond"],[0.22,0.72,0.22],[0.16,0.16,0.16],[0.015,0.22,0.015],[0,0,0]],index=["types","k","L","A","Rvalue2"],columns=["R6","R7","R8"])
Resistances_DF_p
##Resistances_DF_s.loc["h",:]
###Resistances_DF_s=pd.DataFrame(pd.zeros(5))
Resistances_DF_p.loc["Rvalue2"][Resistances_DF_p.loc["types"]=="cond"]=Resistances_DF_p.loc["L"][Resistances_DF_p.loc["types"]=="cond"]/(Resistances_DF_p.loc["k"][Resistances_DF_p.loc["types"]=="cond"]*Resistances_DF_p.loc["A"][Resistances_DF_p.loc["types"]=="cond"])
Resistances_DF_p
###Resistances_Rtot1=Resistances_DF_s.sum()


Tot_R_Parallel =  1/(2/Resistances_DF_p.loc["Rvalue2","R6"] + 1/ Resistances_DF_p.loc["Rvalue2","R7"])


R_tot=Tot_R_Series+Tot_R_Parallel
print " Resistance of wall(unit width) = " + str(round(R_tot,4)) + " K/W"

## calculation of heat transfer rate-
Tin = 20  # [°C]
Tout = -10  # [°C]

AUnit = 1*0.25  # [m2]
QUnit = (Tin - Tout)/R_tot  # [W]

AWall = 3 * 5  # [m2]
QWall =  QUnit * (AWall/AUnit)  # [W]

print "the total heat tranfer rate through  the wall is = " +str(round(QWall,4)) + "W"



