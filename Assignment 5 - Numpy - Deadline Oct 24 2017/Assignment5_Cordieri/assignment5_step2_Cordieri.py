# -*- coding: utf-8 -*-
import numpy as np
Materials_names=np.array(["WoodBevelLappedSliding","WoodFiberboardSheeting","GlassFiberInsulation","Woodstud","GypsumWallboard",
"InsideSurface","OutsideSurfaceWinter"])
Materials_Rvalues=np.array([0.14,0.23,2.45,0.63,0.079,0.12,0.03])
f=0.75
layerNames_Series=np.array(["WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard"])
R_series = np.zeros(layerNames_Series.size)
for layerName in layerNames_Series:
    R_series[layerNames_Series==layerName] = Materials_Rvalues[Materials_names==layerName]
layerNames_Par=np.array(["GlassFiberInsulation","Woodstud"])
R_par=np.zeros([layerNames_Par.size])
for layerName in layerNames_Par:
    R_par[layerNames_Par==layerName] = Materials_Rvalues[Materials_names==layerName]
R_seriesTot=R_series.sum()
R_parTot=R_par+R_seriesTot    
U_parTot=1/R_parTot    
U_overall=U_parTot[0]*f+U_parTot[1]*(1-f)
R_overall=1/U_overall
print "the total resistance is "+str(R_overall)+" m^2°C/W"          
    

    