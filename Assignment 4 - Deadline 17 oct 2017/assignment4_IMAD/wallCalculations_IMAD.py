# -*- coding: utf-8 -*-
def wall_calc_parallel(layers_in_series,layers_in_paralel,fraction):
    Materials_library={ 'outsideSurface_winter' : 0.03 , 'insideSurface' : 0.12 , 'Wood_50mm' : 0.44 ,
    'wood_bevel' : 0.14 , 'fiberboard_13mm' : 0.23 , 'glassfiber_90mm' : 2.52 , 'woodstud_90mm' : 0.63 , 'gypsum_13mm' : 0.079 , 
    'Common_Brick' : 0.12 }
    convection_resistances=["insideSurface","outsideSurface_winter"]
    layers1=layers_in_series+convection_resistances+["glassfiber_90mm"]
    layers2=layers_in_series+convection_resistances+["woodstud_90mm"]
    Rtot=0
    for anyLayer in layers1:
        RValue_layer=Materials_library[anyLayer]
        Rtot=Rtot+RValue_layer
    Rtot1=0
    for anyLayer in layers2:
        RValue_layer=Materials_library[anyLayer]
        Rtot1=Rtot1+RValue_layer   
    Utot=fraction/Rtot+(1-fraction)/Rtot1
    Rsum=1/Utot
    all_resistances=layers_in_series+layers_in_paralel+convection_resistances
    material=[]
    resistances=[]
    for anyLayer in all_resistances:
        material.append(Materials_library[anyLayer])
        resistances.append(anyLayer)
    library=dict(zip(resistances,material))
    print " Total resistance is :"+str(Rsum)+" m^2* degree C/W"
    print " "
    print " Total thermal coefficient is: "+str(Utot)+" W/m^2*degree C"
    print " "
    print " Library that gives layers that are used in wall and their resistance respectively:"
    print " "
    print library

    

def WallCalcOnlyinSeries (layerlist) :
    
     #Definition of the material library as a dictionnary
    Material_library={ 'outsideSurface_winter' : 0.03 , 'insideSurface' : 0.12 , 'Wood_50mm' : 0.44 ,
    'wood_bevel' : 0.14 , 'fiberboard_13mm' : 0.23 , 'glassfiber_90mm' : 2.52 , 'woodstud_90mm' : 0.63 , 'gypsum_13mm' : 0.079 , 
    'Common_Brick' : 0.12 }
    
    R_series = 0
    
    for anylayer in layerlist :
        R_anylayer = Material_library [anylayer] 
        R_series = R_series + R_anylayer
        print R_series
        print "****************"
        
    U_series = 1 / R_series 
    print "Here is the value of the global overall Resistance R: " + str (R_series) + "m2°C/W"

    print "Here is the value of the global overall heat transfer U:" + str (U_series) + "W/m2°C"
    
    results = {"Roverall" : R_series , "Uoverall" : U_series }
    return results
    
