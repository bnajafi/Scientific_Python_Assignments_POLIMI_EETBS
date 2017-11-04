import numpy as np

f_ins = 0.75 #insulated portion of wall in percentage

Tin = 22.0
Tout = -2.0

H = 2.5 #height
P = 50.0 #perimeter
fin_perc = 0.2 #percentage of windows

materials_names= np.array(["stucco_13mm","FaceBrick_100mm","BuildingPaper","Plywood_13mm","insideSurface","outsideSurfaceSummer",
"outsideSurfaceWinter","woodFiberboard_13mm","WoodBevelLappedSiding","glassFiberInsulation_90mm","woodStud_38x90mm","gypsiumWallboard_13mm"])
materials_Rvalues =np.array([0.023,0.075,0.011,0.11,0.12,0.044,0.03,0.23,0.14,2.45,0.63,0.079])

layersSeries = np.array(["insideSurface","WoodBevelLappedSiding","woodFiberboard_13mm","gypsiumWallboard_13mm","outsideSurfaceWinter"]) 
layersParallel = np.array(["glassFiberInsulation_90mm","woodStud_38x90mm"])

RValues_series = np.zeros(layersSeries.size) 
RValues_parallel = np.zeros(layersParallel.size) 

for layerName in layersSeries:
    RValues_series[layersSeries == layerName] = materials_Rvalues[materials_names == layerName]
for layerName in layersParallel:
    RValues_parallel[layersParallel == layerName] = materials_Rvalues[materials_names == layerName]

Rtot_series = RValues_series.sum()
Rtot_ins = Rtot_series + float(RValues_parallel[layersParallel == "glassFiberInsulation_90mm"])
Rtot_wood = Rtot_series + float(RValues_parallel[layersParallel == "woodStud_38x90mm"])

Utot_ins = 1/Rtot_ins
Utot_wood = 1/Rtot_wood

Utot = f_ins*Utot_ins + (1-f_ins)*Utot_wood
Rtot = 1/Utot

print "the total resistance of the wall is " + str(Rtot) + " (degC m2)/W"

Qwall = Utot*(H*P*(1-fin_perc))*(Tin-Tout)

print "the total heat flux through the wall is " + str(Qwall) + " W"