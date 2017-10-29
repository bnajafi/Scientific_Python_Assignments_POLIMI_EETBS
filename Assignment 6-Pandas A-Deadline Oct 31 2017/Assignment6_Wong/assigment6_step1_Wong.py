# -*- coding: utf-8 -*-
import pandas as pd
rnames = ["inside","foam","plaster1","plaster2","outside","plaster1","plaster2","brick"]
rway= ["serie","serie","serie","serie","serie","parallel","parallel","parallel"]
rtypes = ["conv","cond","cond","cond","conv","cond","cond","cond"]
rh = [10,None,None,None,25,None,None,None]
rarea=[0.25,0.25,0.25,0.25,0.25,0.015,0.015,0.22]
rk=  [None,0.026,0.22,0.22,None,0.22,0.22,0.72]
rl= [None,0.03,0.02,0.02,None,0.16,0.16,0.16]
rvalues=[0,0,0,0,0,0,0,0]

rlist = [rway,rtypes,rh,rk,rl,rarea,rvalues]

rdataframe = pd.DataFrame(rlist,index=["way","type","h","k","L","area","rvalues"], columns=rnames)

Hw = 3 # wall height in m 
Ww = 5 # wall width in m
Awall = Hw*Ww # wall area
Tamb1 = 20 # room temperature in ºC
Tamb2 = -10 # outside temperature in ºC

rdataframe.loc["rvalues"][rdataframe.loc["type"]=="conv"]=1.0/(rdataframe.loc["h"][rdataframe.loc["type"]=="conv"]*rdataframe.loc["area"][rdataframe.loc["type"]=="conv"])
rdataframe.loc["rvalues"][rdataframe.loc["type"]=="cond"]=rdataframe.loc["L"][rdataframe.loc["type"]=="cond"]/(rdataframe.loc["k"][rdataframe.loc["type"]=="cond"]*rdataframe.loc["area"][rdataframe.loc["type"]=="cond"])

rparallel=1/((1/rdataframe.loc["rvalues"][rdataframe.loc["way"]=="parallel"]).sum())
Rtotal=rparallel+(rdataframe.loc["rvalues"][rdataframe.loc["way"]=="serie"]).sum()


print "The total resistance is " + str(Rtotal) + " ºC/W"

Qu = (Tamb1 - Tamb2)/Rtotal # we calculate the heat flux in the unit in W

print "The heat flux in a unit is " + str(Qu) + " W"

#we scale the heat flux using the areas

Q = Qu * Awall/0.25 # in W
print "The total heat flux is " + str(Q) + " W"