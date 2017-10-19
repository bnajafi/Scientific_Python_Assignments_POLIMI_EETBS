# -*- coding: utf-8 -*-
#Assignment 4 - Depalo

def wallCalc_withParallel(materialSeries,materialParallel,f):
    
    "The function receives 3 inputs: list of layers in series, list of the two layers in parallel, and the ratio between the area of the first layer in parallel and the total area. It returns a dictionary which includes the thermal resistances of all layers, the total resistance and the total U of the wall."
    
    materialsLibrary={'outSurface':0.03,'woodBevel':0.14,'woodFiberboard13':0.23,'GlassFiber90':2.52,'woodStud90':0.63,'gypsumWallboard13':0.079,'inSurface':0.12,'wood50':0.44,'commonBrick100':0.12,'GlassFiber25':0.70,'urethaneRigidFoam25':0.98,'faceBrick200':0.15,'acousticTile':0.32,'concreteLight200':1.17,'clayTile100':0.18}    #dictionary 'material':unit thermal resistance
    
    surfaces = ['outSurface','inSurface']      #inner and outer surfaces of the wall
    
    totalWallSeries=surfaces+ materialSeries
    
    f1=float(f)     #ratio between the area of the glass fiber parallel layer and the total area of the wall
    f2=1-f1       #ratio between the area of the glass fiber parallel layer and the total area of the wall
    
    Rseries=0
    for anymaterial in totalWallSeries:
        Rseries=Rseries+materialsLibrary[anymaterial]     #sum of all the resistances of the materials in the list of layers in series
    
    RtotSeries=[]
    for anymaterial in materialParallel:
        Rtot=Rseries+materialsLibrary[anymaterial]     #sum of the previous total series resistance and the resistance of one of the 2 layers in parallel
        RtotSeries.append(Rtot)
        
    U1=1/RtotSeries[0]     #U value in the case of glass fiber
    U2=1/RtotSeries[1]      #U value in the case of wood stud
    
    Utot=f1*U1+f2*U2     #total U value considering the respective proportions for glass fiber and wood stud
    Rtot=1/Utot          #total resistance    
        
    RallLayers = []
    for anylayer in totalWallSeries+materialParallel:
        Rlayer = materialsLibrary[anylayer]
        RallLayers.append(Rlayer)
    results = {"Resistance value of all layers":RallLayers, "Total resistance":Rtot,'Total U':Utot}
    return results
    


def wallCalc_onlyInSeries(materialSeries):
    
    "The function receives 1 input: list of layers in series. It returns a dictionary which includes the thermal resistances of all layers, the total resistance and the total U."
    
    materialsLibrary={'outSurface':0.03,'woodBevel':0.14,'woodFiberboard13':0.23,'GlassFiber90':2.52,'woodStud90':0.63,'gypsumWallboard13':0.079,'inSurface':0.12,'wood50':0.44,'commonBrick100':0.12,'GlassFiber25':0.70,'urethaneRigidFoam25':0.98,'faceBrick200':0.15,'acousticTile':0.32,'concreteLight200':1.17,'clayTile100':0.18}    #dictionary 'material':unit thermal resistance
    
    surfaces = ['outSurface','inSurface']      #inner and outer surfaces of the wall
    
    totalWallSeries=surfaces+ materialSeries
    
    Rseries=0
    for anymaterial in totalWallSeries:
        Rseries=Rseries+materialsLibrary[anymaterial]     #sum of all the resistances of the materials in the list of layers in series
    
    U=1/Rseries     #total U value
    R=1/U          #total resistance    
        
    RallLayers = []
    for anylayer in totalWallSeries:
        Rlayer = materialsLibrary[anylayer]
        RallLayers.append(Rlayer)
    results = {"Resistance value of all layers":RallLayers, "Total resistance":R,'Total U':U}
    return results