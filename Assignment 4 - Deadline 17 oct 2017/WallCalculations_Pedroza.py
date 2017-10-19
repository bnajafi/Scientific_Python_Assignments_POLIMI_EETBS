# -*- coding: utf-8 -*-

#Dictionary with unit thermal resistance of common components used in buildings.
Material_Library = {"Outside_surface_Summer":0.044, "Outside_surface_Winter":0.030,"Inside_surface": 0.12,
                "Insulation_Glass_Fiber_90mm":2.52, "WoodStud_90mm":0.63, "WoodFiberboard": 0.23, 
                "Stucco_25":0.037, "WoodBevel_13x200": 0.14, "Gypsum_13mm":0.079, "CommonBrick_100mm": 0.12, "Wood_50mm":0.44}

#OVERALL HEAT TRANSFER COEFICCIENT 
def wallCalc_withParallel(L_WS, L_GF, A_GF):
    
    Layers_WoodStud = L_WS # The sum of all layers.
    Rtot_Stud = 0 
    Resistances={}
    
    for anyLayer in Layers_WoodStud:
        RValue = Material_Library[anyLayer]
        Rtot_Stud = Rtot_Stud + RValue
        Dict1={anyLayer:RValue} 
        Resistances.update(Dict1)

    
        #FOR GLASS FIBER
    Layers_GlassFiber = L_GF #For this case, 
    Rtot_Fiber = 0
        
    for anyLayer in Layers_GlassFiber:
        RValue = Material_Library[anyLayer]
        Rtot_Fiber = Rtot_Fiber + RValue
        Dict1={anyLayer:RValue} 
        Resistances.update(Dict1)
    
    U_Stud = 1/(Rtot_Stud) #Overall heat transfer coefficient, which is the inverse of the specific resistance.
    U_Fiber = 1/(Rtot_Fiber)
    
    U_Total = (A_GF)*(U_Fiber) + (1-A_GF)*(U_Stud)
    R_Total = 1/U_Total
    
    results = {"U_Total":U_Total, "R_Tot": R_Total, "Dict":Resistances}
    return results 


#ONLY IN SERIES
def wallCalc_onlyInSeries(RValues):
    Layers = RValues # The sum of all layers.
    Rtot = 0 
        
    for anyLayer in Layers:
        RValues = Material_Library[anyLayer]
        Rtot = Rtot + RValues

    U_tot = 1/(Rtot)
    return U_tot
    

#HEATING CALCULATIONS
def Q_heat (TempWinter, Area, Uheating):
    T_confort_Winter = 20
    T_heating = T_confort_Winter - TempWinter
    HF=Uheating*T_heating
    Q = (HF)*(Area)
    results = {"Area":Area, "U_heating":Uheating, "HF":HF, "Q_heating":Q}
    return results
    

#COOLING CALCULATIONS
def Q_cool (TempSummer, Area, Ucool, OFt, OFb, OFr, DR):
    T_confort_Summer = 24
    T_cooling = TempSummer - T_confort_Summer
    CF=Ucool*((T_cooling*OFt)+OFb+(OFr*DR))
    Q = (CF)*(Area)
    results = {"Area":Area, "U_cooling":Ucool, "CF":CF, "Q_cooling":Q}
    return results
    