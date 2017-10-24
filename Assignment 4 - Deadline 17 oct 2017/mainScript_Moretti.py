# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 4 - RLF method, opaque surfaces (with funcion caller)

Giorgio Moretti (10433550)

"""
import wallCalculation_Moretti as walls

print "\n ********** HEAT TRANSFER COEFFICIENTS OF OPAQUE SURFACES **********"

##### U WALL #####

layers_wall_series = ["gypsumBoard_13mm","commonBrick_100mm","woodFiberboard_13mm","woodBevelLappedSiding_13x200mm"]
layers_wall_parallel = ["woodStud_90mm","glassFiberInsulation_25mm"]
percentage_ins = 0.70
season = "winter"

results_wall = walls.wallCalcSP(layers_wall_series, layers_wall_parallel, percentage_ins, season)
print "\n The global heat transfer coefficient of the wall is: U_WALL = " + str(results_wall["U"]) + " W/m^2°C"

##### U DOOR #####

layers_door_series = ["wood_25mm"]
season = "winter"

results_door = walls.wallCalcSeries(layers_door_series, season)
print "\n The global heat transfer coefficient of the door is: U_DOOR = " + str(results_door["U"]) + " W/m^2°C"

##### U CEILING #####
#layers_ceiling_series = ["wood_25mm","woodFiberboard_13mm","asphaltRoofing"]
#season = "winter"

#results_ceiling = walls.wallCalcSeries(layers_ceiling_series, season)
#print "\n The global heat transfer coefficient of the ceiling is: U_CEILING = " + str(results_ceiling["U"]) + " W/m^2°C"

U_ceiling = 0.25 
print "\n The global heat transfer coefficient of the ceiling is: U_CEILING = " + str(U_ceiling) + " W/m^2°C"

##### HEAT TRANSFER RATE #####
Tmin = -4.8
Tmax = 31.9
deltaT_heating = 20 - Tmin
deltaT_cooling = Tmax - 24

A_wall = 105.8 #[m^2]
A_door = 2.2 #[m^2]
A_ceiling = 200 #[m^2]

HF_wall = results_wall["U"]*deltaT_heating #[W/m^2]
HF_door = results_door["U"]*deltaT_heating #[W/m^2]
HF_ceiling = U_ceiling*deltaT_heating #[W/m^2]

QH_wall = round(HF_wall*A_wall,2) #[W]
QH_door = round(HF_door*A_door,2) #[W]
QH_ceiling = round(HF_ceiling*A_ceiling,2) #[W]
QH_tot = QH_wall + QH_door + QH_ceiling #[W]

print "\n ********** HEATING LOADS **********"
print "\n The heating load through the walls is: QH_WALL = " + str(QH_wall) + " W"
print "\n The heating load through the door is: QH_DOOR = " + str(QH_door) + " W"
print "\n The heating load through the ceiling is: QH_CEILING = " + str(QH_ceiling) + " W"
print "\n The total heating load through the opaque surfaces is: QH_TOT = " + str(QH_tot) + " W"