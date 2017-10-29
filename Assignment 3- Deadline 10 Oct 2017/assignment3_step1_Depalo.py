# -*- coding: utf-8 -*-
#Assignment 3 - step 1

materialsLibrary={'outSurface':0.03,'woodBevel':0.14,'woodFiberboard13':0.23,'GlassFiber90':2.45,'woodStud90':0.63,'gypsumWallboard13':0.079,'inSurface':0.12}    #dictionary 'material':unit thermal resistance
surfaces = ['outSurface','inSurface']      #inner and outer surfaces of the wall
materialSeries=['woodBevel','woodFiberboard13','gypsumWallboard13']    #list with material names of layers in series
totalWallSeries=surfaces+ materialSeries
materialParallel=['GlassFiber90','woodStud90']      #list with material names of layers in parallel
fGlassFiber=float(0.75)     #ratio between the area of the glass fiber parallel layer and the total area of the wall
fWoodStud=float(0.25)       #ratio between the area of the glass fiber parallel layer and the total area of the wall

Rseries=0
for anymaterial in totalWallSeries:
    Rseries=Rseries+materialsLibrary[anymaterial]     #sum of all the resistances of the materials in the list of layers in series
print 'The total unit resistance for the layers in series is ' + str(Rseries) + ' m^2*°C/W.'+'\n\n'

RtotSeries=[]
for anymaterial in materialParallel:
    Rtot=Rseries+materialsLibrary[anymaterial]     #sum of the previous total series resistance and the resistance of one of the 2 layers in parallel
    RtotSeries.append(Rtot)
    print 'The total unit resistance of the wall with ' + anymaterial + ' is ' + str(Rtot) + ' m^2*°C/W.\n\n'

Ufiber=1/RtotSeries[0]     #U value in the case of glass fiber
Ustud=1/RtotSeries[1]      #U value in the case of wood stud

Utot=fGlassFiber*Ufiber+fWoodStud*Ustud     #total U value considering the respective proportions for glass fiber and wood stud

print 'The U value for the glass fiber case is ' + str(Ufiber) + ' W/m^2*°C, the U value for the wood stud case is ' + str(Ustud) + ' W/m^2*°C, the total U value is ' + str(Utot) + ' W/m^2*°C. \n\n'

A=100     #total area of the wall [m^2]
Tin=22    #inner temperature
Tout=-2   #outer temperature

Q=A*Utot*(Tin-Tout)    #heat flux through the wall

print 'The heat flux through the wall is ' +str(Q) + ' W.\n\n'