# -*- coding: utf-8 -*-
#      Assigment 4 Functions for Calculation of the overall unit thermal resistance (the R-value) 
#             and the overall heat transfer coefficient (the U-factor) in parallel and series


#  Librery of materials 
material={"Inside_surface":0.12,"Outside_surface_winter": 0.030,
"Outside_surface_summer": 0.044,"Common_brick":0.12,
"Wood_bevel_lapped_siding": 0.14,"Wood_fiberboard_sheeting":0.23,
"Glass_fiber_insulation":2.52,"Wood stud":0.63,"Gypsum_wallboard":0.079,"Wood":0.44,"Asphalt_shingle_roofing":0.077,"Plywood":0.11}

def matSeries(List):
    """Function designed for calculate the overall unit thermal resistance (the R-value) 
#     and the overall heat transfer coefficient (the U-factor) for a element with all materials in series"""
    # Adding the thermal resistance for the inside and outside surface for winter and summer
    Winter=["Inside_surface","Outside_surface_winter"]
    Summer=["Inside_surface","Outside_surface_summer"]
    
    # Defining the total list of materials in series for winter and summer
    LSwinter=List+Winter
    LSsummer=List+Summer  
    
    # Defining the variables for the total unit thermal resistance in series and parallel
    Rtotals=0
    Rtotalw=0
    # Defining the variable for the unit thermal resistance of each material
    Rvalues_layers={}
    
    
    # Defining the for cycle to acquired and compute the unit thermal resistance for 
    # Summer season
    for anylayer in LSsummer:
        
        # Acquiring the thermal resistance for the specific material of the list in [m2*ºC/W]
        Rvalue_layer=material[anylayer]
        # Computing the sum of each unit thermal resistance of each material in series in [m2*ºC/W]
        Rtotals=Rtotals+Rvalue_layer
        # Saving the value of each unit thermal resistance of each material in [m2*ºC/W]
        Rdict={anylayer:Rvalue_layer}
        Rvalues_layers.update(Rdict)
    for anylayer in LSwinter:
        
        # Acquiring the thermal resistance for the specific material of the list in [m2*ºC/W]
        Rvalue_layer=material[anylayer]
        # Computing the sum of each unit thermal resistance of each material in series in [m2*ºC/W]
        Rtotalw=Rtotalw+Rvalue_layer
        # Saving the value of each unit thermal resistance of each material in [m2*ºC/W]
        Rdict={anylayer:Rvalue_layer}
        Rvalues_layers.update(Rdict)

    # Computing the overall heat transfer coefficient of the wall according with its 
    # respectively U-factor and area percentages for the list of materials 
    # in series and parallel in winter and summer [W/m2*ºC]
    Uoverallw=(1/Rtotalw)
    Uoveralls=(1/Rtotals)
    
    Results={"Resistances":Rvalues_layers,"Rtotal_Winter":Rtotalw,"Utotal_winter":Uoverallw,"Rtotal_Summer":Rtotals,"Utotal_Summer":Uoveralls}
    return Results

def matParallel(ListS,ListP,percentage):    
    """Function designed for calculate the overall unit thermal resistance (the R-value) 
#     and the overall heat transfer coefficient (the U-factor) for a element with materials in parallel"""

    
    # Adding the thermal resistance for the inside and outside surface for winter and summer
    Winter=["Inside_surface","Outside_surface_winter"]
    Summer=["Inside_surface","Outside_surface_summer"]
    
    # Defining the total list of materials in series for winter and summer
    LSwinter=ListS+Winter
    LSsummer=ListS+Summer
    
    # Defining the total list of materials in parallel for winter and summer
    LPwinter=ListP+Winter
    LPsummer=ListP+Summer
    
    # Defining lenght of list of materials 
    x=len(LSwinter)
    # Defining an accounter
    y=0
    
    # Defining the total list of materials for winter and summer
    ListWinter=LSwinter+LPwinter
    ListSummer=LSsummer+LPsummer
    
    # Defining the variables for the total unit thermal resistance in series and parallel
    Rtotals=0
    Rtotalp=0
    # Defining the variable for the unit thermal resistance of each material
    Rvalues_layers={}
    
    
    # Defining the for cycle to acquired and compute the unit thermal resistance for 
    # Summer season
    for anylayer in ListSummer:
        
        # Acquiring the thermal resistance for the specific material of the list in [m2*ºC/W]
        Rvalue_layer=material[anylayer]
        
        if y<x:
            # Computing the sum of each unit thermal resistance of each material in series in [m2*ºC/W]
            Rtotals=Rtotals+Rvalue_layer
            # Saving the value of each unit thermal resistance of each material in [m2*ºC/W]
            Rdict={anylayer:Rvalue_layer}
            Rvalues_layers.update(Rdict)
        else:
            # Computing the sum of each unit thermal resistance of each material in parallel in [m2*ºC/W]
            Rtotalp=Rtotalp+Rvalue_layer
            # Saving the value of each unit thermal resistance of each material in [m2*ºC/W]
            Rdict={anylayer:Rvalue_layer}
            Rvalues_layers.update(Rdict)
        # Counting
        y=y+1
    
    
    # Computing the overall heat transfer coefficient of the wall according with its 
    # respectively U-factor and area percentages for the list of materials 
    # in series and parallel in summer [W/m2*ºC]
    UoverallS=(1/Rtotals)*(float(percentage))+(1/Rtotalp)*(1-float(percentage))
    
    # Computing the overall unit thermal resistance for the wall in summer  [m2*ºC/W]
    RoverallS=1/UoverallS
    
    # Reset of accounter variables
    Rtotals=0
    Rtotalp=0
    y=0
    
    # Defining the for cycle to acquired and compute the unit thermal resistance for 
    # Winter season
    
    for anylayer in ListWinter:
        
        # Acquiring the thermal resistance for the specific material of the list in [m2*ºC/W]
        Rvalue_layer=material[anylayer]
        
        if y<x:
            # Computing the sum of each unit thermal resistance of each material in series in [m2*ºC/W]
            Rtotals=Rtotals+Rvalue_layer
            # Saving the value of each unit thermal resistance of each material in [m2*ºC/W]
            Rdict={anylayer:Rvalue_layer}
            Rvalues_layers.update(Rdict)
        else:
            # Computing the sum of each unit thermal resistance of each material in parallel in [m2*ºC/W]
            Rtotalp=Rtotalp+Rvalue_layer
            # Saving the value of each unit thermal resistance of each material in [m2*ºC/W]
            Rdict={anylayer:Rvalue_layer}
            Rvalues_layers.update(Rdict)
        # Counting
        y=y+1
    
    
    # Computing the overall heat transfer coefficient of the wall according with its 
    # respectively U-factor and area percentages for the list of materials 
    # in series and parallel in winter [W/m2*ºC]
    UoverallW=(1/Rtotals)*(float(percentage))+(1/Rtotalp)*(1-float(percentage))
    
    # Computing the overall unit thermal resistance for the wall winter [m2*ºC/W]
    RoverallW=1/UoverallW
    # Returning of the results
    
    Results={"Resistances":Rvalues_layers,"Rtotal_Winter":RoverallW,"Utotal_winter":UoverallW,"Rtotal_Summer":RoverallS,"Utotal_Summer":UoverallS}
    return Results




