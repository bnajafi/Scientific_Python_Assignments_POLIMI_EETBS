import pandas as pd

Ri= (["conv","series",0.25,None,None,10,0])
Rf= (["cond","series",0.25,0.03,0.026,None,0])
Rp1= (["cond","series",0.25,0.02,0.22,None,0])
Rpc1= (["cond","parallel",0.015,0.16,0.22,None,0])
Rb= (["cond","parallel",0.22,0.16,0.72,None,0])
Rpc2= (["cond","parallel",0.015,0.16,0.22,None,0])
Rp2= (["cond","series",0.25,0.02,0.22,None,0])
Ro= (["conv","series",0.25,None,None,25,0])


resistanceNames= ["insideSurface","foam","plaster1","thickPlaster1","brick",
                    "thickPlaster2","plaster2","outsideSurface"]
columnNames= ["type","config","area","length","k","h","Rvalue"]

ResistanceDF=pd.DataFrame([Ri,Rf,Rp1,Rpc1,Rb,Rpc2,Rp2,Ro],index=resistanceNames,columns=columnNames)

ResistanceDF["Rvalue"][ResistanceDF["type"]=="conv"]=1/ResistanceDF["h"]/ResistanceDF["area"]
ResistanceDF["Rvalue"][ResistanceDF["type"]=="cond"]=ResistanceDF["length"]/ResistanceDF["area"]/ResistanceDF["k"]

resistanceParallel=(1/ResistanceDF.loc["thickPlaster1","Rvalue"]+1/ResistanceDF.loc["brick","Rvalue"]+1/ResistanceDF.loc["thickPlaster2","Rvalue"])**(-1)
resistanceSeries=ResistanceDF["Rvalue"][ResistanceDF["config"]=="series"]
sumSeries=pd.Series.sum(resistanceSeries)

Rtot=sumSeries+resistanceParallel

A=0.25
Tin=20
Tout=-10
Qunit=(Tin-Tout)/Rtot
AreaWall=3*5
Qwall=Qunit*AreaWall/A

print("Total sum of resistance in series is "+str(sumSeries)+" W/m2K")
print("Total resistance in parallel is "+str(resistanceParallel)+" W/m2K")
print("Total resistance of the wall is "+str(Rtot)+" W/m2K")
print("Total heat flow rate through a unit-wall is "+str(Qunit)+" W")
print("Total heat flow rate through the wall is "+str(Qwall)+" W")
