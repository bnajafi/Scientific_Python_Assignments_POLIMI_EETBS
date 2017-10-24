def wallCalc_withParallel(wall_withParallel):
    Material_library = {"AsphaltRoofing":0.077,"Wood_50mm":0.44,"Wood bevel lapped siding":0.14,"Wood fiber board,13mm":0.23,"Glass fiber insulation":0.70,"Wood stud,38mm*90mm":0.63,"Gypsum wallboard,13mm":0.079,"OutSurface 24km/h wind":0.03,"InsideSurface still air":0.12}    
    layers_wall_complete = wall_withParallel
    Rtot_withParallel = 0
    RValues_layers = []
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rtot_withParallel=1/(Rtot_withParallel+1/RValue_layer)
        Utot_withParallel = 1/Rtot_withParallel
        RValues_layers.append(RValue_layer)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layer)
        print "***************************************"
    print "the total R Value is "+ str(Rtot_withParallel)
    print "***************************************"
    print "the total U Value is "+ str(Utot_withParallel)
    print "***************************************"
    Utot_Parallel = {"Utot":Utot_withParallel}
    return Utot_Parallel



def wallCalc_onlyInSeries(wall_onlyInSeries):
    Material_library = {"AsphaltRoofing":0.077,"Wood_50mm":0.44,"Wood bevel lapped siding":0.14,"Wood fiberboard sheeting,13mm":0.23,"Wood stud,38mm*90mm":0.63,"Gypsum wallboard,13mm":0.079,"OutSurface 24km/h wind":0.03,"InsideSurface still air":0.12}    
    airOnTwoSides = ["OutSurface 24km/h wind","InsideSurface still air"]
    layers_wall_complete = wall_onlyInSeries + airOnTwoSides
    Rtot_onlyInSeries = 0
    RValues_layers = []
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rtot_onlyInSeries=Rtot_onlyInSeries+RValue_layer
        Utot_onlyInSeries = 1/Rtot_onlyInSeries
        RValues_layers.append(RValue_layer)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layer)
        print "***************************************"
    print "the total R Value is "+ str(Rtot_onlyInSeries)
    print "***************************************"
    print "the total U Value is "+ str(Utot_onlyInSeries)
    print "***************************************"
    Utot_Series = {"Utot":Utot_onlyInSeries}
    return Utot_Series


