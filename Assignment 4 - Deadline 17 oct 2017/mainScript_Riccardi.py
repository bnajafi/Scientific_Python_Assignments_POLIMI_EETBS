# -*- coding: utf-8 -*-
#assignment 4
#assumptions: 
    #-season:winter
    #-DeltaT=20°C

import os
os.chdir("C:\Users\Luca\Dropbox\git_fork\Assignment4")
import WallCalculations_Riccardi as WC
Tout=-4.8
Tin=20
DeltaT=Tin-Tout
Material_library={"WoodBevel":0.14,"WoodFiberboard_13mm":0.23,"Wood_50mm":0.22*50/25,"GlassFiberIns_90mm":2.45,
"WoodStud_38x90mm2":0.63,"GypsumWallboard_13mm":0.079,"CommonBrick_100mm":0.12,"AcousticTile":0.32,
"BuildingPaper":0.011,"Plywood_13mm":0.11,"Stucco_25mm":0.037,"OutsideSurface":0.030,"InsideSurface":0.12,"AsphaltShingle":0.077}
ConvRes=["OutsideSurface","InsideSurface"]
Door=["Wood_50mm"]
WallsSeries=["WoodBevel","WoodFiberboard_13mm","GypsumWallboard_13mm"]
WallsParallel=["GlassFiberIns_90mm","WoodStud_38x90mm2"]
Ceiling=["GypsumWallboard_13mm","GypsumWallboard_13mm","CommonBrick_100mm","AsphaltShingle"]
AreaFraction=0.7

ResultsWalls=WC.wallCalc_withParallel(Material_library,WallsSeries,WallsParallel,ConvRes,AreaFraction)
ResultsDoor=WC.wallCalc_onlyInSeries(Material_library,Door,ConvRes)
ResultsCeiling=WC.wallCalc_onlyInSeries(Material_library,Ceiling,ConvRes)

Awalls=144
Adoor=2.2
Aceiling=200
Qwalls=Awalls*ResultsWalls["TotalUFactor"]*DeltaT
print "Qwalls = "+str(Qwalls)+" W"
Qdoor=Adoor*ResultsDoor["TotalUFactor"]*DeltaT
print "Qdoor = "+str(Qdoor)+" W"
Qceiling=Aceiling*ResultsCeiling["TotalUFactor"]*DeltaT
print "Qceiling = "+str(Qceiling)+" W"