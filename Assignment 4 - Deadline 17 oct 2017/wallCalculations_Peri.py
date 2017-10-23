## step1 Peri




def wallCalc_withParallel (L_series,L_parallel,Ratio_sp): 
    MaterialLibrary={"AsphaltRoofing":0.077,"Wood_50mm":0.44,"slag_13mm":0.067,"AcousticTile":0.32,"BuildingPaper":0.011,"gypsumBoard":0.079,"CommonBrik":0.12,
    "FaceBrik_100mm":0.075,"Outside_surface_summer":0.044,"Outside_surface_winter":0.03,"Inside_surface":0.12,"insulation_glassFiber":2.52,"WoodStud_90mm":0.63,
    "WoodFiberboard_13mm":0.23,"Stucco_25mm":0.037,"WoodBevel":0.14}
    
    
    V_Rtot=[];
    for comp in L_parallel:
        L_series.append(comp)
        
        Rcalc=0
        for comp in L_series:
            Rvalue=MaterialLibrary[comp]
            Rcalc=Rcalc+Rvalue
        print "the resistance of the section is: "+str(Rcalc)+" degC/W"
        V_Rtot.append(Rcalc)
        print "---------------------"
        L_series.pop(-1)
        
        
    Utot=((V_Rtot[0]**-1)*(1-Ratio_sp))+((V_Rtot[1]**-1)*(Ratio_sp))
    print "Utot value for this wall is: "+str(Utot)+" W/degC"
    results=Utot
    return results


def wallCalc_onlySeries(layers_list):
    
    MaterialLibrary={"AsphaltRoofing":0.077,"Wood_50mm":0.44,"slag_13mm":0.067,"AcousticTile":0.32,"BuildingPaper":0.011,"gypsumBoard":0.079,"CommonBrik":0.12,
    "FaceBrik_100mm":0.075,"Outside_surface_summer":0.044,"Outside_surface_winter":0.03,"Inside_surface":0.12,"insulation_glassFiber":2.52,"WoodStud_90mm":0.63,
    "WoodFiberboard_13mm":0.23,"Stucco_25mm":0.037,"WoodBevel":0.14}
    
    
    R_series=0
    
    for layer in layers_list:
        Rvalue=MaterialLibrary[layer]
        R_series=R_series+Rvalue
    print "the value of the series resistance of the input list is: "+str(R_series)+" degC/W"
    Utot=1/R_series
    result2=Utot
    print "the overall heat transfer coeff is: "+str(Utot)+ " W/degC"
    return result2  
        