def wall_calc(listOfLayers):
    Material_library = {"Wood bevel lapped siding":0.14,"Wood fiberboard sheeting,13mm":0.23,"Glass fiber insulation,90mm":2.45,"Wood stud,38mm*90mm":0.63,"Gypsum wallboard,13mm":0.079,"OutSurface 24km/h wind":0.03,"InsideSurface still air":0.12}    
    airOnTwoSides = ["OutSurface 24km/h wind","InsideSurface still air"]
    layers_wall_complete = listOfLayers + airOnTwoSides
    Rtotseries = 0
    Rtotpara = 0
    RValues_layers = []
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rtotseries=Rtotseries+RValue_layer
        RValues_layers.append(RValue_layer)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layer)
        print "***************************************"
    print "the total R Value is "+ str(Rtotseries)
    print "***************************************"
    
    for anyLayer in layers_wall_parallel:
        RValue_layer = Material_library[anyLayer]
        Rtotpara=Rtotpara+1/RValue_layer
        RValues_layers.append(RValue_layer)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layer)
        print "***************************************"
    print "the total R Value is "+ str(Rtotpara)
    print "***************************************"

    Rtot = Rtotpara + Rtotseries    
    results = {"Rtot":Rtot,"Rvalue of all layers":RValues_layers}
    return results

layers_wall = ["Wood bevel lapped siding","Wood fiberboard sheeting,13mm","Gypsum wallboard,13mm"]
layers_wall_parallel = ["Glass fiber insulation,90mm","Wood stud,38mm*90mm"]
results_thisWall = wall_calc(layers_wall)
