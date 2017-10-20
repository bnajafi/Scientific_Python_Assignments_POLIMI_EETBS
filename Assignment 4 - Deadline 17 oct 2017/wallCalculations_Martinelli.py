Material_library = {"stucco_13mm":0.023,"FaceBrick_100mm":0.075,"BuildingPaper":0.011,"Plywood_13mm":0.11,"insideSurface":0.12,"outsideSurfaceSummer":0.044,"wood_50mm":0.44,
"outsideSurfaceWinter":0.03,"woodFiberboard_13mm":0.23,"WoodBevelLappedSiding":0.14,"glassFiberInsulation_90mm":2.52,"woodStud_38x90mm":0.63,"gypsiumWallboard_13mm":0.079,"commonBrick_100mm":0.12}

#f_ins = 0.7

#layers_wall_series = ["gypsiumWallboard_13mm","commonBrick_100mm","woodFiberboard_13mm","WoodBevelLappedSiding"]
#layers_wall_par = ["glassFiberInsulation_90mm","woodStud_38x90mm"]
airOnTwoSides_win = ["insideSurface","outsideSurfaceWinter"]
airOnTwoSides_sum = ["insideSurface","outsideSurfaceSummer"]

def wallCalc_onlyInSeries(listS):
    layers_wall_series_sum = listS + airOnTwoSides_sum
    layers_wall_series_win = listS + airOnTwoSides_win
    Rtot_series_sum = 0
    Rtot_series_win = 0
    
    for anyLayer in layers_wall_series_sum:
        Rvalue_layer_series_sum = Material_library[anyLayer]
        Rtot_series_sum = Rtot_series_sum + Rvalue_layer_series_sum
    
    for anyLayer in layers_wall_series_win:
        Rvalue_layer_series_win = Material_library[anyLayer]
        Rtot_series_win = Rtot_series_win + Rvalue_layer_series_win

    Utot_sum = 1/Rtot_series_sum
    Utot_win = 1/Rtot_series_win  
    
    Rseries = {"Utot_sum":Utot_sum,"Utot_win":Utot_win,"Rvalue of all layers in summer":Rtot_series_sum,"Rvalue of all layers in winter":Rtot_series_win} 
    return Rseries


def wallCalc_withParallel(listSer,listPar,r): #we don't know how many variables, so we define a list
    layers_wall_series_sum = listSer + airOnTwoSides_sum
    layers_wall_series_win = listSer + airOnTwoSides_win
    Rtot_series_sum = 0
    Rtot_series_win = 0
    
    for anyLayer in layers_wall_series_sum:
        Rvalue_layer_series_sum = Material_library[anyLayer]
        Rtot_series_sum = Rtot_series_sum + Rvalue_layer_series_sum
    
    for anyLayer in layers_wall_series_win:
        Rvalue_layer_series_win = Material_library[anyLayer]
        Rtot_series_win = Rtot_series_win + Rvalue_layer_series_win
    
    res_tot_sum = []
    res_tot_win = []
    layers_wall_par = listPar
    for anyLayer in layers_wall_par:
        Rvalue_layer = Material_library[anyLayer]
        res_tot_sum.append(Rvalue_layer + Rtot_series_sum)
        res_tot_win.append(Rvalue_layer + Rtot_series_win)

    Utot_ins_sum = 1/res_tot_sum[0]
    Utot_wood_sum = 1/res_tot_sum[1]    
    Utot_ins_win = 1/res_tot_win[0]
    Utot_wood_win = 1/res_tot_win[1]
    
    Utot_sum = r*Utot_ins_sum + (1-r)*Utot_wood_sum
    Rtot_sum = 1/Utot_sum
    Utot_win = r*Utot_ins_win + (1-r)*Utot_wood_win
    Rtot_win = 1/Utot_win
    
    Results = {"Rtot_ins_sum":res_tot_sum[0],"Rtot_wood_sum":res_tot_sum[1],"Utot_sum":Utot_sum,"Rvalue of all layers in summer":Rtot_sum,
               "Rtot_ins_win":res_tot_win[0],"Rtot_wood_win":res_tot_win[1],"Utot_win":Utot_win,"Rvalue of all layers in winter":Rtot_win} #resistances of the wall as if it was all insulated or all wooden
    return Results