"""

EETBS 2017/2018 - Assignment 4 - wall calculation function

Giorgio Moretti (10433550)

"""
def wallCalcSP(layers_series, layers_parallel, percentage_ins, season):
    """This function can be used to calculate the total resistance of a multi-layer wall."""
    """It includes a material library and calculations for resistances in parallel and in series."""

    material_library = {"outsideSurfaceWinter":0.030, "outsideSurfaceSummer":0.044,"insideSurface":0.12, "woodBevelLappedSiding_13x200mm":0.14,
    "woodFiberboard_13mm":0.23, "glassFiberInsulation_25mm":2.45, "woodStud_90mm":0.63, "gypsumBoard_13mm":0.079,
    "commonBrick_100mm":0.12, "wood_25mm":0.44, "asphaltRoofing":0.077}
    
    air_sides = ["insideSurface"]
    
    if (season == "winter"):
        air_sides.append("outsideSurfaceWinter")
    else:
        air_sides.append("outsideSurfaceSummer")

    layers_wall_series_complete = layers_series + air_sides

    RValues_series = []
    Rtot_series = 0
    
    for anyLayer in layers_wall_series_complete:
        RValue_layer = material_library[anyLayer]
        RValues_series.append(RValue_layer)
        Rtot_series = Rtot_series + RValue_layer

    RValues_wall = []
    
    for anyLayer in layers_parallel:
        RValues_wall.append(material_library[anyLayer] + Rtot_series)
        
    Rtot = round(RValues_wall[0]*(1-percentage_ins) + RValues_wall[1]*percentage_ins,4)
    Utot = round(1/RValues_wall[0]*(1-percentage_ins) + 1/RValues_wall[1]*percentage_ins,4)
    
    results = {"Rtot":Rtot,"U":Utot}
    return results   
    

def wallCalcSeries(layers_series, season):
    """ This function calculates the total resistance (Rtot) and the global heat transfer coefficient (U) of layers ONLY IN SERIES. """
    
    material_library = {"outsideSurfaceWinter":0.030, "outsideSurfaceSummer":0.044,"insideSurface":0.12, "woodBevelLappedSiding_13x200mm":0.14,
    "woodFiberboard_13mm":0.23, "glassFiberInsulation_25mm":2.45, "woodStud_90mm":0.63, "gypsumBoard_13mm":0.079,
    "commonBrick_100mm":0.12, "wood_25mm":0.44, "asphaltRoofing":0.077}
    
    air_sides = ["insideSurface"]
    
    if (season == "winter"):
        air_sides.append("outsideSurfaceWinter")
    else:
        air_sides.append("outsideSurfaceSummer")

    layers_wall_series_complete = layers_series + air_sides

    RValues_series = []
    Rtot_series = 0
    
    for anyLayer in layers_wall_series_complete:
        RValue_layer = material_library[anyLayer]
        RValues_series.append(RValue_layer)
        Rtot_series = Rtot_series + RValue_layer
        
    Rtot = Rtot_series
    Utot = round(1/Rtot_series,4)
    
    results = {"Rtot":Rtot,"U":Utot}
    return results