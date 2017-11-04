#Rachid Aamrani

def HeatTransferCalc(Layers_atStuds,Layers_betweenStuds,f_ins,f_stud):
    Material_library= {"winteroutsidesurface":0.030, "summeroutsidesurface":0.044,"insideSurface":0.12,"stucco_25mm":0.037,"faceBrick_100mm":0.075,
    "commonBrick_100mm":0.12,"woodStud_90mm":0.63,"woodFiberboard_13mm":0.23,"buildingPaper":0.011,"gypsum":0.079,"glassfiberInsulation_90mm":2.45,
    "woodBevelLapped":0.14} 
    AirOnTwoSides= ["winteroutsidesurface","insideSurface"] 
     
    CompleteLayer_atStuds= AirOnTwoSides+Layers_atStuds
    valuesRes_as=[]
    Rtot_as=0
    for anyLayer_as in CompleteLayer_atStuds:
        valueRes_as=Material_library[anyLayer_as]
        valuesRes_as.append(valueRes_as)  
        Rtot_as= Rtot_as+valueRes_as
    print "The unit thermal resistances of the layer  are: "+str(valuesRes_as)
    print "The total unit thermal resistance of the layer  is: "+str(Rtot_as)+ " (m^2 degC)/W"
    U_as= 1/Rtot_as
    print "So, the overall heat transfer coefficient U is: "+str(U_as)+ " W/(m^2 degC) \n"
 
     
     
    CompleteLayer_betweenStuds= AirOnTwoSides+Layers_betweenStuds
    valuesRes_bs=[]
    Rtot_bs=0
    for anyLayer_bs in  CompleteLayer_betweenStuds:
        valueRes_bs=Material_library[anyLayer_bs]
        valuesRes_bs.append(valueRes_bs)
        Rtot_bs= Rtot_bs+valueRes_bs
    print "The unit thermal resistances of the layer between studs are: "+str(valuesRes_bs)
    print "The total unit thermal resistance of the layer between studs is: "+str(Rtot_bs)+ " (m^2 degC)/W"
    U_bs=1/Rtot_bs
    print "Thus, the overall heat transfer coefficient U is: "+str(U_bs)+ " W/(m^2 degC) \n"
     
    U_wall=U_bs*f_ins+U_as*f_stud
    print "The overall thermal resistence is: "+str(U_wall)+ " W/(degC m^2) \n"
    R_wall= 1/U_wall 
    print "The overall unit thermal resistance is: " +str(R_wall) + " m^2(degC)/W \n"
     
     
Layers_atStuds = ["gypsum","woodStud_90mm","woodFiberboard_13mm","woodBevelLapped"] 
Layers_betweenStuds= ["gypsum","glassfiberInsulation_90mm","woodFiberboard_13mm","woodBevelLapped"] 
     
results= HeatTransferCalc(Layers_atStuds,Layers_betweenStuds,0.75,0.25)
     