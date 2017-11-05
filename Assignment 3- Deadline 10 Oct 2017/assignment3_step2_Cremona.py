# -*- coding: utf-8 -*-
# Assignment 3 step2

Walls_Materials = {'gypsum_wallboard_13mm':0.079,'wood_bevel_lapped_siding':0.14,'wood_fiberboard_sheeting_13mm':0.23,'glass_fiber_insulation_90mm':2.45,
'wood_studs_38x90':0.63,'stucco_25mm':0.037,'common_brick':0.12,'inside_surface':0.12,'outside_surface_summer':0.044,'outside_surface_winter':0.03}


Res_tot1 = 0
Res_tot2 = 0

def Wall_calculation(W_1,W_2,I_R):
    Res_tot1 = 0
    Res_tot2 = 0
    Res_vals = []
    for anyMat in W_1:
        Res_val = Walls_Materials[anyMat]
        Res_vals.append(Res_vals)
        Res_tot1 = Res_tot1 + Res_val
    print 'The total resistance considering only the insulation is '+str(Res_tot1)+' m2/°C*K'
    print 'The global heat transfer coefficient considering only the insulation is '+str((Res_tot1)**-1)+' °C*K/m2'
    for anyMat in W_2:
        Res_val = Walls_Materials[anyMat]
        Res_vals.append(Res_vals)
        Res_tot2 = Res_tot2 + Res_val
    print 'The total resistance considering only wood studs is '+str(Res_tot2)+' m2/°C*K'
    print 'The global heat transfer coefficient considering only wood studs is '+str((Res_tot2)**-1)+' °C*K/m2'

    U_global = I_R*((Res_tot1)**-1)+(1-I_R)*((Res_tot2)**-1)
    Res_tot = (U_global)**-1
    results = {'Res_vals':Res_vals,'Res_tot':Res_tot,'U_global':U_global}
    return results




