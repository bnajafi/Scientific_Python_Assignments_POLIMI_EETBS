# Assignment 4


def wallCalc_withParallel(list_Of_Layers_Studs,list_Of_Layers_Insu,IF):
    Material_library = {"stucco_25mm":0.023,"face_brick_100mm":0.075,"common_brick_100mm":0.12,"wood_bevel_lapped_siding_13mmx200mm":0.14,
     "plaster_or_gypsum_board_13mm":0.079,"inside_surface":0.12,"outside_surface_summer":0.044,"outside_surface_winter":0.03,"wood_stud_nominal":0.63,
     "asphalt_shingle_roofing":0.077,"cement_mortar_13mm":0.018,"wood_fiberboard_13mm":0.23,"glass_fiber_insulation_25mm":0.70,"wood_25mm":0.22}    
    air_on_two_sides = ["inside_surface","outside_surface_winter"]
    layers_wall_studs = list_Of_Layers_Studs + air_on_two_sides
    Rtot_S = 0
    for anyLayer in layers_wall_studs:
        RValue_layer_s = Material_library[anyLayer]
        Rtot_S = Rtot_S + RValue_layer_s
    U_S=(1/(Rtot_S))
    print "the total U Value is "+ str(U_S)
    layers_wall_insu = list_Of_Layers_Insu + air_on_two_sides
    Rtot_I = 0
    for anyLayer in layers_wall_insu:
        RValue_layer_i = Material_library[anyLayer]
        Rtot_I = Rtot_I+RValue_layer_i
    U_I=(1/(Rtot_I))
    print "the total U Value is "+ str(U_I)
    U_global = U_I*IF + U_S*(1-IF)
    print "the real total U Value is "+ str(U_global)
    return U_global

def wallCalc_onlyInSeries(list_of_layers):
     Material_library = {"stucco_25mm":0.023,"face_brick_100mm":0.075,"common_brick_100mm":0.12,"wood_bevel_lapped_siding_13mmx200mm":0.14,
     "plaster_or_gypsum_board_13mm":0.079,"inside_surface":0.12,"outside_surface_summer":0.044,"outside_surface_winter":0.03,"wood_stud_nominal":0.63,
     "asphalt_shingle_roofing":0.077,"cement_mortar_13mm":0.018,"wood_fiberboard_13mm":0.23,"glass_fiber_insulation_25mm":0.70,"wood_25mm":0.22}    
     Air_On_Two_Sides = ["inside_surface","outside_surface_winter"]
     layers_wall_series = list_of_layers + Air_On_Two_Sides
     Rtot = 0
     for anyLayer in layers_wall_series:
        RValue_layer = Material_library[anyLayer]
        Rtot=Rtot+RValue_layer
     U_global=((Rtot)**-1)
     print "the total U Value is "+ str(U_global)
     return U_global