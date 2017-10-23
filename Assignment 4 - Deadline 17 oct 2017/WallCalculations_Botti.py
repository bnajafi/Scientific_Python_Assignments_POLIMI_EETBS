# -*- coding: utf-8 -*-
def WallCalc_withParallel(WallSer,WallPar,AreaFraction):
    Materials_Dictionary = {"Outside_surface":0.030,"Wood_bevel_lapped_siding":0.14,"Wood_fiberboard_sheeting13mm":0.23,"Glass_fiber_insulation90mm":2.45,"Wood_stud38*90mm":0.63,"Gypsum_wallboard13mm":0.079,"Wood25mm":0.44,"Inside_surface":0.12}
    Air = ["Outside_surface","Inside_surface"]
    RSeriesValues = []
    RParallelValues = []
    RAirValues = []
    RSerTot = 0
    RAirTot = 0
    
    for AnyLayer in WallSer:
        RValueSer = Materials_Dictionary[AnyLayer]
        RSeriesValues.append(RValueSer)
        RSerTot = RSerTot + RValueSer   
        
    for AnyLayer in Air:
        RValueAir = Materials_Dictionary[AnyLayer]
        RAirValues.append(RValueAir)
        RAirTot = RAirTot + RValueAir   

    Uoverall = 0
    for AnyLayer in WallPar:
        RValuePar = Materials_Dictionary[AnyLayer]
        RParallelValues.append(RValuePar)
        Rsection = RSerTot + RAirTot + RValuePar
        Usection = 1 / Rsection
        if (AnyLayer=="Glass_fiber_insulation90mm"):
            AreaCoeff=AreaFraction
        else:
            AreaCoeff=1-AreaFraction
      
        Uoverall = Uoverall + Usection*AreaCoeff
    
    Roverall = 1 / Uoverall
    R_tot = RSerTot+RAirTot+Roverall
    U_tot = 1/R_tot
    
    result = {"R_tot":R_tot,"U_tot":U_tot}
    
    return result

def WallCalc_onlyInSeries(WallSer):    
    Materials_Dictionary = {"Outside_surface":0.030,"Wood_bevel_lapped_siding":0.14,"Wood_fiberboard_sheeting13mm":0.23,"Glass_fiber_insulation90mm":2.45,"Wood_stud38*90mm":0.63,"Gypsum_wallboard13mm":0.079,"Wood25mm":0.44,"Inside_surface":0.12}
    Air = ["Outside_surface","Inside_surface"]
    RSeriesValues = []
    RAirValues = []
    RSerTot = 0
    RAirTot = 0
    
    for AnyLayer in WallSer:
        RValueSer = Materials_Dictionary[AnyLayer]
        RSeriesValues.append(RValueSer)
        RSerTot = RSerTot + RValueSer   
        
    for AnyLayer in Air:
        RValueAir = Materials_Dictionary[AnyLayer]
        RAirValues.append(RValueAir)
        RAirTot = RAirTot + RValueAir   
    R_tot = RSerTot+RAirTot
    U_tot = 1/R_tot
    
    result = {"R_tot":R_tot,"U_tot":U_tot}
    
    return result
    
#**************************************TEST************************************************************
WallSerie = ["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting13mm","Gypsum_wallboard13mm"]
WallCalc_onlyInSeries(WallSerie)