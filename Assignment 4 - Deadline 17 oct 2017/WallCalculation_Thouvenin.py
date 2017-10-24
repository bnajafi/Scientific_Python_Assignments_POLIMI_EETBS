# -*- coding: utf-8 -*-

#This function permit to calculate the U value of the walls which have 2 layers in parallel

def wallcalc_withparallel ( wallpara1,wallpara2,f):
    """This function will calculate the overall heat transfer coefficient and resistance of the wall"""
    
    #Definition of the material library as a dictionnary
    Material_library = { 'Outside_Surface_Winter' : 0.03 , 'Inside_Surface' : 0.12 , 'Wood_25mm' : 0.22 ,
    'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.52 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 ,
    'Cement_Mortar' : 0.018 , 'Common_Brick' : 0.12 , 'Wood_Fiberboard' : 0.23 }
   
    #output a dictionnary with the resistances of all layers
    layers_wall_complete = wallpara1 + wallpara2
    
    RValues_layers = []
    for anylayer in layers_wall_complete:
        RValue_layers = Material_library[anylayer]
        RValues_layers.append(RValue_layers)
        print "this layer is: "+ anylayer
        print "The value of R for this layer is: "+ str(RValue_layers)
        print "***************************************"
    
    
    #Unit thermal resistance and overall heat transfer in serie between studs
    R_Between_Studs = 0

    for anylayer in wallpara1 : 
        Between_Studs_library = Material_library [anylayer]
        R_Between_Studs = R_Between_Studs + Between_Studs_library
    U_Between_Studs = 1 / R_Between_Studs
    print U_Between_Studs

    #Unit thermal resistance and overall heat transfer in serie at studs

    R_At_Studs = 0

    for anylayer in wallpara2 : 
        At_Studs_library = Material_library [anylayer]
        R_At_Studs = R_At_Studs + At_Studs_library
    U_At_Studs = 1 / R_At_Studs
    print U_At_Studs

    #Calculation of the global overall heat transfer and the global resistance

    U_Global = f[0] * U_Between_Studs + f[1] * U_At_Studs
    R_Global = 1 / U_Global
    print "Here is the value of the global overall Resistance R: " + str(R_Global) + "m2°C/W"
    print "Here is the value of the global overall heat transfer U: " + str(U_Global) + "W/m2°C"

    results = { "Roverall" : R_Global, "Rvalue of all layers" : RValue_layers , "Uoverall" : U_Global}
    return results

#Informations for the function

wallpara1 = [ 'Outside_Surface_Winter' , 'Gypsum' , 'Glass_Fiber' , 'Common_Brick' , 'Wood_Fiberboard' ,'Wood_Bevel', 'Inside_Surface' ]
wallpara2 = [ 'Outside_Surface_Winter' , 'Gypsum' , 'Wood_Stud' , 'Common_Brick' , 'Wood_Fiberboard' ,'Wood_Bevel', 'Inside_Surface' ]
f = [ 0.7 , 0.3 ]

results_thisWall = wallcalc_withparallel ( wallpara1,wallpara2,f)

#**********************************************************************
#This function permit to calculate the U value of layers in series: We will use it here for the door and the roof

def WallCalcOnlyinSeries (layerlist) :
    
     #Definition of the material library as a dictionnary
    Material_library = { 'Outside_Surface_Winter' : 0.03 , 'Inside_Surface' : 0.12 , 'Wood_25mm' : 0.22 ,
    'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.52 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 ,
    'Cement_Mortar' : 0.018 , 'Common_Brick' : 0.12 , 'Wood_Fiberboard' : 0.23 , 'AsphaltShingleRoofing' : 0.077}
    
    R_serie = 0
    
    for anylayer in layerlist :
        if (anylayer == 'Wood_50mm') :                                  # Here, the dimension of the material wood is not the same than the one in the Material library
            R_anylayer = Material_library [ 'Wood_25mm' ] * 50 / 25     #Proportionality
        else :
            R_anylayer = Material_library [ anylayer ] 
        R_serie = R_serie + R_anylayer
        print R_serie
        print "**************************************"
        
    U_serie = 1 / R_serie 
    print "Here is the value of the global overall Resistance R: " + str (R_serie) + "m2°C/W"

    print "Here is the value of the global overall heat transfer U:" + str (U_serie) + "W/m2°C"
    
    results = {"Roverall" : R_serie , "Uoverall" : U_serie }
    return results
    
    
#Informations for the function
  
layerlist_door = [ 'Outside_Surface_Winter' , 'Wood_50mm' , 'Inside_Surface' ]
layerlist_roof = [ 'Outside_Surface_Winter' , 'AsphaltShingleRoofing' ,
'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]

results_door = WallCalcOnlyinSeries ( layerlist_door )
results_roof = WallCalcOnlyinSeries ( layerlist_roof )







