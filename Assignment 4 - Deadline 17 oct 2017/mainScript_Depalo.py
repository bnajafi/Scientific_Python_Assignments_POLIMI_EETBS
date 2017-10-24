#Assignment 4 - Depalo

import os
os.chdir("M:\Poli\EETBS Energy Environmental Tech Building Systems")
import wallCalculations_Depalo as WC

materialSeriesWall=['woodBevel','woodFiberboard13','gypsumWallboard13','commonBrick100']
materialParallelWall=['GlassFiber90','woodStud90']
materialDoor=['wood50']
materialRoof=['GlassFiber25','woodFiberboard13','urethaneRigidFoam25','faceBrick200','acousticTile','concreteLight200','clayTile100','commonBrick100']

resultsWall=WC.wallCalc_withParallel(materialSeriesWall,materialParallelWall,0.7)
resultsDoor=WC.wallCalc_onlyInSeries(materialDoor)
resultsRoof=WC.wallCalc_onlyInSeries(materialRoof)
Uwall=resultsWall['Total U']
Udoor=resultsDoor['Total U']
Uroof=resultsRoof['Total U']

Awall=105.8   #total area of the walls [m^2]
Adoor=2.2     #area of the door
Aroof=200     #area of the roof
Tin=20        #project winter inner temperature
Tout=-4.8     #project winter outer temperature
deltaT=Tin-Tout
HFwall=Uwall*deltaT     #heating factors
HFdoor=Udoor*deltaT
HFroof=Uroof*deltaT
Qwall=Awall*HFwall    #heat load through the wall
Qdoor=Adoor*HFdoor    #heat load through the door
Qroof=Aroof*HFroof    #heat load through the roof

Qtot=Qwall+Qdoor+Qroof

print '\nThe U value for the walls is '+str(Uwall)+' W/m^2*K, the U value for the door is '+str(Udoor)+' W/m^2*K, the U value for the roof is ' +str(Uroof)+' W/m^2*K.\n\n'+'The heat flux through the wall is ' +str(Qwall) + ' W, the flux through the door is ' + str(Qdoor) + ' W, the flux through the roof is ' + str(Qroof) + ' W and the total flux through opaque surfaces is '+str(Qtot) + ' W.\n\n'