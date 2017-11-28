def wallCalc_withParallel(layers_series,layers_par,fArea):
    Material_library={"outsideSurface":0.03, "woodBevel":0.14, "woodFiberSheeting":0.23, "glassInsulation": 2.45,"woodStud":0.63, "gypsumWallboard":0.079, "insideSurface":0.12, "wood":0.44}
    par1=[layers_par[0]]
    par2=[layers_par[1]]
    layers1=layers_series+par1
    layers2=layers_series+par2
    layers=layers_series+par1+par2
    fArea=0.75
    Rtot1=0
    Rtot2=0
    RValues1=[]
    for anyLayer in layers1:
        RValue_layers_1 = Material_library[anyLayer]
        Rtot1=Rtot1+RValue_layers_1
        RValues1.append(RValue_layers_1)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layers_1)
        print "***************************************"
    print "the total R Value is "+ str(Rtot1)
    Utot1=1/Rtot1*(fArea)
    print "the total U value is "+str(Utot1)
    print "**************************************"
    print "**************************************"
   
    RValues2=[]
    for anyLayer in layers2:
        RValue_layers_2 = Material_library[anyLayer]
        Rtot2=Rtot2+RValue_layers_2
        RValues2.append(RValue_layers_2)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layers_2)
        print "***************************************"
    print "the total R value is "+str(Rtot2)
    Utot2=1/Rtot2*(1-fArea)
    print "the total U value is "+str(Utot2)
    print "***************************************"
    print "***************************************"
    RValues=[]
    for anyLayer in layers:
        RValue_layers=Material_library[anyLayer]
        RValues.append(RValue_layers)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layers)
        print "***************************************"
    print "the list of R values is: "+str(RValues)
    
    Utot=Utot1+Utot2
    Rtot=1/Utot
    total_results=Utot
    return total_results
    
layers_series=["outsideSurface","woodBevel","woodFiberSheeting","gypsumWallboard","insideSurface"] 
layers_par=["glassInsulation", "woodStud"]
fArea=0.75
results_Wall=wallCalc_withParallel(layers_series,layers_par,fArea)

def wallCalc_onlyInSeries(layers_series):
    Material_library={"outsideSurface":0.03, "woodBevel":0.14, "woodFiberSheeting":0.23, "glassInsulation": 2.45,"woodStud":0.63, "gypsumWallboard":0.079, "insideSurface":0.12, "wood":0.44}
    layers_door=[layers_series[0],layers_series[1],layers_series[2]]
    Rtot_door=0
    RValues_door=[]
    U_roof=0.25
    for anyLayer in layers_door:
        RValue_layers_door = Material_library[anyLayer]
        Rtot_door=Rtot_door+RValue_layers_door
        RValues_door.append(RValue_layers_door)
        print "this layer is: "+ anyLayer
        print "The value of R for this layer is: "+ str(RValue_layers_door)
        print "***************************************"
    print "the total R Value for the door is "+ str(Rtot_door)
    Utot_door=1/Rtot_door
    print "the total U value for the door is "+str(Utot_door)
    print "**************************************"
    print "the total U value for the roof is "+str(U_roof)
    print "**************************************"
    result=Utot_door
    return result
    
layers=["outsideSurface", "insideSurface", "wood","commonBrick", "asphaltRoofing", "concreteLightweight", "cementMortar"]
results_doorRoof=wallCalc_onlyInSeries(layers)