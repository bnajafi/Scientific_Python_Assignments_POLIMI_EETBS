# -*- coding: utf-8 -*-
def WallCalculatorAssignment(WallSer,WallPar,AreaFraction):
    """This function calculates the overall resistance and conductivity of a wall with two layers in parallel as seen in the exercise 1 of chapter 1.3"""
    
    """The input needed are: a list of the layers in series, a list containing the two layers in parallel and the fraction of the area of the insulation over the total area of the wall """
    
    Matetials_Dictionary = {"Wood_Bevel_Lapped_Siding":0.14,"Wood_Fiberboard_Sheeting":0.23,"Glass_Fiber_Insulation":2.45,"Wood_Stud":0.63,"Gypsum_Wallboard":0.079,"Outside_Surface_Winter":0.03,"Inside_Surface":0.12}
    
    Air = ["Outside_Surface_Winter","Inside_Surface"]
    
    RSeriesValues = []

    RParallelValues = []

    RAirValues = []

    RSerTot = 0

    RAirTot = 0
    
    for AnyLayer in WallSer:
        RValueSer = Matetials_Dictionary[AnyLayer]
        RSeriesValues.append(RValueSer)
        RSerTot = RSerTot + RValueSer   
        print "This layer is "+AnyLayer
        print "The resistance of " +AnyLayer +" is "+str(RValueSer) +" m^2*°C/W"
    print "**********************************************************************************************"
    print "The total value of the conduvtive resistances in series is "+str(RSerTot) +" m^2*°C/W"
    print "**********************************************************************************************"
    
    for AnyLayer in Air:
        RValueAir = Matetials_Dictionary[AnyLayer]
        RAirValues.append(RValueAir)
        RAirTot = RAirTot + RValueAir   
        print "This layer is "+AnyLayer
        print "The convective resistance of " +AnyLayer +" is "+str(RValueAir) +" m^2*°C/W"
    print "**********************************************************************************************"
    print "The total value of the convective resistances is "+str(RAirTot) +" m^2*°C/W"
    
    
    Uoverall = 0
    
    for AnyLayer in WallPar:
        RValuePar = Matetials_Dictionary[AnyLayer]
        RParallelValues.append(RValuePar)
        print "This layer is "+AnyLayer
        print "The resistance of " +AnyLayer +" is "+str(RValuePar) +" m^2*°C/W"
        Rsection = RSerTot + RAirTot + RValuePar
        Usection = 1 / Rsection
        if (AnyLayer=="Glass_Fiber_Insulation"):
            AreaCoeff=AreaFraction
        else:
            AreaCoeff=1-AreaFraction
      
        Uoverall = Uoverall + Usection*AreaCoeff
    
        print "The conductivity of the section with "+AnyLayer+" is "+str(Usection)+" W/(m^2*°C)"
    print "**********************************************************************************************"
    print "The overall conductivity of the wall is "+str(Uoverall)+" W/(m^2*°C)"
    
    Roverall = 1 / Uoverall

    print "**********************************************************************************************"
    print "The overall resistance of the wall is "+str(Roverall)+" m^2*°C/W"
    print "**********************************************************************************************"
    
    result = {"Roverall":Roverall,"Uoverall":Uoverall,"RSeriesValues":RSeriesValues,"RParallelValues":RParallelValues}
    
    return result

#************************FUNCTION***TEST********************************************************

Wall_Series_List = ["Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Gypsum_Wallboard"]

Area_Fraction= 0.75

Wall_Parallel_List = ["Glass_Fiber_Insulation","Wood_Stud"]

WallCalculatorAssignment(Wall_Series_List,Wall_Parallel_List,Area_Fraction)
