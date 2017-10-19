# -*- coding: utf-8 -*-
import os 
os.chdir("C:/Users/stefy/Desktop/POLIMI/I ANNO/1 Semestre/Buildings/ASSIGNMENTS")

import wallCalculations_Patrignani as CALC

#walls
ListOfLayersInSeries=["gypsum_13mm", "common_brick", "wood_fiberboard", "wood_bevel","inside_surface","outside_surface"]
ListOfLayersInParallel=["glass_fiber", "wood_stud"]
AreaRatioInsulation = 0.70

U_wall = CALC.wallCalc_withParallel(ListOfLayersInSeries,ListOfLayersInParallel,AreaRatioInsulation)

#door
ListOfLayers = ["wood_25mm", "inside_surface","outside_surface"]

U_door = CALC.wallCalc_onlyInSeries(ListOfLayers)

#roof
ListOfLayers = ["gypsum_13mm", "glass_fiber", "wood_bevel","inside_surface","outside_surface"]
U_roof = CALC.wallCalc_onlyInSeries(ListOfLayers)

#Temperature difference
deltaT_heating = 20-(-4.8)

# heating factor [W/m2]
HF_wall = U_wall * deltaT_heating
HF_door = U_door * deltaT_heating
HF_roof = U_roof * deltaT_heating

#Areas [m2]
A_ceiling = 20*10
A_wall = 2.4*(2*(20+10))
A_door = 1*2.2

#Heating Loads  [W]
HL_wall = HF_wall * A_wall
HL_door = HF_door * A_door
HL_ceiling = HF_roof * A_ceiling