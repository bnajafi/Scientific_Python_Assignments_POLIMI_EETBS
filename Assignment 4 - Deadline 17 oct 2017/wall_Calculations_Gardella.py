def wallCalc_withParallel(WallSer,WallPar,AreaFraction):
    """This function calculates the overall resistance and conductivity of a wall with two layers in parallel as seen in the exercise 1 of chapter 1.3"""
    
    """The input needed are: a list of the layers in series, a list containing the two layers in parallel and the fraction of the area of the insulation over the total area of the wall """
    
    Matetials_Dictionary = {"Wood_Bevel_Lapped_Siding":0.14,"Wood_Fiberboard_Sheeting":0.23,"Glass_Fiber_Insulation":2.45,"Wood_Stud":0.63,"Gypsum_Wallboard":0.079,"Outside_Surface_Winter":0.03,"Inside_Surface":0.12,"Wood":0.44}
    
    
    Air = ["Outside_Surface_Winter","Inside_Surface"]
    
    RSerTot = 0

    RAirTot = 0
    
    for AnyLayer in WallSer:
        RValueSer = Matetials_Dictionary[AnyLayer]
        RSerTot = RSerTot + RValueSer   
    
    for AnyLayer in Air:
        RValueAir = Matetials_Dictionary[AnyLayer]
        RAirTot = RAirTot + RValueAir   
    
    
    UPartot = 0
    
    for AnyLayer in WallPar:
        RValuePar = Matetials_Dictionary[AnyLayer]
        Rsection = RSerTot + RAirTot + RValuePar
        Usection = 1 / Rsection
        if (AnyLayer=="Glass_Fiber_Insulation"):
            AreaCoeff=AreaFraction
        else:
            AreaCoeff=1-AreaFraction
      
        UPartot = UPartot + Usection*AreaCoeff
    
    
    RPartot = 1 / UPartot

    Rtot=RSerTot+RAirTot+RPartot
    
    Utot=1/Rtot
    
    result = {"RPartot":RPartot,"UPartot":UPartot,"Rtot":Rtot,"Utot":Utot}
    
    return result
    
def wallCalc_onlyInSeries(WallSer):
    """This function calculates the overall resistance and conductivity of a wall with only layers in series"""
    
    """The input needed is a list of the layers in series """

    Matetials_Dictionary = {"Wood_Bevel_Lapped_Siding":0.14,"Wood_Fiberboard_Sheeting":0.23,"Glass_Fiber_Insulation":2.45,"Wood_Stud":0.63,"Gypsum_Wallboard":0.079,"Outside_Surface_Winter":0.03,"Inside_Surface":0.12,"Wood":0.44}
    
    Air = ["Outside_Surface_Winter","Inside_Surface"]   
    
    RSerTot = 0

    RAirTot = 0
    
    for AnyLayer in WallSer:
        RValueSer = Matetials_Dictionary[AnyLayer]
        RSerTot = RSerTot + RValueSer   
    
    for AnyLayer in Air:
        RValueAir = Matetials_Dictionary[AnyLayer]
        RAirTot = RAirTot + RValueAir   
    
    Rtot=RSerTot+RAirTot
    
    Utot=1/Rtot
                
    result = {"Rtot":Rtot,"Utot":Utot}
    
    return result
   
