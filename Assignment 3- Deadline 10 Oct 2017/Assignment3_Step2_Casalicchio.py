# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146

Step 2: you should define a function that does exactly the same procedure as step 1. The function should receive three inputs: list of layers in series, 
list of the two  layers in parallel, and the ratio between the area of the first layer in the parallel list to the total one. The function should include 
a documentation and should return a dictionary which includes the thermal resistances of all layers, Total resistance and the total U of the wall.
"""
#Definition of the function
def Wall_Function(Layers_In_Series, Layers_In_Parallel, Ratio_Insulation):

    #Definition of the materials' library
    Library_Material = {"Outside_Surface_Winter":0.030,
                        "Wood_Bevel_Lapped_Siding": 0.14,
                        "Wood_Fiberboard_Sheeting": 0.23,  
                        "Glass_Fiber_Insulation":2.45, 
                        "Wood_Stud":0.63,
                        "Gypsum_Wallboard":0.079,
                        "Inside_Surface": 0.12}
    
    Layers_Air=["Outside_Surface_Winter","Inside_Surface"]
    
    
    #Monitor the serie and parallel layers
    Tot_R_Series=0
    for anyLayer in Layers_In_Series:
        Tot_R_Series=Tot_R_Series+Library_Material[anyLayer]
    
    List_R=[]  
    for anyLayer in Layers_In_Parallel:
        R_Parallel=Tot_R_Series+Library_Material[anyLayer]
        List_R.append(R_Parallel)
    
    #Calculate  the total global heat transfer coefficient and the total thermal resistance
    Tot_U=round(Ratio_Insulation/List_R[0]+(1-Ratio_Insulation)/List_R[1],4)
    Tot_R=round(1/Tot_U,4)
    
    Results = {"GLOBAL HEAT TRANSFER COEFFICIENT":{"N.VALUE":Tot_U,"U.MEASURE":"[W/m2C]"}, "TOTAL THERMAL RESISTANCE":{"N.VALUE":Tot_R,"U.MEASURE":"[m2C/W]"}}
    return Results
    
#Definition of the lists of the materials in series and in parallel (INPUT)
Layers_In_Series=["Outside_Surface_Winter","Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Gypsum_Wallboard","Inside_Surface"]
Layers_In_Parallel=["Glass_Fiber_Insulation","Wood_Stud"]

#Definition of the relationship between the area of the first parallel layer and the total one (INPUT)
Ratio_Insulation=float(0.75)       

Results_Wall_Function=Wall_Function(Layers_In_Series, Layers_In_Parallel, Ratio_Insulation)
print Results_Wall_Function