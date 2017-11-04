# -*- coding: utf-8 -*-
def wall_calc ( Between_Studs,At_Studs,f):
    """This function will calculate the overall heat transfer coefficient and resistance of the wall"""
    #Definition of the material library as a dictionnary

    Material_library = { 'Outside_Surface_Winter' : 0.03 , 'Inside_Surface' : 0.12 , 'Wood' : 0.22 , 'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.45 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 , 'Cement_Mortar' : 0.018 }
   
    #output a dictionnary with the resistances of all layers
    layers_wall_complete = Between_Studs + At_Studs
    
    RValues_layers = []
    for anylayer in layers_wall_complete:
        RValue_layers = Material_library[anylayer]
        RValues_layers.append(RValue_layers)
        print "this layer is: "+ anylayer
        print "The value of R for this layer is: "+ str(RValue_layers)
        print "***************************************"

    
    #Unit thermal resistance and overall heat transfer in serie between studs
    R_Between_Studs = 0

    for anylayer in Between_Studs : 
        Between_Studs_library = Material_library [anylayer]
        R_Between_Studs = R_Between_Studs + Between_Studs_library
    U_Between_Studs = 1 / R_Between_Studs
    print U_Between_Studs

    #Unit thermal resistance and overall heat transfer in serie at studs

    R_At_Studs = 0

    for anylayer in At_Studs : 
        At_Studs_library = Material_library [anylayer]
        R_At_Studs = R_At_Studs + At_Studs_library
    U_At_Studs = 1 / R_At_Studs
    print U_At_Studs

    #Calculation of the global overall heat transfer and the global resistance

    U_Global = f[0] * U_Between_Studs + f[1] * U_At_Studs
    print "Here is the value of the global overall heat transfer: " + str(U_Global) + "W/m2°C"
    R_Global = 1 / U_Global
    print "Here is the value of the global overall Resistance: " + str(R_Global) + "m2°C/W"

    results = { "R_Global" : R_Global, "Rvalue of all layers" : RValue_layers}
    return results
    

Between_Studs = [ 'Outside_Surface_Winter' , 'Wood_Bevel' , 'Wood_Fiberboard' , 'Glass_Fiber' , 'Gypsum' , 'Inside_Surface' ]
At_Studs = [ 'Outside_Surface_Winter' , 'Wood_Bevel' , 'Wood_Fiberboard' , 'Wood_Stud' , 'Gypsum' , 'Inside_Surface' ]
f = [ 0.75 , 0.25 ]

results_thisWall = wall_calc ( Between_Studs,At_Studs,f)
