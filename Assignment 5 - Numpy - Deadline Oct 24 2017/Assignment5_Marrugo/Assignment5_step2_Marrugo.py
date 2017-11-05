# -*- coding: utf-8 -*-
#      Assigment 5 Step 2 Calculation of the overall unit thermal resistance (the R-value) 
#             and the overall heat transfer coefficient (the U-factor) using numpy

print """        Assigment 5 step 2 Calculation of the overall unit thermal resistance 
(the R-value) and the overall heat transfer coefficient (the U-factor) using numpy \n"""


#  import library

import numpy as np

#  Librery of materials for the example

material_librery_names=np.array(["Inside_surface","Outside_surface",
"Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Glass_fiber_insulation","Wood stud","Gypsum wallboard"])
material_librery_values=np.array([0.12,0.03,0.14,0.23,2.45,0.63,0.079])

# List of materials in series configuration

ListSeries=np.array(["Inside_surface","Outside_surface","Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Glass_fiber_insulation","Gypsum wallboard"])

# List of materials in parallel configuration

ListParallel=np.array(["Inside_surface","Outside_surface","Wood_bevel_lapped_siding","Wood_fiberboard_sheeting",
"Wood stud","Gypsum wallboard"])


# Parameters of the wall [Heat area percentage, perimeter, height, 
# temperatura inside, temperature outside]
InputsWall={"HeatArea%":0.7,"Perimeter":50,"Height":2.5,"Tin":22,"Tout":-2}
# Ratio of the series resistances
percentage=0.75

# Defining the variables for the total thermal resistance
RtotalS=0
RtotalP=0
# Defining the variable for the thermal resistance of each material
Rvalues_layer=np.array(np.zeros(material_librery_names.size))


# Compute the total unit thermal resistance for the materials in series in [m2*C/W]


for anylayer in ListSeries:
    
    # Acquiring the thermal resistance for the specific material of the list in [m2*C/W]
    Rvalues_layer[material_librery_names==anylayer]=material_librery_values[material_librery_names==anylayer]
    # Computing the sum of each unit thermal resistance of each material in [m2*C/W]
    RtotalS=RtotalS+Rvalues_layer[material_librery_names==anylayer]

    
# Compute the total unit thermal resistance for the materials in parallel in [m2*C/W]

for anylayer in ListParallel:
    
    Rvalues_layer[material_librery_names==anylayer]=material_librery_values[material_librery_names==anylayer]
    # Computing the sum of each unit thermal resistance of each material in [m2*C/W]
    RtotalP=RtotalP+Rvalues_layer[material_librery_names==anylayer]
    

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

# Defining the list of materials as a dictionary
layerS={}
for name in material_librery_names:
    #Acquiring valus of each material 
    layer={name:Rvalues_layer[material_librery_names==name][0]}
    #Saving the value of the material in the dictionary    
    layerS.update(layer)
    
# Showing results to the user
print "The list of resistances in W/m2*C are ",layerS,"\n"
print "The overall unit thermal resistance is",Roverall[0],"m2*ºC/W \n"
print "The overall heat transfer coefficient is ",Uoverall[0],"W/m2*ºC \n"
print "The rate of heat loss through the walls is ",Q[0],"W \n"