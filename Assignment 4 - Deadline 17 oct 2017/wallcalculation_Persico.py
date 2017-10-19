# -*- coding: utf-8 -*-
Material_library={"outsideSurfaceWinter":0.030,"woodBevel":0.14,"woodFiberboard_13mm":0.23,
    "glassFiberInsulation_90mm":2.52,"woodStud_90mm":0.63,"gypsumWallboard_13mm":0.079,"insideSurface":0.12, "wood":0.44,"commonBrick":0.12}
layers_wall_series = ["outsideSurfaceWinter","woodBevel","woodFiberboard_13mm", "gypsumWallboard_13mm","insideSurface","commonBrick"]
layers_wall_parallel= ["glassFiberInsulation_90mm","woodStud_90mm"]


def wall_calc_series(layers_wall_series):
    Rseriestot=0
    for anylayers in layers_wall_series:
        Rseriestot=Rseriestot+Material_library[anylayers]
    Userietot=1/Rseriestot
    return Userietot
    

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
 
    return U_overall
       
    

    


 
