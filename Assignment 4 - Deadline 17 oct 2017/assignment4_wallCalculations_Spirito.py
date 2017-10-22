#calculations of heat transfer coefficient of the walls, doors and ceilings

#Let's calculate U of the wall

def wallCalc_withParallel(Layers_atStuds,Layers_betweenStuds,f_ins,f_stud):
    Material_library= {"outsideSurfaceWinter":0.030,"insideSurface":0.12,"commonBrick_100mm":0.12,"woodStud_90mm":0.63,
    "woodFiberboard_13mm":0.23,"gypsum_13mm":0.079,"glassfiberInsulation_90mm":2.52,"woodBevelLapped":0.14} 
    AirOnTwoSides= ["outsideSurfaceWinter","insideSurface"] 
    
    CompleteLayer_atStuds= AirOnTwoSides+Layers_atStuds
    valuesRes_as=[]
    Rtot_as=0
    for anyLayer_as in CompleteLayer_atStuds:
        valueRes_as=Material_library[anyLayer_as]
        valuesRes_as.append(valueRes_as)  
        Rtot_as= Rtot_as+valueRes_as
    print "The unit thermal resistances of the layer at studs are: "+str(valuesRes_as)
    print "The total unit thermal resistance of the layer at studs is: "+str(Rtot_as)+ " (m^2 degC)/W"
    U_as= 1/Rtot_as
    print "Thus, the overall heat transfer coefficient U is: "+str(U_as)+ " W/(m^2 degC) \n"
    
    CompleteLayer_betweenStuds=AirOnTwoSides+Layers_betweenStuds
    valuesRes_bs=[]
    Rtot_bs=0
    for anyLayer_bs in CompleteLayer_betweenStuds:
        valueRes_bs=Material_library[anyLayer_bs]
        valuesRes_bs.append(valueRes_bs)
        Rtot_bs= Rtot_bs+valueRes_bs
    print "The unit thermal resistances of the layer between studs are: "+str(valuesRes_bs)
    print "The total unit thermal resistance of the layer between studs is: "+str(Rtot_bs)+ " (m^2 degC)/W"
    U_bs= 1/Rtot_bs
    print "Thus, the overall heat transfer coefficient U is: "+str(U_bs)+ " W/(m^2 degC) \n"
   
    U_wall=U_bs*f_ins+U_as*f_stud
    print "THE OVERALL HEAT TRANSFER COEFFICIENT OF THE WALL IS: "+str(U_wall)+ " W/(degC m^2) \n"
    R_wall= 1/U_wall 
    print "THE OVERALL UNIT THERMAL RESISTANCE R' OF THE WALL IS: " +str(R_wall) + " m^2(degC)/W \n"
    results_w = {"U_wall":U_wall}
    return results_w
Layers_atStuds=["woodStud_90mm","gypsum_13mm","commonBrick_100mm","woodFiberboard_13mm","woodBevelLapped"]
Layers_betweenStuds=["gypsum_13mm","commonBrick_100mm","woodFiberboard_13mm","woodBevelLapped","glassfiberInsulation_90mm"]              
results= wallCalc_withParallel(Layers_atStuds,Layers_betweenStuds,0.70,0.30)

#Let's calculate U of the door
#I consider U of ceiling known because it's given in the text 

def wallCalc_onlyInSeries(DoorLayer,CeilingLayer):
    Material_library={"outsideSurfaceWinter":0.030,"insideSurface":0.12,"wood_50mm":0.44,"ceiling_layer":3.85}
    AirOnTwoSides= ["outsideSurfaceWinter","insideSurface"]
    
    CompleteLayer_door=AirOnTwoSides+DoorLayer
    Rtot_door=0
    for anyRes_d in CompleteLayer_door:
        ResValue_door=Material_library[anyRes_d]
        Rtot_door=Rtot_door+ResValue_door
    print "The total unit thermal resistance of the door is: "+str(Rtot_door)+ " (m^2 degC)/W"
    U_door=1/Rtot_door
    print "Thus, the overall heat transfer coefficient U of the door is: "+str(U_door)+ " W/(m^2 degC) \n"
    
   
    CompleteLayer_ceiling= AirOnTwoSides+CeilingLayer
    Rtotceiling=0
    for anyRes_c in CompleteLayer_ceiling:
        ResValue_ceiling=Material_library[anyRes_c]
        Rtotceiling=Rtotceiling+ResValue_ceiling
    print "The total unit thermal resistance of the ceiling is: "+str(Rtotceiling)+ " (m^2 degC)/W"
    U_ceiling=1/Rtotceiling
    print "Thus, the overall heat transfer coefficient U of the ceiling is: "+str(U_ceiling)+ " W/(m^2 degC) \n"
    results = {"U_ceiling":U_ceiling,"U_door":U_door}
    return results

      
 
DoorLayer=["wood_50mm"]
CeilingLayer=["ceiling_layer"] 
results_door= wallCalc_onlyInSeries(DoorLayer,CeilingLayer)
