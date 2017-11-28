# -*- coding: utf-8 -*-
#assignment 5 - step 2
import numpy as np
Materials_names=np.array(["WoodBevel","WoodFiberboard_13mm","GlassFiberIns_90mm","WoodStud_38x90mm2","GypsumWallboard_13mm","CommonBrick_100mm","AcousticTile",
"BuildingPaper","Plywood_13mm","OutsideSurface","InsideSurface"])
Materials_Rvalues=np.array([0.14,0.23,2.45,0.63,0.079,0.12,0.32,0.011,0.11,0.030,0.12])

Series=np.array(["WoodBevel","WoodFiberboard_13mm","GypsumWallboard_13mm","OutsideSurface","InsideSurface"])
Parallel=np.array(["GlassFiberIns_90mm","WoodStud_38x90mm2"])

Series_Rvalues=np.zeros(Series.size)
Parallel_Rvalues=np.zeros(Parallel.size)

for layerName in Series:
    Series_Rvalues[Series==layerName] = Materials_Rvalues[Materials_names==layerName]
    
for layerName in Parallel:
    Parallel_Rvalues[Parallel==layerName] = Materials_Rvalues[Materials_names==layerName]

Rtot_series=Series_Rvalues.sum()
Rtot_WithParallel=np.zeros(Parallel.size)
for any in [0,Parallel.size-1]:
    Rtot_WithParallel[any]=Rtot_series+Parallel_Rvalues[any]
    
Ratio=0.75

U_overall=Ratio*1/Rtot_WithParallel[0]+(1-Ratio)*1/Rtot_WithParallel[1]
print "The overall U factor of the wall is: "+str(U_overall)+" [W/(m^2*°c)]"


    
    