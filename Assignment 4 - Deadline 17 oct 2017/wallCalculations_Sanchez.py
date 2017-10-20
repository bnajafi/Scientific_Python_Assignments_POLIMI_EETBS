def wallCalc_withParallel(listOfLayersinSeries,listOfLayersinParallel):
    Material_library = {"stucco":{"Rvalue":0.023,"length":13},"faceBreak_100mm":0.075,
     "insideSurface":0.12,"outsideSurfaceSummer":0.044,"outsideSurfaceWinter":0.03
        ,"woodFiberboard_13mm":0.23,'GlassFiber':0.70,'FaceBrick':0.075,
        'GypsumBoard':0.079,'Plaster':0.079,'ConcreteBlockLight':0.27,
        'WoodBevel':0.14,'CommonBrick':0.12,'woodStud':0.63}    
    airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]
    Rparmul=1
    Rparsum=0
    for anylayer in listOfLayersinParallel:
        RValue_layer = Material_library[anylayer]
        Rparmul=Rparmul*RValue_layer
        Rparsum=Rparsum+RValue_layer    
    Rpartot=Rparmul/Rparsum    
    layers_wall_complete = listOfLayersinSeries + airOnTwoSides
    Rsertot = 0
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rsertot=Rsertot+RValue_layer    
    Rtot=Rpartot+Rsertot
    return Rtot
    
def wallCalc_onlyinSeries(list_Layers):
    Material_library = {"stucco_13mm":0.023,"faceBreak_100mm":0.075,
     "insideSurface":0.12,"outsideSurfaceSummer":0.044,"outsideSurfaceWinter":0.03
        ,"woodFiberboard_13mm":0.23,'GlassFiber':0.70,'FaceBrick':0.075,
        'AsphaltRoofing':0.077,'GypsumBoard':0.079,'Plaster':0.079,
        'ConcreteBlockLight':0.27,'WoodBevel':0.14,'CommonBrick':0.12,'WoodStud':0.63}
    airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]
    layers_wall_complete = list_Layers + airOnTwoSides
    Rsertot = 0
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rsertot=Rsertot+RValue_layer    
    return Rsertot
    
layers_roof=["faceBreak_100mm",'AsphaltRoofing']
layers_door=["woodFiberboard_13mm",'WoodBevel']
layers_wallseries = ["faceBreak_100mm","woodFiberboard_13mm"]
layers_wallparallel=['Plaster','FaceBrick','woodStud']
Udoor=1/wallCalc_onlyinSeries(layers_door)
Uroof=1/wallCalc_onlyinSeries(layers_roof)
Uwall =1/wallCalc_withParallel(layers_wallseries,layers_wallparallel)
print "the wall U Value is "+ str(Uwall)
print "the roof U Value is "+ str(Uroof)
print "the door U Value is "+ str(Udoor)