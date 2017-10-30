# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.4 (Step1) Date: 16/10/2017
#RLF example

#I define two functions: the first calculates the value of the overall heat transfer coeffcient of a wall (Layers in series) 
#and the second calculates the overall heat transfer coefficient considering Layers in series, in parallel (Wood studs and
#Glass fiber insulation) and the ratio of the area respect the total area of the wall
   
#Function 1 (wall calc series):
def wallCalc_onlyInSeries(Layers_in_series):
    
    Material_Library ={"AsphaltRoofing":0.077,"Wood_50mm":0.44,"slag_13mm":0.067,"AcousticTile":0.32,"BuildingPaper":0.011,
    "gypsumBoard":0.079,"CommonBrik":0.12,
    "FaceBrik_100mm": 0.075,"Outside_surface_Summer":0.044, "Outside_Surface_Winter":0.030,"Inside_Surface": 0.12,
    "Insulation_Glass_Fiber":2.52, "WoodStud_90mm":0.63, "WoodFiberboard13mm": 0.23,"Stucco_25mm":0.037, "WoodBevel": 0.14}
    Layers_air=["Inside_Surface","Outside_Surface_Winter"]
    Layers_in_series=Layers_in_series+Layers_air 
    R_tot=0
    for  anyLayer in Layers_in_series:
         Material=Material_Library[anyLayer]
         R_tot=R_tot+Material
         print "This layer is: " +anyLayer
         print "****************************"
    U_tot=(1/R_tot)    
    print "The total R value of the wall is: " +str(R_tot)+ "m2°C/W"
    print "The overall heat transfer coefficient is:" +str(U_tot)+ "W/m2°C"
    return U_tot
    
#Function 2 (Calculates the U of the wall)
def wallCalc_withParallel(Layers_in_series,Layers_in_parallel,fraction): 
    #I define a dictionary with the unit thermal resistance (R-value) of common components used in buildings:
    Material_Library={"AsphaltRoofing":0.077,"Wood_50mm":0.44,"slag_13mm":0.067,"AcousticTile":0.32,"BuildingPaper":0.011,
    "gypsumBoard":0.079,"CommonBrik":0.12,
    "FaceBrik_100mm": 0.075,"Outside_surface_Summer":0.044, "Outside_Surface_Winter":0.030,"Inside_Surface": 0.12,
    "Insulation_Glass_Fiber":2.52, "WoodStud_90mm":0.63, "WoodFiberboard13mm": 0.23,"Stucco_25mm":0.037, "WoodBevel": 0.14}
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
    GF=["Insulation_Glass_Fiber"]
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
    return U_overall         

    
          
    
    
    

    