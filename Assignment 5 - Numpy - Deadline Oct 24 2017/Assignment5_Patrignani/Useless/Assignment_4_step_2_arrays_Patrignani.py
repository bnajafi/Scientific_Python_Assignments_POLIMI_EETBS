import numpy as np

import os 
os.chdir("C:/Users/stefy/Desktop/POLIMI/I ANNO/1 Semestre/Buildings/ASSIGNMENTS/Assignment 5")

import Assignment_4_step_1_arrays_Patrignani as CALC

#walls
layers = np.array(["gypsum_13mm", "common_brick", "glass_fiber_90mm", "wood_stud", "wood_fiberboard",  "wood_bevel", "inside_surface", "otside_surface"])
resistances = np.array([0.079, 0.12, 2.52, 0.63, 0.23, 0.14, 0.12, 0.03])
types = np.array(["series","series","parallel","parallel","series","series","series","series"])
AreaRatioInsulation = 0.70

U_wall = CALC.wallCalc_withParallel(layers, resistances, types, AreaRatioInsulation)


#door
layers_opaque = np.array([ "wood_25mm", "inside_surface","outside_surface"])
resistances_opaque = np.array([0.44, 0.12, 0.03])

U_door = CALC.wallCalc_onlyInSeries(resistances_opaque)

#roof
layers_opaque = np.array([ "gypsum_13mm", "glass_fiber", "wood_bevel","inside_surface","outside_surface"])
resistances_opaque = np.array([0.079, 2.52, 0.63, 0.12, 0.03])

U_roof = CALC.wallCalc_onlyInSeries(resistances_opaque)

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