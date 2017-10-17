# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.3 (Step2) Date: 08/10/2017
#Example 1

#Use of FUNCTION to calculate the overall unit thermal resistance (R-value) and the overall heat transfer coefficient (U)
   
#Function
def wall_calc(Layers_in_series,Layers_in_parallel,fraction):
    #I define a dictionary with the unit thermal resistance (R-value) of common components used in buildings:
    Material_Library = {"Outside_surface_Summer":0.044, "Outside_Surface_Winter":0.030,"Inside_Surface": 0.12,
    "Insulation_Glass_Fiber_25mm":2.45, "WoodStud_90mm":0.63, "WoodFiberboard13mm": 0.23,"Stucco_25mm":0.037, "WoodBevel_13*200": 0.14, "Gypsum_13mm":0.079}
    R_s = 0
    Rvalue_layers=[]
    for anyLayer in Layers_in_series:
         Rvalue_layer_s=Material_Library[anyLayer]
         R_s=R_s+Rvalue_layer_s
         Rvalue_layers.append(Rvalue_layer_s)
         print "This layer is: " +anyLayer
         print "The value of R for this layer in series is :" +str(Rvalue_layer_s)
         print "****************************"
    print "The total R value in series is: " +str(R_s)+ "m2°C/W"
    
    R_p = 1
    for anyLayer in Layers_in_parallel:
         Rvalue_layer_p=Material_Library[anyLayer]
         R_p = 1/((1/R_p) + (1/Rvalue_layer_p))
         Rvalue_layers.append(Rvalue_layer_p)
         print "This layer is: " +anyLayer
         print "The value of R for this layer in parallel is :" +str(Rvalue_layer_p)
         print "****************************"
    print "The total R value in parallel is: " +str(R_p)+ "m2°C/W"
    #Now i calculate the R-value and U of the wall with glass fiber and with wood studs:
    GF=["Insulation_Glass_Fiber_25mm"]
    Wall_GF= GF+Layers_in_series
    R_GF = 0
    for anyLayer in Wall_GF:
        RValue_layer = Material_Library [anyLayer]
        R_GF = R_GF + RValue_layer
    print "The resistance of the wall with glass fiber is: "+str(R_GF)+ "m2°C/W"
     
    WS = ["WoodStud_90mm"]
    Wall_WS = WS+Layers_in_series
    R_WS=0
    for anyLayer in Wall_WS:
        RValue_layer = Material_Library [anyLayer]
        R_WS = R_WS + RValue_layer
    print "The resistance of the wall with wood studs is: "+str(R_WS)+ "m2°C/W"
    #The overall heat transfer coefficients are:
    U_GF = (1/R_GF)
    print "The overall heat transfer coefficient considering glass fiber is: "+str(U_GF)+ "W/m2°C"
    U_WS = (1/R_WS)
    print "The overall heat transfer coefficient considering wood studs is: "+str(U_WS)+ "W/m2°C"
    
    #So the total heat transfer U and R value are:
    U_overall = fraction*(U_GF) + (1-fraction)*(U_WS)
    R_overall = 1/U_overall
 
    print "The overall heat transfer coefficient is: " +str(U_overall)+ "W/°C"
    print "The total resistance of the wall is: "+str(R_overall)+" °C/W"
    results = {"RValue of all layers":Rvalue_layers, "R tot":R_overall, "U tot":U_overall}
    return results
    
Layers_in_series = ["Inside_Surface","Outside_Surface_Winter","Gypsum_13mm","WoodFiberboard13mm","WoodBevel_13*200"]
Layers_in_parallel = ["WoodStud_90mm","Insulation_Glass_Fiber_25mm"]
fraction=float(0.75)    

Result=wall_calc(Layers_in_series,Layers_in_parallel,fraction)      
    
    
    

    