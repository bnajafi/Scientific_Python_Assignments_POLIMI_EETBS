# -*- coding: utf-8 -*-
# Assignment5 step2

import numpy as np

Material_library = np.array(["stucco_25mm","face_brick_100mm","common_brick_100mm","wood_bevel_lapped_siding_13mmx200mm",
     "plaster_or_gypsum_board_13mm","inside_surface","outside_surface_summer","outside_surface_winter","wood_stud_nominal",
     "asphalt_shingle_roofing","cement_mortar_13mm","wood_fiberboard_13mm","glass_fiber_insulation_90mm","wood_25mm"])
materials_Rvalue = np.array([0.023,0.075,0.12,0.14,0.079,0.12,0.044,0.03,0.63,0.077,0.018,0.23,2.45,0.22])


layers_series = np.array(["wood_bevel_lapped_siding_13mmx200mm","wood_fiberboard_13mm","plaster_or_gypsum_board_13mm"])
layers_parallel = np.array(["wood_stud_nominal","glass_fiber_insulation_90mm"])
air_on_two_sides = np.array(["inside_surface","outside_surface_winter"])
IR = 0.75

# convective resistances

Rvalue_air = np.zeros(air_on_two_sides.size)
for anylayer in air_on_two_sides:
    Rvalue_air[air_on_two_sides==anylayer] = materials_Rvalue[Material_library==anylayer]
Rtot_air = Rvalue_air.sum()

# layers in series

Rvalue_series = np.zeros(layers_series.size)
for anylayer in layers_series:
    Rvalue_series[layers_series==anylayer] = materials_Rvalue[Material_library==anylayer]
Rtot_series = Rvalue_series.sum()

# layers in parallel

Rvalue_parallel = np.zeros(layers_parallel.size)
for anylayer in layers_parallel:
    Rvalue_parallel[layers_parallel==anylayer] = materials_Rvalue[Material_library==anylayer]
Utot_wall_studs = float((Rtot_air + Rtot_series + Rvalue_parallel[layers_parallel=="wood_stud_nominal"])**-1)
Utot_wall_insu = float((Rtot_air + Rtot_series + Rvalue_parallel[layers_parallel=="glass_fiber_insulation_90mm"])**-1)


U_TOT = Utot_wall_studs*(1-IR) + Utot_wall_insu*IR
print 'The global heat transfer coefficient is '+str(U_TOT)+' W/m2*C°'
               

