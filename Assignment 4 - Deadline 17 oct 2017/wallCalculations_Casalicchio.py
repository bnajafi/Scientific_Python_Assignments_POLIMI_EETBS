# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146
"""
#Definition of the function
def Wall_Function(Global_Heat_Transfer_Coeff,Layers_In_Series, Layers_In_Parallel, Ratio_Insulation, 
                    N_Layers_In_Parallel, Area, Delta_T):

    #Definition of the materials' library
    Library_Material = {"Outside_Surface_Winter":0.030,
                        "Wood_Bevel_Lapped_Siding": 0.14,
                        "Wood_Fiberboard_Sheeting": 0.23,  
                        "Glass_Fiber_Insulation":2.45, 
                        "Wood_Stud":0.63,
                        "Gypsum_Wallboard":0.079,
                        "Common_Brick":0.12,
                        "Door_Wood":0.44,
                        "Inside_Surface": 0.12}
    
    Layers_Air=["Outside_Surface_Winter","Inside_Surface"]
    
    
    #Monitor the serie and parallel layers
    if Global_Heat_Transfer_Coeff == 0:
        Tot_R_Series=0
        for anyLayer in Layers_In_Series:
            Tot_R_Series=Tot_R_Series+Library_Material[anyLayer]
    
        if N_Layers_In_Parallel > 0:
            List_R=[]  
            for anyLayer in Layers_In_Parallel:
                R_Parallel=Tot_R_Series+Library_Material[anyLayer]
                List_R.append(R_Parallel)
            
            #Calculate  the total global heat transfer coefficient and the total thermal resistance
            Tot_U=0
            for i in range (0,N_Layers_In_Parallel):
                Tot_U=Tot_U+round(Ratio_Insulation[i]/List_R[i],4)
            Tot_R=round(1/Tot_U,4)
        else:
            Tot_U=round(1/Tot_R_Series,4)
            Tot_R=round(1/Tot_U,4)
    else:
        Tot_U=round(Global_Heat_Transfer_Coeff,4)
        Tot_R=round(1/Tot_U,4)       
     
    Heat_Exchange=round(Tot_U*Delta_T*Area,4)
    
    Results = {"GLOBAL HEAT TRANSFER COEFFICIENT":{"N.VALUE":Tot_U,"U.MEASURE":"[W/m2C]"}, 
                "TOTAL THERMAL RESISTANCE":{"N.VALUE":Tot_R,"U.MEASURE":"[m2C/W]"},
                "HEAT EXCHANGE":{"N.VALUE":Heat_Exchange,"U.MEASURE":"[W]"}}
    return Results
