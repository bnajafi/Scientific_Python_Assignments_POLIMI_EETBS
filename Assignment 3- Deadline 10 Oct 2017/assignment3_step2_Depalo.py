# -*- coding: utf-8 -*-
#Assignment 3 - step 2

materialSeries=['woodBevel','woodFiberboard13','gypsumWallboard13']
materialParallel=['GlassFiber90','woodStud90']

def wall_calc(materialSeries,materialParallel,f):
    
    "The function receives 3 inputs: list of layers in series, list of the two layers in parallel, and the ratio between the area of the first layer in parallel and the total area. It returns a dictionary which includes the thermal resistances of all layers, the total resistance and the total U of the wall."
    
    materialsLibrary={'outSurface':0.03,'woodBevel':0.14,'woodFiberboard13':0.23,'GlassFiber90':2.45,'woodStud90':0.63,'gypsumWallboard13':0.079,'inSurface':0.12}    #dictionary 'material':unit thermal resistance
    
    surfaces = ['outSurface','inSurface']      #inner and outer surfaces of the wall
    
    totalWallSeries=surfaces+ materialSeries
    
    f1=float(f)     #ratio between the area of the glass fiber parallel layer and the total area of the wall
    f2=1-f1       #ratio between the area of the glass fiber parallel layer and the total area of the wall
    
    dic={}
    Rseries=0
    for anymaterial in totalWallSeries:
        dic={anymaterial:materialsLibrary[anymaterial]}
        Rseries=Rseries+materialsLibrary[anymaterial]     #sum of all the resistances of the materials in the list of layers in series
    
    RtotSeries=[]
    for anymaterial in materialParallel:
        Rtot=Rseries+materialsLibrary[anymaterial]     #sum of the previous total series resistance and the resistance of one of the 2 layers in parallel
        RtotSeries.append(Rtot)
        
    U1=1/RtotSeries[0]     #U value in the case of glass fiber
    U2=1/RtotSeries[1]      #U value in the case of wood stud
    
    Utot=f1*U1+f2*U2     #total U value considering the respective proportions for glass fiber and wood stud
    Rtot=1/Utot          #total resistance    
    
    A=100     #total area of the wall [m^2]
    Tin=22    #inner temperature
    Tout=-2   #outer temperature
    
    Q=A*Utot*(Tin-Tout)    #heat flux through the wall
    
    RallLayers = []
    for anylayer in totalWallSeries+materialParallel:
        Rlayer = materialsLibrary[anylayer]
        RallLayers.append(Rlayer)
    results = {"Resistance value of all layers":RallLayers, "Total resistance":Rtot,'Total U':Utot}
    return results