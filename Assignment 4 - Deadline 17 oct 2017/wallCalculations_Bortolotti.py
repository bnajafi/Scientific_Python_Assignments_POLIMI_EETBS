def wallCalc_onlyInSeries(ListS):
    Material_library = {"OutsideSurfaceWinter":0.03,"WoodBevelLapperSiding_13mm*200mm":0.14,
    "WoodFiberBoard_13mm":0.23,"GlassFiberInsultation_90mm":2.52,"FaceBreak_100m":0.075,
    "WoodStud_38mm*90mm":0.63,"CommonBrick_100m":0.12,"GypsumWallBoard_13mm":0.079,"Wood_50mm":0.44,"InsideSurface":0.12}
    
    AirOnTwoSides = ["InsideSurface","OutsideSurfaceWinter"]
     
    Layers_Wall_series_tot = ListS + AirOnTwoSides
    Rtot_series = 0
       
    for anyLayer in Layers_Wall_series_tot:
           Rvalue_Layer = Material_library[anyLayer]
           Rtot_series = Rtot_series + Rvalue_Layer
       
    Utot_series = 1/Rtot_series  
       
    Results_series = {"Rtot_series":Rtot_series,"Utot_series":Utot_series}
       
    return Results_series
        
def wallCalc_withParallel(ListS,ListP,f_ins):
    Material_library = {"OutsideSurfaceWinter":0.03,"WoodBevelLapperSiding_13mm*200mm":0.14,
    "WoodFiberBoard_13mm":0.23,"GlassFiberInsultation_90mm":2.52,"FaceBreak_100m":0.075,
    "WoodStud_38mm*90mm":0.63,"CommonBrick_100m":0.12,"GypsumWallBoard_13mm":0.079,"Wood_50mm":0.44,"InsideSurface":0.12}
    
    AirOnTwoSides = ["InsideSurface","OutsideSurfaceWinter"]
    
    Layers_Wall_series_tot = ListS + AirOnTwoSides
    Rtot_series = 0
    
    for anyLayer in Layers_Wall_series_tot:
        Rvalue_Layer = Material_library[anyLayer]
        Rtot_series = Rtot_series + Rvalue_Layer
    
    r_tot = []
    for anyLayer in ListP:
        Rvalue_Layer = Material_library[anyLayer]
        r_tot.append(Rvalue_Layer + Rtot_series)
   
    U_tot_ins = 1/r_tot[0]
    U_tot_wood = 1/r_tot[1]
    U_overall = U_tot_ins*f_ins + (1-f_ins)*U_tot_wood
    Rtot = 1/U_overall
    
    Results = {"Rtot_series":Rtot_series,"Rtot_ins":r_tot[0],"Rtot_wood":r_tot[1],"U_overall":U_overall,"Rtot":Rtot}
    
    return Results
