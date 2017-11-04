# -*- coding: utf-8 -*-
# Defining Functions_Example 1
#*****************************

#Dictionary containing thermal resistances of common components used in buildings
Material_Library = {"OutsideSurface_Summer":0.044, "OutsideSurface_Winter":0.030,"InsideSurface": 0.12,
                "InsulationFiberGlass_90mm":2.45, "WoodStud_90mm":0.63, "WoodFiberboard": 0.23, 
                "Stucco_25mm":0.037, "WoodBevel_13x200": 0.14, "Gypsum_13mm":0.079}


length_GlassFiber = 90  # Resistance when length is different

if length_GlassFiber == 25:
    RvalueGlassFiber = 0.7
else:
    RvalueGlassFiber = float(length_GlassFiber)*(0.7/25)
    
print RvalueGlassFiber

# Calculation of the heat flux loss
AirOnTwoSides = ["OutsideSurface_Winter", "InsideSurface"] # List containing inside and outside of wall 
Layers_Wall_Studs = ["WoodFiberboard","WoodBevel_13x200","WoodStud_90mm","Gypsum_13mm"] # List for the Woodstud
Layers_Wall_Fiber = ["WoodBevel_13x200","WoodFiberboard","InsulationFiberGlass_90mm","Gypsum_13mm"] # List containing layers in series 


layers_wall_complete_25 = AirOnTwoSides + Layers_Wall_Studs # #For the wood stud

#Loop for wood studs calculation
Rtot_Stud = 0 
RValues_Stud = []

for anyLayer_Stud in layers_wall_complete_25:
    RValueStud = Material_Library[anyLayer_Stud]
    Rtot_Stud = Rtot_Stud + RValueStud
    RValues_Stud.append(RValueStud)
print RValues_Stud
print "The total Resistance of stud is "+str(Rtot_Stud) +" degC/W" 

U_of_Stud = 1/(Rtot_Stud) #Overall heat transfer coefficient
print "The overall heat transfer coefficient for the stud wall "+str(U_of_Stud)+ " W/m^2 degC"
print "***********************************************************************************"

#For The Glass Fiber:
layers_complete_Fiber = AirOnTwoSides + Layers_Wall_Fiber #For this case, 

Rtot_Fiber = 0
RValues_Fiber = []

for anyLayer_Fiber in layers_complete_Fiber:
    RValueFiber = Material_Library[anyLayer_Fiber]
    Rtot_Fiber = Rtot_Fiber + RValueFiber
    RValues_Fiber.append(RValueFiber)
print RValues_Fiber
print "For a wall with Fiber R value is " + str(Rtot_Fiber)+" degC/W"

U_of_Fiber = 1/(Rtot_Fiber)
print "The overall heat transfer coefficient for the wall with Fiber is "+str(U_of_Fiber)+ " W/m^2 degC"
print "**********************************************************************************************"

# Calculation of the Total resistance
A_Stud = 0.25
A_GlassFiber = 0.75

U_total = (A_GlassFiber)*(U_of_Fiber) + (A_Stud)*(U_of_Stud)

R_Total = 1/U_total # Total resistance
print "The Total Resistance of the wall is "+str(R_Total)+" degC/W"
print "The Overall heat transfer coefficient,U is " +str(U_total)+ " W/degC" 

# Determining Heat Loss
T_1 = 22 # internal Temperature of the building
T_0 = -2 # External Temperature, Winter mode for our case
Q =U_total*(T_1 - T_0)

Area_wall = 0.8*50*2.5 # Area of wall with height = 2.5 and Perimeter = 50
Qtot = Area_wall*Q
print "Total Heat Loss throught the buliding is "+str(Qtot/1000)+" kW"


