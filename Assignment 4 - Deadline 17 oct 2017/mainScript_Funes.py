# -*- coding: utf-8 -*-


cd "D:\MIS DOCUMENTOS\Documents\Maestría\Energy Building Systems"
pwd

import wallCalculations_Funes as UC

Materials_In_Series = ["insideSurface","outsideSurfaceWinter","gypsumWallboard13mm","woodFiberboard13mm","woodBevel200mm"]
Materials_In_Parallel = ["woodStuds90mm","glassFiber25mm"]
door = ["insideSurface","outsideSurfaceWinter","wood_25mm"]
roof = ["ClayTile_100mm","woodFiberboard_13mm","woodStud_90mm","gypsumWallboard13mm"]

Anet_wall = 105.8
Anet_wall=float(Anet_wall)
Aroof = float(200)
Adoor = float(2.2)
Tdb_winter = float(-4.8)
Tin_winter = float(20)
DeltaT = float(Tin_winter-Tdb_winter)

UC.wallCalc_withParallel(Materials_In_Series,Materials_In_Parallel,0.7)
Utot = 0.473684

UC.wallCalc_OnlyInSeries(door)
Udoor = 1.694915 

UC.wallCalc_OnlyInSeries(roof)
Uroof = 0.893655

HFnet_wall = Anet_wall*DeltaT
Qnet_wall = Utot*HFnet_wall
print "The total heat transfered through the walls is :"+str(Qnet_wall)+" (W)"

HFroof=Aroof*DeltaT
Qroof = Uroof*HFroof
print "The total heat transfered through the roof is :"+str(Qroof)+" (W)"

HFdoor=Adoor*DeltaT
Qdoor = Uroof*HFdoor
print "The total heat transfered through the door is :"+str(Qdoor)+" (W)"

Q=Qnet_wall+Qroof+Qdoor
print "The total heating load from opaque surfaces is :"+str(Qroof)+" (W)"