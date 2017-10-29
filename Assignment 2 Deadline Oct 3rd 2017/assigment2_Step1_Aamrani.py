# -*- coding: utf-8 -*-
#Rachid Aamrani



# Resistence Data

R_foam = [0.026,0.03,0.25]
R_plaster = [0.22,0.02,0.25]
R_plaster2 = [0.22,0.16,0.015]
R_brick = [0.72,0.16,0.22]
R_conv_int = [10,0.25]
R_conv_ext = [25,0.25]
 
# conductive resistances

R_tot_cond = 0
first_list = [R_foam,R_plaster,R_plaster]
for anyres in first_list:
    k_anyres = anyres[0]
    L_anyres = anyres[1]
    A_anyres = anyres[2]
    R_value_cond = L_anyres/(A_anyres*k_anyres)
    R_tot_cond = R_tot_cond+R_value_cond
print 'The total conductive resistance in serie is '+str(R_tot_cond)+(' °C/W')
 
# parallel resistence

R_parallel = 0
second_list = [R_plaster2,R_brick,R_plaster2]
for anyres in second_list:
    k_anyres = anyres[0]
    L_anyres = anyres[1]
    A_anyres = anyres[2]
    R_value_paral = (L_anyres/(A_anyres*k_anyres))**-1
    R_parallel = R_parallel+R_value_paral
print 'The parallel resistence is '+str((R_parallel)**-1)+(' °C/W')
 
#  convective resistances

R_tot_conv = 0
third_list = [R_conv_int,R_conv_ext]
for anyres in third_list:
    h_conv_anyres = anyres[0]
    A_anyres = anyres[1]
    R_conv = (h_conv_anyres*A_anyres)**-1
    R_tot_conv = R_tot_conv+R_conv
print "The total convective resistance is "+str(R_tot_conv)+" °C/W"
 
R_tot_wall = R_tot_conv+(R_parallel)**-1+R_tot_cond
print "The total thermal resistance of the wall is "+str(R_tot_wall)+" °C/W"