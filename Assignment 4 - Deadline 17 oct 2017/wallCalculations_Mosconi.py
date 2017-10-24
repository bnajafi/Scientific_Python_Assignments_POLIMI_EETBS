def wallCalc_withParallel (listOfLayers_series,listOfLayers_parallel,ratio_area):
    """first input: all the layers in series not convective ones
    second input: two layers in parallel
    third input: ratio between first parallel layer(in input 2) and total area"""

    Material_library={"stucco_25mm": 0.037, "faceBrick_100mm": 0.075,
        "insideSurface":0.12, "outsideSurfaceSummer":0.044,"commonBrick":0.12,
        "outsideSurfaceWinter":0.030,"woodfiberboard_13mm":0.23,"gypsumBoard":0.079,
        "woodStud":0.63,"woodBevel":0.14,"buildingPaper":0.011,"acousticTile":0.32,
        "slag_13mm":0.067,"glassFiber": 2.52,"wood_50mm":0.44, "asphaltRoofing":0.077}
    Layer_air=["insideSurface","outsideSurfaceWinter"]
    listOfLayers_series=listOfLayers_series+Layer_air
    R_list=[]
    for Layer_par in listOfLayers_parallel:
        Rtot=0
        R_parallel=Material_library[Layer_par]
        for anyLayer in listOfLayers_series:
            R_anyLayer=Material_library[anyLayer]
            Rtot=Rtot+R_anyLayer
        R_list.append(Rtot+R_parallel)
    U_overall=(1/R_list[0]*ratio_area)+(1/R_list[1]*(1-ratio_area)) 
        
    return U_overall  


def wallCalc_onlyInSeries (listOfLayers_series):
    """insert only layers in series to compute di total U"""

    Material_library={"stucco_25mm": 0.037, "faceBrick_100mm": 0.075,"commonBrick":0.12,
        "insideSurface":0.12, "outsideSurfaceSummer":0.044,
        "outsideSurfaceWinter":0.030,"woodfiberboard_13mm":0.23,"gypsumBoard":0.079,
        "woodStud":0.63,"woodBevel":0.14,"buildingPaper":0.011,"acousticTile":0.32,
        "slag_13mm":0.067,"glassFiber":2.52,"wood_50mm":0.44,"asphaltRoofing":0.077}
    Layer_air=["insideSurface","outsideSurfaceWinter"]
    listOfLayers_series=listOfLayers_series+Layer_air
    Rtot=0    
    for anyLayer in listOfLayers_series:
        RanyLayer=Material_library[anyLayer]
        Rtot=Rtot+RanyLayer
    U_overall=(1/Rtot)
        
    return U_overall 


