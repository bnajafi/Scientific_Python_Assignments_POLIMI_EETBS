# -*- coding: utf-8 -*-
# Assignement 2 step2 

# list of resistances 
R_foam = {'conductivity':0.026,'length':0.03,'area':0.25}
R_plaster = {'conductivity':0.22,'length':0.02,'area':0.25}
R_plaster2 = {'conductivity':0.22,'length':0.16,'area':0.015}
R_brick = {'conductivity':0.72,'length':0.16,'area':0.22}
R_conv_int = {'convective coefficient':10,'area':0.25}
R_conv_ext = {'convective coefficient':25,'area':0.25}

# for conductive resistances
R_tot_cond = 0
first_list = [R_foam,R_plaster,R_plaster]
for anyres in first_list:
    k_anyres = anyres['conductivity']
    L_anyres = anyres['length']
    A_anyres = anyres['area']
    R_value_cond = L_anyres/(A_anyres*k_anyres)
    R_tot_cond = R_tot_cond+R_value_cond
print 'The total conductive resistance in serie is '+str(R_tot_cond)+(' °C/W')

# for the parallel
R_parallel = 0
second_list = [R_plaster2,R_brick,R_plaster2]
for anyres in second_list:
    k_anyres = anyres['conductivity']
    L_anyres = anyres['length']
    A_anyres = anyres['area']
    R_value_paral = (L_anyres/(A_anyres*k_anyres))**-1
    R_parallel = R_parallel+R_value_paral
print 'The total value for the parallel of resistances is '+str((R_parallel)**-1)+(' °C/W')

# for convective resistances
R_tot_conv = 0
third_list = [R_conv_int,R_conv_ext]
for anyres in third_list:
    h_conv_anyres = anyres['convective coefficient']
    A_anyres = anyres['area']
    R_conv = (h_conv_anyres*A_anyres)**-1
    R_tot_conv = R_tot_conv+R_conv
print "The total convective resistance is "+str(R_tot_conv)+" °C/W" 

R_tot_wall = R_tot_conv+(R_parallel)**-1+R_tot_cond
print "The total thermal resistance of the wall is "+str(R_tot_wall)+" °C/W" 