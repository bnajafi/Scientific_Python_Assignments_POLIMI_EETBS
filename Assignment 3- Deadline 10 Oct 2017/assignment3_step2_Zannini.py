MaterialLibrary={"WoodBevelLappedSidings":0.14,"FoamInsulation":0.98,
"GlassFiber_90mm":2.45,"WoodStud":0.63,"GypsumBoard":0.079,"WoodFiberboardSheeting_13mm":0.23,
"insideSurf":0.12,"outsideSurfSummer":0.044,"outsideSurfWinter":0.03}

LayersSeries=["WoodBevelLappedSidings","WoodFiberboardSheeting_13mm","GypsumBoard","insideSurf","outsideSurfWinter"]
LayersParallel=["WoodStud","GlassFiber_90mm"]
RatioParallel=0.75


def CalcUtotWall (LayersSeries,LayersParallel,MaterialLibrary,RatioParallel):  ##function
    ###the function calculates the total heat conduction coefficient of the wall composed by two resistances in parallel and other in series
    Rtot=[]
    for any in LayersParallel:
        LayersSeries.append(any)  
        print "This type of wall is composed by: " +str(LayersSeries)
        print"***"
        R=0
        for any in LayersSeries:
            RvalueLayer=MaterialLibrary[any]
            R=R+RvalueLayer
        print "The value of resistance is: " + str(R)
        Rtot.append(R)
        print "*************"
        print" "
        LayersSeries.pop(-1)
        
    Utot=( (Rtot[0]**-1)*(1-RatioParallel) )+( (Rtot[1]**-1) *RatioParallel )
    print "the value of the total heat transfert coefficient (Utotal) is " +str(Utot) +" W/k m^2 "
    
    LayersWall=LayersSeries+LayersParallel
    Rvalues=[]   ## creation of a list with the value of each single resistance utilized
    for any in LayersWall:
        Rvalues.append(MaterialLibrary[any])
    results={"Rsection":Rtot,"Rvalues":Rvalues,"Overall heat transfert coeff":Utot}
    return results
    