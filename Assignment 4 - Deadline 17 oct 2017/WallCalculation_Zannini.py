## wall cal series

def CalcWallSeries (List,Lenghts): #list of materials, lenghts of layers in mm
    ### The function calculates the value of the total resistance of a wall. The imput must be a List with all the materials which the wall is composed of. 
    
    MaterialLibrary={"WoodBevelLappedSidings":{"Rvalue":0.14,"lenght":1},"FoamInsulation":{"Rvalue":0.98,"lenght":1},
    "GlassFiber":{"Rvalue":0.70,"lenght":25},"WoodStud":{"Rvalue":0.63,"lenght":90},"GypsumBoard":{"Rvalue":0.079,"lenght":13},
    "WoodFiberboardSheeting":{"Rvalue":0.23,"lenght":13},"insideSurf":{"Rvalue":0.12,"lenght":1},"outsideSurfSummer": {"Rvalue":0.044,"lenght":1},
    "outsideSurfWinter":{"Rvalue":0.03,"lenght":1},"Wood": {"Rvalue":0.22,"lenght":25}}   ##lenghts in mm
    
    print "This wall is composed by: " + str(List)
    
    Rtot=0
    count=0
    for any in List:
        Material=MaterialLibrary[any] #I save a temporary directory of materials one by one
        Rtot=Rtot+Material["Rvalue"]*(Lenghts[count]/Material["lenght"])
        count+=1
    Utot=1/Rtot    
    print "The total resistance of the wall is: "+str(Rtot)
    print "The overall heat transfert coefficient is:"+str(Utot) 
    return Utot
    
def CalcUtotWall (LayersSeries,LayersParallel,RatioParallel):  ##function
    ###the function calculates the total heat conduction coefficient of the wall composed by two resistances in parallel and other in series
    MaterialLibrary={"WoodBevelLappedSidings":0.14,"FoamInsulation":0.98,
"GlassFiber_90mm":2.45,"WoodStud":0.63,"GypsumBoard":0.079,"WoodFiberboardSheeting_13mm":0.23,
"insideSurf":0.12,"outsideSurfSummer":0.044,"outsideSurfWinter":0.03}
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
    