def HeatTransfert_calc(Layers_Wall_series,Layers_Wall_par,f_ins): 
    
    Material_library = {"OutsideSurfaceWinter":0.03,"WoodBevelLapperSiding":0.14,
    "WoodFiberBoard_13mm":0.23,"GlassFiberInsultation_90mm":2.45,"FaceBreak_100m":0.075,
    "Wood stud_38mm*90mm":0.63,"GypsumWallBoard_13mm":0.079,"InsideSurface":0.12}
    
    Layers_Wall_series = ["WoodBevelLapperSiding","WoodFiberBoard_13mm","GypsumWallBoard_13mm"]
    
    Layers_Wall_par = ["GlassFiberInsultation_90mm","Wood stud_38mm*90mm"]
    
    AirOnTwoSides = ["InsideSurface","OutsideSurfaceWinter"]
    
    Layers_Wall_series_tot = Layers_Wall_series + AirOnTwoSides
    Rtot_series = 0
    
    for anyLayer in Layers_Wall_series_tot:
        Rvalue_Layer = Material_library[anyLayer] 
        Rtot_series = Rtot_series + Rvalue_Layer
    
    r_tot = []
    for anyLayer in Layers_Wall_par:
        Rvalue_Layer = Material_library[anyLayer]
        r_tot.append(Rvalue_Layer + Rtot_series)
        
    U_tot_ins = 1/r_tot[0]
    U_tot_wood = 1/r_tot[1]
    U_overall = U_tot_ins*f_ins + (1-f_ins)*U_tot_wood
    
    Rtot = 1/U_overall
    
    Results = {"Rtot_series":Rtot_series,"Rtot_ins":r_tot[0],"Rtot_wood":r_tot[1],"U_overall":U_overall,"Rtot":Rtot}
    
    return Results

Layers_Wall_series = ["WoodBevelLapperSiding","WoodFiberBoard_13mm","GypsumWallBoard_13mm"]

Layers_Wall_par = ["GlassFiberInsultation_90mm","Wood stud_38mm*90mm"]

results_thisWall = HeatTransfert_calc(Layers_Wall_series,Layers_Wall_par,0.75)

print "the results for this wall are " + str(results_thisWall)