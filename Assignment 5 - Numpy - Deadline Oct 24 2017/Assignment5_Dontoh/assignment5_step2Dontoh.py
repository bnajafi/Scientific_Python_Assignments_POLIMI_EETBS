#Using Numpy to define various Material

import numpy as np
materials_list= np.array(["OutsideSurface_Summer", "OutsideSurface_Winter","InsideSurface","InsulationFiberGlass_90mm",
                        "WoodStud_90mm","WoodFiberboard", "Stucco_25mm", "WoodBevel_13x200","Gypsum_13mm"]) 
materials_Rvalues =np.array([0.044,0.030,0.12,2.45,0.63,0.23,0.037,0.14,2.52])

layerNames_Stud = np.array(["OutsideSurface_Winter", "InsideSurface","WoodFiberboard","WoodBevel_13x200","WoodStud_90mm","Gypsum_13mm"])
RValue_myStud = np.zeros(layerNames_Stud.size)

for layerName in layerNames_Stud:
    RValue_myStud[layerNames_Stud==layerName] = materials_Rvalues[materials_list==layerName]

Rtot_stud = RValue_myStud.sum()
U_of_Stud = 1/(Rtot_stud) #Overall heat transfer coefficient

print "The total Resistance of the stud is "+str(Rtot_stud) +" degC/W" 
print "The overall heat transfer coefficient for the stud wall is "+str(U_of_Stud)+ " W/m^2 degC"
print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

#Calculation of glass fiber
layerNames_Fiber = np.array(["OutsideSurface_Winter", "InsideSurface","WoodBevel_13x200","WoodFiberboard",
                            "InsulationFiberGlass_90mm","Gypsum_13mm"]) # List containing layers in series 
RValue_myFiber = np.zeros(layerNames_Fiber.size)

for layerName in layerNames_Fiber:
    RValue_myFiber[layerNames_Fiber==layerName] = materials_Rvalues[materials_list==layerName]

Rtot_Fiber = RValue_myFiber.sum()
U_of_Fiber = 1/(Rtot_Fiber) #Overall heat transfer coefficient of wall with fiber

print "For the wall with Fiber,the R value is " + str(Rtot_Fiber)+" degC/W"

U_of_Fiber = 1/(Rtot_Fiber)
print "The overall heat transfer coefficient for the wall with Fiber is "+str(U_of_Fiber)+ " W/m^2 degC"
print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

# Calculation of the total resistance
A_Stud = 0.25
A_GlassFiber = 0.75

U_total = (A_GlassFiber)*(U_of_Fiber) + (A_Stud)*(U_of_Stud)

R_Total = 1/U_total # Total resistance
print "The Total Resistance of the wall is "+str(R_Total)+" degC/W"
print "And the Overall heat transfer coefficient,U is " +str(U_total)+ " W/degC" 

# Determining Heat Loss
T_1 = 22 # Temperature inside the building
T_0 = -2 # External temperature, winter season 
Q =U_total*(T_1 - T_0)

Area_wall = 0.8*50*2.5 # Area of wall (height = 2.5 and perimeter = 50)
Qtot = Area_wall*Q
print "The Total Heat Loss throught the buliding is "+str(Qtot/1000)+" kW"


