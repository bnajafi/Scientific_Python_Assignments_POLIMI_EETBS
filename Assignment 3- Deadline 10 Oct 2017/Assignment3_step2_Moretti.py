# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 3, step 2 - Multi-layer wall (material library + function)

Giorgio Moretti (10433550)

"""
def wallCalc(layers_series,layers_parallel,percentage_ins):
    """This function can be used to calculate the total resistance of a multi-layer wall."""
    """It includes a material library and calculations for resistances in parallel and in series."""

    material_library = {"outsideSurfaceWinter":0.030, "insideSurface":0.12, "woodBevelLappedSiding_13x200mm":0.14,
    "woodFiberboard_13mm":0.23, "glassFiberInsulation_25mm":0.70, "woodStud_90mm":0.63, "gypsumBoard_13mm":0.079}
    
    air_sides =  ["outsideSurfaceWinter","insideSurface"]

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
    results = {"Rtot":Rtot,"Utot":Utot}
    return results
    
layers_wall_series = ["woodBevelLappedSiding_13x200mm","woodFiberboard_13mm","gypsumBoard_13mm"]
layers_wall_parallel = ["woodStud_90mm","glassFiberInsulation_25mm"]
percentage_ins = 0.75

results_this_wall = wallCalc(layers_wall_series,layers_wall_parallel,percentage_ins)
print "\n The overall thermal resistance is: " + str(results_this_wall["Rtot"]) + " m^2°C/W"
print "\n The global heat transfer coefficient is: " + str(results_this_wall["Utot"]) + " W/m^2°C"