Material_Library = {"Outside_surface_Winter":0.030,"Inside_surface": 0.12,
"Insulation_Glass_Fiber_90mm":2.52, "WoodStud_90mm":0.63, 
"WoodFiberboard": 0.23,"WoodBevel_13x200": 0.14,"Gypsum_13mm":0.079,"CommonBrick_100mm":0.12,"Wood_50mm":0.44,
"MineralFiberBat_150mm":3.96}

def wallCalc_withParallel(Layers_Wall_Parallel,Layers_Wall_Serie,fraction):    
    Rtot=0
    Rvalues_serie=[]
    for anyLayer in Layers_Wall_Serie:
        RValue= Material_Library[anyLayer]
        Rtot = Rtot+RValue
        Rvalues_serie.append(RValue)
    
    Layers_Glass=Layers_Wall_Serie+[Layers_Wall_Parallel[0]]
    RValue_glass= Material_Library["Insulation_Glass_Fiber_90mm"]
    Rtot_g=Rtot+RValue_glass
    Rvalues_serie.append(RValue_glass)
    U_glass=1/Rtot_g
    
    Layers_Stud=Layers_Wall_Serie+[Layers_Wall_Parallel[1]]
    RValue_stud= Material_Library["WoodStud_90mm"]
    Rtot_s=Rtot+RValue_stud
    Rvalues_serie.append(RValue_stud)
    U_stud=1/Rtot_s
    
    U_tot=fraction*(U_glass)+(1-fraction)*(U_stud)
    R_TOT=1/U_tot
    results=U_tot
    return results
    
Layers_Wall_Serie = ["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","Gypsum_13mm","Inside_surface","CommonBrick_100mm"] 
Layers_Wall_Parallel= ["Insulation_Glass_Fiber_90mm","WoodStud_90mm"]
fraction=0.7
results_wall=wallCalc_withParallel(Layers_Wall_Parallel,Layers_Wall_Serie,fraction)

def wallCalc_onlyInSeries(Layers):    
    Rtot=0
    Rvalues_serie=[]
    for anyLayer in Layers:
        RValue= Material_Library[anyLayer]
        Rtot = Rtot+RValue
        Rvalues_serie.append(RValue)
        U=1/Rtot
    results=U
    return results
Layers_door=["Outside_surface_Winter","Inside_surface","Wood_50mm"]
Layers_roof=["Outside_surface_Winter","Inside_surface","MineralFiberBat_150mm","WoodFiberboard",]
results_door=wallCalc_onlyInSeries(Layers_door)
results_roof=wallCalc_onlyInSeries(Layers_roof)
