# -*- coding: utf-8 -*-
import os
os.chdir("C:\Users\Karla\OneDrive\SECOND SEMESTER - Sept 17\Buildings\Homework\Assignment4")
import WallCalculations_Pedroza as WC

#EXERCISE

#Input data:
Length_building = 20
Width_building = 10
H_building = 2.4

Windows = {"East":8, "South":4, "West":8}
L_Win = 1.8

W_Door = 2.2
L_Door = 1

T_Winter = -4.8
T_Summer = 31.9
DR = 11.9 
Walls_OF = {"OFt":1,"OFb":8.2,"OFr":-0.36}
Door_OF = {"OFt":1,"OFb":8.2,"OFr":-0.36}
Ceiling_OF = {"OFt":0.62,"OFb":14.3*0.85-4.5,"OFr":-0.19}
T_confort_Summer = 24
T_confort_Winter = 20
U_ceiling = 0.25


#CALCULATIONS

#OVERALL HEAT TRANSFER COEFFICIENT CALCULATION

#For Walls: 

Layers_Wall_Studs_Winter = ["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","CommonBrick_100mm","WoodStud_90mm","Gypsum_13mm","Inside_surface"] #A list considering just Woodstud
Layers_Wall_Fiber_Winter = ["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","CommonBrick_100mm","Insulation_Glass_Fiber_90mm","Gypsum_13mm","Inside_surface"] #Considering the layers in series including Glass fiber insulation
A_GlassFiber = 0.70

Layers_Wall_Studs_Summer = ["Outside_surface_Summer","WoodBevel_13x200","WoodFiberboard","CommonBrick_100mm","WoodStud_90mm","Gypsum_13mm","Inside_surface"] #A list considering just Woodstud
Layers_Wall_Fiber_Summer = ["Outside_surface_Summer","WoodBevel_13x200","WoodFiberboard","CommonBrick_100mm","Insulation_Glass_Fiber_90mm","Gypsum_13mm","Inside_surface"] #Considering the layers in series including Glass fiber insulation
A_GlassFiber = 0.70

UWall_Winter = WC.wallCalc_withParallel(Layers_Wall_Studs_Winter,Layers_Wall_Fiber_Winter,A_GlassFiber)#FUnction
UWall_Summer = WC.wallCalc_withParallel(Layers_Wall_Studs_Summer,Layers_Wall_Fiber_Summer,A_GlassFiber)#FUnction


#For Doors:
Layers_Door_Winter = ["Outside_surface_Winter","Wood_50mm","Inside_surface"] #Wood Door 
Layers_Door_Summer = ["Outside_surface_Summer","Wood_50mm","Inside_surface"]

UDoor_Winter = WC.wallCalc_onlyInSeries(Layers_Door_Winter)#Function
UDoor_Summer = WC.wallCalc_onlyInSeries(Layers_Door_Summer)#Function


#AREA CALCULATIONS

Area_ceiling = Length_building*Width_building
Area_walls = (Length_building+ Width_building)*2*H_building

#Windows
def A_Windows(W_Win):
    Area_Win = W_Win
    Atot_Win = 0
        
    for anyWindow in Area_Win:
        W_Win = Windows[anyWindow]
        Atot_Win = Atot_Win + 1.8*W_Win
    return Atot_Win

Area_Windows = A_Windows(Windows)
Area_door = W_Door*L_Door

Area_net_walls = Area_walls - Area_Windows - Area_door


#HEATING CALCULATIONS

Q_heating_Walls = WC.Q_heat(T_Winter, Area_net_walls, UWall_Winter["U_Total"])
Q_heating_Ceiling = WC.Q_heat(T_Winter, Area_ceiling, U_ceiling)
Q_heating_Door = WC.Q_heat(T_Winter, Area_door, UDoor_Winter)
Qtot_heating = Q_heating_Walls["Q_heating"]+Q_heating_Ceiling["Q_heating"]+Q_heating_Door["Q_heating"]

print "The heat load for the walls is ",Q_heating_Walls
print "The heat load for the ceiling is ",Q_heating_Ceiling
print "The heat load for the door is ",Q_heating_Door 
print "___________________________________________________________________________\n"
print "The total heat that is needed to warm the building is "+str(Qtot_heating)+" W"
