# -*- coding: utf-8 -*-
Material_library={"outsideSurfaceWinter":0.030,"woodBevel":0.14,"woodFiberboard_13mm":0.23,
    "glassFiberInsulation_90mm":2.45,"woodStud_90mm":0.63,"gypsumWallboard_13mm":0.079,"insideSurface":0.12}
layers_wall_series = ["outsideSurfaceWinter","woodBevel","woodFiberboard_13mm", "gypsumWallboard_13mm","insideSurface"]
layers_wall_parallel= ["glassFiberInsulation_90mm","woodStud_90mm"]
fraction=float(0.75)
    

def wall_calc(layers_wall_series,layers_wall_parallel,fraction):
    
     
    Rseriestot=0;
    Rvaluelayers=[]

    for anylayer in layers_wall_series:
        Rseriestot=Rseriestot+Material_library[anylayer]
        Rvaluelayers.append(Rseriestot)


    Rparallel=0;
    for anylayer in layers_wall_parallel:
        Rparallel=Material_library[anylayer]+Rseriestot
        Rvaluelayers.append(Rparallel)


    U_overall = fraction*Rvaluelayers[-2]**-1 +(1-fraction)*Rvaluelayers[-1]**-1
 
    print "The overall heat transfer coefficient is: " +str(U_overall)+ "W/°C"
       
    
Result=wall_calc(layers_wall_series, layers_wall_parallel,fraction)      
    


 
