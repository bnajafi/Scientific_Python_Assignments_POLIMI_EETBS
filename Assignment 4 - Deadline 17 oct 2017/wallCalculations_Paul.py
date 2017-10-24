def wallCalc_withParallel(layer1,layer2):                                                    #Calculate U-value of Wall                                 
    if("Glass fiber insulation" in layersInParallel):
        betweenStuds=layersInseries_forParallel+["Glass fiber insulation"]
    if("Wood stud" in layersInParallel):
        atStuds=layersInseries_forParallel+["Wood stud"]
    RValuebetween,RValueat=0,0
    for layer in betweenStuds:
        if(layer!="Glass fiber insulation"):
            RValuebetween+=materialLibrary[layer]["Rvalue"]
        else:
            RValuebetween+=materialLibrary[layer]["Rvalue"]*(90.0/materialLibrary[layer]["length"])   
    for layer in atStuds:
        RValueat+=materialLibrary[layer]["Rvalue"]

    Uwall=round((fractionBetweenstuds*(1/RValuebetween)+(1-fractionBetweenstuds)*(1/RValueat)),3)
    
    return Uwall 
    
def wallCalc_OnlyInSeries(layer1,layer2):                                                    #Calculate U-value of Door & roof
    RforDoor,RforRoof=0,0
    for layer in layers_forDoor:
        if(layer!="Wood"):
            RforDoor+=materialLibrary[layer]["Rvalue"]
        else:
            RforDoor+=materialLibrary[layer]["Rvalue"]*(50.0/materialLibrary[layer]["length"])
    Udoor=round((1/RforDoor),3)
    for layer in layers_forRoof:
        if(layer!="Wood"):
            RforRoof+=materialLibrary[layer]["Rvalue"]
        else:
            RforRoof+=materialLibrary[layer]["Rvalue"]*(400.0/materialLibrary[layer]["length"])
    Uroof=round((1/RforRoof),3)
    return {"U-Value of Door":Udoor,"U-value of Roof":Uroof}
       
#----Defining all values----
materialLibrary={"Wood bevel lapped siding":{"Rvalue":0.14,"length":13},"Wood fiberboard":{"Rvalue":0.23,"length":13},"Glass fiber insulation":{"Rvalue":0.68,"length":25},"Wood stud":{"Rvalue":0.63,"length":90},"Wood":{"Rvalue":0.22,"length":25},"Gypsum wallboard":{"Rvalue":0.079,"length":13},"Common brick":{"Rvalue":0.12,"length":100},"Asphalt shingle roofing":{"Rvalue":0.077,"length":13},"insideSurface":{"Rvalue":0.12},"outsideSurfaceWinter":{"Rvalue":0.030}}
layersInseries_forParallel=["insideSurface","outsideSurfaceWinter","Wood bevel lapped siding","Wood fiberboard","Gypsum wallboard","Common brick"]
layersInParallel=["Glass fiber insulation","Wood stud"]
layers_forRoof=["insideSurface","outsideSurfaceWinter","Wood","Asphalt shingle roofing"]
layers_forDoor=["insideSurface","outsideSurfaceWinter","Wood"]
fractionBetweenstuds=0.70

