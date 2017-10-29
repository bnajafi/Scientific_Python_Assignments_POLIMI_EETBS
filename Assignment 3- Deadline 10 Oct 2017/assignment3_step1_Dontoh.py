# -*- coding: utf-8 -*-
#HEAT TRANSFER LOSS 
#Dicfining the unit thermal resistance of the various components used in buildings 
Material_Library = {"Outside_surface_Summer":0.044, "Outside_surface_Winter":0.030,"Inside_surface": 0.12,
                "Insulation_Glass_Fiber_90mm":2.45, "WoodStud_90mm":0.63, "WoodFiberboard": 0.23, 
                "Stucco_25":0.037, "WoodBevel_13x200": 0.14, "Gypsum_13mm":0.079}

#Calculating the resistance when length is different from table
length_GlassFiber = 90

if length_GlassFiber == 25:
    RvalueGF = 0.7
else:
    RvalueGF = float(length_GlassFiber)*(0.7/25)
    
print RvalueGF

print "To calculate the heat flux loss with the Overall heat transfer coefficient/n"
#We start calculations defining each list
AirOnTwoSides = ["Outside_surface_Winter", "Inside_surface"] #List where both inside and outside of wall is defined. 
Layers_Wall_Studs = ["WoodBevel_13x200","WoodFiberboard","WoodStud_90mm","Gypsum_13mm"] #A list considering just Woodstud
Layers_Wall_Fiber = ["WoodBevel_13x200","WoodFiberboard","Insulation_Glass_Fiber_90mm","Gypsum_13mm"] #Considering the layers in series including Glass fiber insulation

#FOR WOOD STUD
Layers_25 = AirOnTwoSides + Layers_Wall_Studs # The sum of all layers.

#Loop for wood studs calculation
Rtot_Stud = 0 
RValues_Stud = []

for anyLayerStud in Layers_25:
    RValueStud = Material_Library[anyLayerStud]
    Rtot_Stud = Rtot_Stud + RValueStud
    RValues_Stud.append(RValueStud)
print RValues_Stud #List showing all the specific resistances that are used.
print "The value of R assuming a wall with stud is " + str(Rtot_Stud)+ " m2 °C/W"
U_Stud = 1/(Rtot_Stud) #Overall heat transfer coefficient, which is the inverse of the specific resistance.
print "The overall heat transfer for a wall with Stud is "+str(U_Stud)+ "W/m2 °C"
print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

#FOR GLASS FIBER
Layers_75 = AirOnTwoSides + Layers_Wall_Fiber #For this case, 

#Loop for Glass Fiber insulation calculation
Rtot_Fiber = 0
RValues_Fiber = []

for anyLayerFiber in Layers_75:
    RValueFiber = Material_Library[anyLayerFiber]
    Rtot_Fiber = Rtot_Fiber + RValueFiber
    RValues_Fiber.append(RValueFiber)
print RValues_Fiber
print "The value of R assuming a wall with 100% Fiber is " + str(Rtot_Fiber)+" m2 °C/W"
U_Fiber = 1/(Rtot_Fiber)
print "The overall heat transfer for a wall with Fiber is "+str(U_Fiber)+ "W/m2 °C"
print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*/n"

#For the total calculation of the resistance, 25% of Studs and 75% of Glass fiber are considered.
A_Stud = 0.25
A_GF = 0.75

U_total = (A_GF)*(U_Fiber) + (A_Stud)*(U_Stud)
R_Total = 1/U_total

print "The Overall heat transfer coefficient (U) is " +str(U_total)+ "W/°C"
print "The TOTAL RESISTANCE of the wall is "+str(R_Total)+" °C/W" 
print "--**--**--**--**--**--**--**--**--**--**--**--*--**--"
print "*****************************************************"

#Calculation of heat loss of a house in Las Vegas, Nevada
T_inside = 22 #Temperature inside the building
T_outside = -2 #Temperature outside, depending on the season - Winter: for this case
Q =U_total*(T_inside - T_outside)

Perimeter = 50
Wall_height = 2.5
Area_wall = 0.8*Perimeter*Wall_height

Qtot = Area_wall*Q

print "THE TOTAL HEAT LOSS throught the house is "+str(Qtot)+"W.\n"