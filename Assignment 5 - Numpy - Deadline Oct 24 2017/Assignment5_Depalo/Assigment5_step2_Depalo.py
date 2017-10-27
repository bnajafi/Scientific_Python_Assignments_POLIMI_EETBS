# -*- coding: utf-8 -*-
#Assignment 5 - step 2

import numpy as np

materials_names=np.array(['outSurface','woodBevel','woodFiberboard13','GlassFiber90','woodStud90','gypsumWallboard13','inSurface'])
materials_Rvalues=np.array([0.03,0.14,0.23,2.45,0.63,0.079,0.12])

layerNames_myWall_series = np.array(['outSurface','inSurface','woodBevel','woodFiberboard13','gypsumWallboard13'])
layerNames_myWall_parallel = np.array(['GlassFiber90','woodStud90'])
fGlassFiber=float(0.75)
RValue_myWall_series = np.zeros(layerNames_myWall_series.size)
RValue_myWall_parallel = np.zeros(layerNames_myWall_parallel.size)

for layerName in layerNames_myWall_series:
    RValue_myWall_series[layerNames_myWall_series==layerName] = materials_Rvalues[materials_names==layerName]
    
Rvalue_tot_series=RValue_myWall_series.sum()

for layerName in layerNames_myWall_parallel:
    RValue_myWall_parallel[layerNames_myWall_parallel==layerName] = materials_Rvalues[materials_names==layerName]

Rvalue_tot_fiber=RValue_myWall_parallel[layerNames_myWall_parallel=='GlassFiber90']+Rvalue_tot_series
Rvalue_tot_stud=RValue_myWall_parallel[layerNames_myWall_parallel=='woodStud90']+Rvalue_tot_series
Ufiber=1/Rvalue_tot_fiber
Ustud=1/Rvalue_tot_stud

Utot=fGlassFiber*Ufiber+(1-fGlassFiber)*Ustud
A=100     #total area of the wall [m^2]
Tin=22    #inner temperature
Tout=-2   #outer temperature

Q=A*Utot*(Tin-Tout)    #heat flux through the wall

print 'The heat flux through the wall is ' +str(Q) + ' W.\n\n'