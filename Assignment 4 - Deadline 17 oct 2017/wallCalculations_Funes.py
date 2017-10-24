# -*- coding: utf-8 -*-
def wallCalc_withParallel (Materials_In_Series,Materials_In_Parallel,fins):
    """This function computes each resistance of a composite wall, and also the total thermal Resistance and the overall heat transfer coefficient (U)""" 
    
    Materials_RValues = {"insideSurface":0.12,"outsideSurfaceWinter":0.03,"gypsumWallboard13mm":0.079,
    "woodStuds90mm":0.63,"glassFiber25mm":2.45,"woodFiberboard13mm":0.23,"woodBevel200mm":0.14, "commonBrick_100mm":0.12}
    
    Rseries = 0
    RValues_layers = []
    for AnyMaterial in Materials_In_Series:
        RValue_layer_series = Materials_RValues [AnyMaterial]
        RValues_layers.append(RValue_layer_series)
        print "The name of this layer is: "+AnyMaterial
        print "The resistance of the layer "+AnyMaterial+" is: "+str(RValue_layer_series)
        print "************************"
        Rseries = Rseries + RValue_layer_series
    print "The equivalent Resistance Value of the materials in series is: "+str(Rseries)+"(m2*°C/W)"
    
    Rparallel = 99999999999999999999
    for AnyMaterial in Materials_In_Parallel:
        RValue_layer_parallel = Materials_RValues [AnyMaterial]
        RValues_layers.append(RValue_layer_parallel)
        print "The name of this layer is: "+AnyMaterial
        print "The resistance of the layer "+AnyMaterial+" is: "+str(RValue_layer_parallel)
        print "************************"
        Rparallel = 1/((1/Rparallel) + (1/RValue_layer_parallel))
    print "The equivalente Resistance Value of the materials in parallel is: "+str(Rparallel)+"(m2*°C/W)"
    
    
    CenterWallJustGlassFiber = ["glassFiber25mm"]
    WallFirstLayer = Materials_In_Series + CenterWallJustGlassFiber
    RfirstLayer=0
    for AnyMaterial in WallFirstLayer:
        RValue_layer = Materials_RValues [AnyMaterial]
        RfirstLayer = RfirstLayer + RValue_layer
    print "The resistance of the wall considering just the insulation is: "+str(RfirstLayer)+"(m2*°C/W)"
    
    CenterWallJustWoodStud = ["woodStuds90mm"]
    WallSecondLayer = Materials_In_Series + CenterWallJustWoodStud
    RsecondLayer=0
    for AnyMaterial in WallSecondLayer:
        RValue_layer = Materials_RValues [AnyMaterial]
        RsecondLayer = RsecondLayer + RValue_layer
    print "The resistance of the wall considering just the wood studs is: "+str(RsecondLayer)+"(m2*°C/W)"
        
    Uins = (1/RfirstLayer)
    Uwood = (1/RsecondLayer)
    print "The heat transfer coefficient taking into account that there's only wood in the center is :"+str(Uwood)+"(W/m2*°C)"
    print "The heat transfer coefficient taking into account that there's only glass fiber insulator in the center is :"+str(Uins)+"(W/m2*°C)"
    
    Utot = Uins*fins + Uwood*(1-fins)
    print "The overall heat transfer coefficient is: "+str(Utot)+"(W/m2*°C)"
    
    Rtot = 1/Utot
    print "The overall thermal resistance of the wall is: "+str(Rtot)+"(m2*°C/W)"
    
    results = {"RValue of all layers":RValues_layers, "Total Resistance":Rtot, "Total U":Utot}
    return results
    
    
    
    
def wallCalc_OnlyInSeries (Materials_In_Series):
    """This function computes each resistance of a composite wall, and also the total thermal Resistance and the overall heat transfer coefficient (U)""" 
    
    Materials_RValues = {"insideSurface":0.12,"outsideSurfaceWinter":0.03,
    "wood_25mm":0.44,"ClayTile_100mm":0.18,"woodFiberboard_13mm":0.23,"woodStud_90mm":0.63, "gypsumWallboard13mm":0.079}
    
    Rseries = 0
    RValues_layers = []
    for AnyMaterial in Materials_In_Series:
        RValue_layer_series = Materials_RValues [AnyMaterial]
        RValues_layers.append(RValue_layer_series)
        print "The name of this layer is: "+AnyMaterial
        print "The resistance of the layer "+AnyMaterial+" is: "+str(RValue_layer_series)
        print "************************"
        Rseries = Rseries + RValue_layer_series
    print "The equivalent Resistance Value of the materials in series is: "+str(Rseries)+"(m2*°C/W)"
    
    Utot = 1/Rseries
    print "The total coefficient heat transfer is :"+str(Utot)

    results = {"RValue of all layers":RValues_layers, "Total Resistance":Rseries, "Total U":Utot}
    return results

Materials_In_Series = ["insideSurface","outsideSurfaceWinter","gypsumWallboard13mm","woodFiberboard13mm","woodBevel200mm"]
Materials_In_Parallel = ["woodStuds90mm","glassFiber25mm"]
door = ["insideSurface","outsideSurfaceWinter","wood_25mm"]
roof = ["ClayTile_100mm","woodFiberboard_13mm","woodStud_90mm","gypsumWallboard13mm"]