# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.5 (Step2) Date: 23/10/2017
#One dimensional problem:
#Example 1
#Solution by Numpy:
import numpy as np
#I define an array with the names of common components used in buildings:
materials_names= np.array(["Outside_surface_Summer", "Outside_surface_Winter","Inside_surface",
"Insulation_Glass_Fiber", "WoodStud", "WoodFiberboard13mm", 
"Stucco_25mm", "WoodBevel_13*200", "Gypsum_13mm"])
#I define an array with the thermal resistance (R-value) of common components used in buildings:
materials_Rvalues =np.array([0.044,0.030,0.12,2.45,0.63,0.23,0.037,0.14,0.079])
#For the material in series:
Series_myWall = np.array(["Outside_surface_Winter","WoodBevel_13*200","WoodFiberboard13mm","Gypsum_13mm","Inside_surface"]) 
Rseries_myWall = np.zeros(5)

for material in Series_myWall:
    Rseries_myWall[Series_myWall==material] = materials_Rvalues[materials_names==material]
    
U_series=1/(Rseries_myWall.sum())
#For the parallel:
Parallel_myWall = np.array(["Insulation_Glass_Fiber","WoodStud"]) 
Rparallel_myWall = np.zeros(2)

for material in Parallel_myWall:
    Rparallel_myWall[Parallel_myWall==material] = materials_Rvalues[materials_names==material]
    
U_parallel=1/Rparallel_myWall
#define the ratio as float:
Ratio=0.75
#Calculating the U_overall of my wall:
U_overall=Ratio*(1/(Rseries_myWall.sum()+Rparallel_myWall[0]))+(1-Ratio)*(1/(Rseries_myWall.sum()+Rparallel_myWall[1]))
print "The overall heat transfer coefficient is:" +str(U_overall)+ "W/m^2*degC"
R_overall = 1/U_overall
print "The total resistance of the wall is: "+str(R_overall)+ "degC/m^2*W"

