# -*- coding: utf-8 -*-
# Assignment 3 step1

Walls_Materials = {'gypsum_wallboard_13mm':0.079,'wood_bevel_lapped_siding':0.14,'wood_fiberboard_sheeting_13mm':0.23,'glass_fiber_insulation_90mm':2.45,
'wood_studs_38x90':0.63,'stucco_25mm':0.037,'common_brick':0.12,'inside_surface':0.12,'outside_surface_summer':0.044,'outside_surface_winter':0.03}

# considering only the glass fiber insulation

example_wall1 = ['inside_surface','gypsum_wallboard_13mm','glass_fiber_insulation_90mm','wood_fiberboard_sheeting_13mm','wood_bevel_lapped_siding',
'outside_surface_winter']
Res_tot1 = 0

for anyMat in example_wall1:
    Res_val = Walls_Materials[anyMat]
    Res_tot1 = Res_tot1 + Res_val
    print 'The resistance of this part of the wall is '+str(Res_val)+' m2/°C*K'
print 'The total resistance is '+str(Res_tot1)+' m2/°C*K'
print 'The global heat transfer coefficient is '+str((Res_tot1)**-1)+' °C*K/m2'

# considering only the wood studs

example_wall2 = ['inside_surface','gypsum_wallboard_13mm','wood_studs_38x90','wood_fiberboard_sheeting_13mm','wood_bevel_lapped_siding',
'outside_surface_winter']
Res_tot2 = 0

for anyMat in example_wall2:
    Res_val = Walls_Materials[anyMat]
    Res_tot2 = Res_tot2 + Res_val
    print 'The resistance of this part of the wall is '+str(Res_val)+' m2/°C*K'
print 'The total resistance is '+str(Res_tot2)+' m2/°C*K'
print 'The global heat transfer coefficient is '+str((Res_tot2)**-1)+' °C*K/m2'
I_R = 0.75 # insulation ratio
U_global = I_R*((Res_tot1)**-1)+(1-I_R)*((Res_tot2)**-1)

print 'So the real global heat transfer coefficient is '+str(U_global)+' °C*K/m2'

# calculation of the total heat transfer
p = 50 #perimeter
h = 2.5 # height
GF = 0.20 #glazing fraction
T_ex = -2
T_in = 22

Area = (p*h)*(1-GF)
Heat_transfer = (U_global*Area*(T_in-T_ex))
print "The total Heat transfer through the wall is: "+str(Heat_transfer)+"[W]"
    