import os
os.chdir("C:\Users\Cremona\Documents\Nuova cartella")
import wallCalculations_Cremona as w_C
w_s = ["common_brick_100mm","wood_bevel_lapped_siding_13mmx200mm","plaster_or_gypsum_board_13mm","wood_fiberboard_13mm","wood_stud_nominal"]
w_i = ["common_brick_100mm","wood_bevel_lapped_siding_13mmx200mm","plaster_or_gypsum_board_13mm","wood_fiberboard_13mm","glass_fiber_insulation_25mm"]
IF = 0.70
U_walls = w_C.wallCalc_withParallel(w_s,w_i,IF)
Door = ["wood_25mm"]
U_door = w_C.wallCalc_onlyInSeries(Door)
Roof = ["asphalt_shingle_roofing","wood_fiberboard_13mm","common_brick_100mm"]
U_roof = w_C.wallCalc_onlyInSeries(Roof)

Del_T_winter = 24.8
area_walls = 105.8
area_door = 2.2
area_roof = 200
list_U_opaque = {"U_walls":U_walls,"U_door":U_door,"U_roof":U_roof}
list_area_opaque = [area_walls,area_door,area_roof]
Q_tot = 0
i = 0


for anyU in list_U_opaque:
    heat_factor = Del_T_winter*list_U_opaque[anyU]
    Q_heat = heat_factor*list_area_opaque[i]
    Q_tot = Q_tot + Q_heat
    i = i+1
    print "The heating load for this surface is "+str(Q_heat)
print "The total heating load is "+str(Q_tot)
    