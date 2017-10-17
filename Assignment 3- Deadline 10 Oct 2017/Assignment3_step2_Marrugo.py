# -*- coding: utf-8 -*-
#      Assigment 3 step 2 Calculation of the overall unit thermal resistance (the R-value) 
#             and the overall heat transfer coefficient (the U-factor) using "def" function

print """        Assigment 3 Calculation of the overall unit thermal resistance 
(the R-value) and the overall heat transfer coefficient (the U-factor) using "def" function \n"""

#  Librery of materials for the example

material={"Inside_surface":0.12,"Outside_surface": 0.03,
"Wood_bevel_lapped_siding": 0.14,"Wood_fiberboard_sheeting":0.23,
"Glass_fiber_insulation":2.45,"Wood stud":0.63,"Gypsum wallboard":0.079}

# List of materials in series configuration

ListS=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Glass_fiber_insulation","Gypsum wallboard"]

# List of materials in parallel configuration

ListP=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Wood stud","Gypsum wallboard"]

# Parameters of the wall [Heat area percentage, perimeter, height, 
# temperatura inside, temperature outside]
InputsWall={"HeatArea%":0.8,"Perimeter":50,"Height":2.5,"Tin":22,"Tout":-2}

# Declaration of the function for calculate the thermal resistance (m2*ºC/W) 
# according with the list of materials
def wall(ListS,listP,percentage):
    
    # Adding the thermal resistance for the inside and outside surface
    airofboth=["Inside_surface","Outside_surface"]
    # Defining the total list of materials in series 
    LayerS=ListS+airofboth
    # Defining the total list of materials in parallel 
    LayerP=ListP+airofboth
    # Defining lenght of list of materials in series
    x=len(LayerS)
    # Defining an accounter
    y=0
    # Defining the total list of materials
    List=LayerS+LayerP
    # Defining the variables for the total unit thermal resistance in series and parallel
    Rtotals=0
    Rtotalp=0
    # Defining the variable for the unit thermal resistance of each material
    Rvalues_layers={}
    
    # Defining the for cycle to acquired and compute the unit thermal resistance for a 
    # specific material in the list of materials 
    
    for anylayer in List:
        
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

    # Computing of the total area of the heat tranfer
    A=InputsWall["HeatArea%"]*InputsWall["Perimeter"]*InputsWall["Height"]
    
    # Computing the overall heat transfer coefficient of the wall according with its 
    # respectively U-factor and area percentages for the list of materials 
    # in series and parallel in in [W/m2*ºC]
    Uoverall=(1/Rtotals)*(float(percentage))+(1/Rtotalp)*(1-float(percentage))
    
    # Computing the overall unit thermal resistance for the wall in [m2*ºC/W]
    Roverall=1/Uoverall
    
    # Computing of the total area of the heat tranfer
    A=InputsWall["HeatArea%"]*InputsWall["Perimeter"]*InputsWall["Height"]
    
    # Computing the rate of heat loss through the all heat transfer areas 
    Q=Uoverall*A*(InputsWall["Tin"]-InputsWall["Tout"])
    
    # Returning of the results
    
    Results={"Rtotal":Roverall,"Resistances":Rvalues_layers,"Utotal":Uoverall,"Q":Q}
    return Results

# Compute the total unit thermal resistance for the materials in series and parallel in [m2*ºC/W]
results=wall(ListS,ListP,0.75)


# Showing results to the user
print "The list of resistances in W/m2*C are ",results["Resistances"],"\n"
print "The overall unit thermal resistance is",results["Rtotal"],"m2*ºC/W \n"
print "The overall heat transfer coefficient is ",results["Utotal"],"W/m2*ºC \n"
print "The rate of heat loss through the walls is ",results["Q"],"W \n"