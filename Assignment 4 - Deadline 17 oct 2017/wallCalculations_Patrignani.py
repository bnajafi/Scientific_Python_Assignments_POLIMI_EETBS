# -*- coding: utf-8 -*-
def wallCalc_withParallel(ListOfLayersInSeries,ListOfLayersInParallel,AreaRatioInsulation):
    season = raw_input("please insert the season which we are referring to:  ")
    if season == "winter":
        material_library = {"gypsum_13mm":0.079, "wood_fiberboard":0.23, "wood_stud":0.63, "wood_bevel":0.14, "wood_25mm":0.44, "slag_13mm":0.067, "common_brick":0.12, "face_brick":0.075, "stucco":0.037, "glass_fiber":2.52, "inside_surface":0.12, "outside_surface":0.03} 

    elif season == "summer":
        material_library = {"gypsum_13mm":0.079, "wood_fiberboard":0.23, "wood_stud":0.63, "wood_bevel":0.14, "wood_25mm":0.44, "slag_13mm":0.067, "common_brick":0.12, "face_brick":0.075, "stucco":0.037, "glass_fiber":2.52, "inside_surface":0.12, "outside_surface":0.044}

    else:
        print "You have not entered an acceptable season"

    Rseries = 0
    for anylayer1 in ListOfLayersInSeries:
        Rvalue = material_library[anylayer1]
        Rseries = Rseries + Rvalue
    
    
    Rvalue = []
    Rtot = []
    for anylayer in ListOfLayersInParallel:
        TotalLayerList=ListOfLayersInSeries.append(anylayer)
        R = material_library[anylayer]
        Rvalue=Rvalue+[R]
    
    Uins = 1/(Rseries+Rvalue[0])
    Uwood = 1/(Rseries+Rvalue[1])
    
    Uoverall=Uins * AreaRatioInsulation + Uwood*(1-AreaRatioInsulation)
    
    
    print "The total heat transfer coefficient of the wall is " + str(Uoverall) + " W/m2°C"
    return Uoverall

#ListOfLayersInSeries=["gypsum_13mm", "common_brick", "wood_fiberboard", "wood_bevel","inside_surface","outside_surface"]
#ListOfLayersInParallel=["glass_fiber", "wood_stud"]
#AreaRatioInsulation = 0.70

#wallCalc_withParallel(ListOfLayersInSeries,ListOfLayersInParallel,AreaRatioInsulation)




def wallCalc_onlyInSeries(ListOfLayers):
    season = raw_input("please insert the season which we are referring to:  ")
    if season == "winter":
        material_library = {"gypsum_13mm":0.079, "wood_fiberboard":0.23, "wood_stud":0.63, "wood_bevel":0.14, "wood_25mm":0.44, "slag_13mm":0.067, "common_brick":0.12, "face_brick":0.075, "stucco":0.037, "glass_fiber":2.52, "inside_surface":0.12, "outside_surface":0.03} 

    elif season == "summer":
        material_library = {"gypsum_13mm":0.079, "wood_fiberboard":0.23, "wood_stud":0.63, "wood_bevel":0.14, "wood_25mm":0.44, "slag_13mm":0.067, "common_brick":0.12, "face_brick":0.075, "stucco":0.037, "glass_fiber":2.52, "inside_surface":0.12, "outside_surface":0.044}

    else:
        print "You have not entered an acceptable season"

    Rvalue = []
    R1 = 0
    for anylayer in ListOfLayers:
       Rvalue = material_library[anylayer]
       R1 = R1 + Rvalue
    U = 1/R1
    print "The trasmittance of the opac element is " + str(U) +" W/m2 °C"
    return U

#ListOfLayers = ["wood_25mm", "inside_surface","outside_surface"]
#wallCalc_onlyInSeries(ListOfLayers)