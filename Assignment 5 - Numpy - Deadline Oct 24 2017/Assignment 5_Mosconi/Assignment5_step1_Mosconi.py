import numpy as np

layerNames=np.array(["insideSurface","foam","plaster","plaster","outsideSurface"])
layerType = np.array(["conv","cond","cond","cond","conv"])
layerLength=np.array([None,0.03,0.02,0.02,None])
layerConductivity=np.array([None,0.026,0.22,0.22,None])
layerH=np.array([10,None,None,None,25])

A=0.25 #area of unit
R_A=np.array([0.0,0.0,0.0,0.0,0.0])

R_A[layerType=="cond"]=layerLength[layerType=="cond"]/layerConductivity[layerType=="cond"]
R_A[layerType=="conv"]=1.0/layerH[layerType=="conv"]
R=np.divide(R_A,A)
resistanceSeries=np.sum(R)

layerNamesParallel=np.array(["plaster","brick","plaster"])
layerTypeParallel=np.array(["cond","cond","cond"])
layerHeightParallel=np.array([0.015,0.22,0.015])
layerConductivityParallel=np.array([0.22,0.72,0.22])
parallelLength=0.16

Rp=np.array([0.0,0.0,0.0])
inverseRp=np.array([0.0,0.0,0.0])
Rp=parallelLength/(layerConductivityParallel*layerHeightParallel)
inverseRp=1/Rp

trasmittanceParallel=np.sum(inverseRp)
resistanceParallel=1/trasmittanceParallel

totalResistance=np.array([resistanceSeries,resistanceParallel])
resistanceValue=np.sum(totalResistance)

Tin=20
Tout=-10
Qunit=(Tin-Tout)/resistanceValue
AreaWall=3*5
Qwall=Qunit*AreaWall/A

print("Total sum of resistance in series is "+str(resistanceSeries)+" W/m2K")
print("Total resistance in parallel is "+str(resistanceParallel)+" W/m2K")
print("Total resistance of the wall is "+str(resistanceValue)+" W/m2K")
print("Total heat flow rate through a unit-wall is "+str(Qunit)+" W")
print("Total heat flow rate through the wall is "+str(Qwall)+" W")
