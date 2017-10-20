def wall_calculator(wall,FractionOfInsulation,door,roof):
    Matrial_Library={"OutsideSurfaceWinter":0.030,"WoodBevelLappedSiding_13mm":0.14,
    "WoodFiberboardSheeting_13mm":0.23,"GlassFiberInsulation_90mm":2.52,"WoodStud_90mm":0.63,
    "GypsumWallboard_13mm":0.079,"InsideSurfaceAir":0.12,"OutsideSurfaceSummer":0.044,"CommonBrick_100mm":0.12,
    "Wood_50mm":0.44}

    Rtot_series=[]
    for series in wall:
        R=0
        for anylayer in series:
            R=R+Matrial_Library[anylayer]
        Rtot_series.append(R) 
    Ratio=FractionOfInsulation    
    Layers_series_Ufactor=[1/Rtot_series[0]*Ratio,1/Rtot_series[1]*(1-Ratio)]    
    U_wall=Layers_series_Ufactor[0]+Layers_series_Ufactor[1]
    
    R_door=0
    for layers in door:
        R_door=R_door+Matrial_Library[layers]
    U_door=1/R_door
    results={"the total U of the wall":U_wall,"the total U of the roof":roof,"the total U of the door":U_door}
    return results