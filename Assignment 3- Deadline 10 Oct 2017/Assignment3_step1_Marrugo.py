# -*- coding: utf-8 -*-
#      Assigment 3 Step 1 Calculation of the overall unit thermal resistance (the R-value) 
#             and the overall heat transfer coefficient (the U-factor) using "for" function

print """        Assigment 3 step 1 Calculation of the overall unit thermal resistance 
(the R-value) and the overall heat transfer coefficient (the U-factor) using "for" function \n"""

#  Librery of materials for the example

material_librery={"Inside_surface":0.12,"Outside_surface": 0.03,
"Wood_bevel_lapped_siding": 0.14,"Wood_fiberboard_sheeting":0.23,
"Glass_fiber_insulation":2.45,"Wood stud":0.63,"Gypsum wallboard":0.079}

# List of materials in series configuration

ListSeries=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Glass_fiber_insulation","Gypsum wallboard"]

# List of materials in parallel configuration

ListParallel=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Wood stud","Gypsum wallboard"]


# Parameters of the wall [Heat area percentage, perimeter, height, 
# temperatura inside, temperature outside]
InputsWall={"HeatArea%":0.8,"Perimeter":50,"Height":2.5,"Tin":22,"Tout":-2}
# Ratio of the series resistances
percentage=0.75


# Adding the thermal resistance for the inside and outside surface
airofboth=["Inside_surface","Outside_surface"]
# Defining the total list of materials in series
LayerS=ListSeries+airofboth
# Defining the total list of materials in parallel
LayerP=ListParallel+airofboth
# Defining the variables for the total thermal resistance
RtotalS=0
RtotalP=0
# Defining the variable for the thermal resistance of each material
Rvalues_layerS={}

# Compute the total unit thermal resistance for the materials in series in [m2*C/W]


for anylayer in LayerS:
    
    # Acquiring the thermal resistance for the specific material of the list in [m2*C/W]
    Rvalue_layer=material_librery[anylayer]
    # Computing the sum of each unit thermal resistance of each material in [m2*C/W]
    RtotalS=RtotalS+Rvalue_layer
    # Saving the value of each unit thermal resistance of each material in [m2*C/W]
    layer={anylayer:Rvalue_layer}
    Rvalues_layerS.update(layer)
    
# Compute the total unit thermal resistance for the materials in parallel in [m2*C/W]

for anylayer in LayerP:
    
    # Acquiring the thermal resistance for the specific material of the list in [m2*C/W]
    Rvalue_layer=material_librery[anylayer]
    # Computing the sum of each unit thermal resistance of each material in [m2*C/W]
    RtotalP=RtotalP+Rvalue_layer
    # Saving the value of each unit thermal resistance of each material in [m2*C/W]
    layer={anylayer:Rvalue_layer}
    Rvalues_layerS.update(layer)
    

# Compute the overall heat transfer coefficient of the wall according with its 
# respectively U-factor and area percentages for the list of materials 
# in series and parallel in in [W/m2*C]
Uoverall=(1/RtotalS)*(percentage)+(1/RtotalP)*(1-percentage)

# Compute the overall unit thermal resistance for the wall in [m2*C/W]
Roverall=1/Uoverall


# computing of the total area of the heat tranfer
A=InputsWall["HeatArea%"]*InputsWall["Perimeter"]*InputsWall["Height"]

# Computing the rate of heat loss through the all heat transfer areas 
Q=Uoverall*A*(InputsWall["Tin"]-InputsWall["Tout"])

# Showing results to the user
print "The list of resistances in W/m2*C are ",Rvalues_layerS,"\n"
print "The overall unit thermal resistance is",Roverall,"m2*ºC/W \n"
print "The overall heat transfer coefficient is ",Uoverall,"W/m2*ºC \n"
print "The rate of heat loss through the walls is ",Q,"W \n"