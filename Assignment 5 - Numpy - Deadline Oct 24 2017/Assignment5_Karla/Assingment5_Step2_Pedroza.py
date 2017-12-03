# -*- coding: utf-8 -*-
#ASSINGMENT NO.3

import numpy as np

materials_names= np.array(["Outside_surface_Summer","Outside_surface_Winter","Inside_surface",
                "Insulation_Glass_Fiber_90mm", "WoodStud_90mm", "WoodFiberboard", 
                "Stucco_25", "WoodBevel_13x200", "Gypsum_13mm"]) 
materials_Rvalues =np.array([0.044, 0.030, 0.12, 2.45, 0.63,  0.23, 0.037, 0.14, 0.079])


Layers_Wall_Studs = np.array(["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","WoodStud_90mm","Gypsum_13mm","Inside_surface"]) # this is just a very simple example wall
Layers_Wall_Fiber = np.array(["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","Insulation_Glass_Fiber_90mm","Gypsum_13mm","Inside_surface"])


#Calculation of R assuming the wall with STUDS

RValue_Wall_Studs = np.zeros(Layers_Wall_Studs.size) # this creates a vector of zeros which has the same length as that of layers_myWall

for anyLayerStud in Layers_Wall_Studs:
    RValue_Wall_Studs[Layers_Wall_Studs==anyLayerStud] = materials_Rvalues[materials_names==anyLayerStud]
    Rtot_Wall_Studs = RValue_Wall_Studs.sum()
print "The total resistance for a wall with Studs is "+str(Rtot_Wall_Studs)+" m2 °C/W"
U_Stud = 1/(Rtot_Wall_Studs) #Overall heat transfer coefficient, which is the inverse of the specific resistance.
print "The overall heat transfer for a wall with Stud is "+str(U_Stud)+ " W/m2 °C"
print "____________________________________________"


#Calculation of R assuming the wall with FIBER

RValue_Wall_Fiber = np.zeros(Layers_Wall_Fiber.size) # this creates a vector of zeros which has the same length as that of layers_myWall

for anyLayerFiber in Layers_Wall_Fiber:
    RValue_Wall_Fiber[Layers_Wall_Fiber==anyLayerFiber] = materials_Rvalues[materials_names==anyLayerFiber]
    Rtot_Wall_Fiber = RValue_Wall_Fiber.sum()
print "The overall heat transfer for a wall with Fiber is "+str(Rtot_Wall_Fiber)+" m2 °C/W"
U_Fiber = 1/(Rtot_Wall_Fiber)
print "The overall heat transfer for a wall with Fiber is "+str(U_Fiber)+ " W/m2 °C"
print "____________________________________________\n"



#For the total calculation of the resistance, 25% of Studs and 75% of Glass fiber are considered.
A_Stud = 0.25
A_GF = 0.75

U_total = (A_GF)*(U_Fiber) + (A_Stud)*(U_Stud)
R_Total = 1/U_total

print "The Overall heat transfer coefficient (U) is " +str(U_total)+ " W/°C"
print "The TOTAL RESISTANCE of the wall is "+str(R_Total)+" °C/W" 
print "____________________________________________"

#Calculation of heat loss of a house in Las Vegas, Nevada
T_inside = 22 #Temperature inside the building
T_outside = -2 #Temperature outside, depending on the season - Winter: for this case
Q =U_total*(T_inside - T_outside)

Perimeter = 50
Wall_height = 2.5
Area_wall = 0.8*Perimeter*Wall_height

Qtot = Area_wall*Q

print "THE TOTAL HEAT LOSS throught the house is "+str(Qtot)+" W.\n"
