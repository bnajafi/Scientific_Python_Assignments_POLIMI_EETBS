# -*- coding: utf-8 -*-
# Assignment 6

import pandas as pnd

# considering only the layers in series

A = 0.25
resistances_series_name = ["Rin","Rfo","Rpl","Rpl","Rex"]
resistances_series_type = ["conv","cond","cond","cond","conv"]
resistances_series_l = [None,0.03,0.02,0.02,None]
resistances_series_k = [None,0.026,0.22,0.22,None]
resistances_series_h = [10.0,None,None,None,25.0]
resistances_series_values = [0,0,0,0,0]
resistances_series_list = [resistances_series_type,resistances_series_l,resistances_series_k,resistances_series_h,resistances_series_values]
RESISTANCES_series = pnd.DataFrame(resistances_series_list,index=['type|','thickness|','conductivity|','conv_coeff|','Rvalue|'], columns=resistances_series_name)

RESISTANCES_series.loc["Rvalue|"][RESISTANCES_series.loc["type|"]=="conv"] = 1.0/RESISTANCES_series.loc['conv_coeff|'][RESISTANCES_series.loc["type|"]=="conv"]*(1.0/A)
RESISTANCES_series.loc["Rvalue|"][RESISTANCES_series.loc["type|"]=="cond"] = (RESISTANCES_series.loc['thickness|'][RESISTANCES_series.loc["type|"]=="cond"]/RESISTANCES_series.loc['conductivity|'][RESISTANCES_series.loc["type|"]=="cond"])*(1.0/A)
Rtot_series = RESISTANCES_series.loc["Rvalue|"].sum()

# considering the parallel

resistances_paral_name = ["Rpl","Rbr","Rpl"]
resistances_paral_type = ["cond","cond","cond"]
resistances_paral_l = [0.16,0.16,0.16]
resistances_paral_k = [0.22,0.72,0.22]
areas = [0.015,0.22,0.015]
resistances_paral_values = [0,0,0]
resistances_paral_list = [resistances_paral_type,resistances_paral_l,resistances_paral_k,areas,resistances_paral_values]
RESISTANCES_parallel = pnd.DataFrame(resistances_paral_list, index=['type|','thickness|','conductivity|','areas|','Rvalue|'], columns=resistances_paral_name)

RESISTANCES_parallel.loc["Rvalue|"] = RESISTANCES_parallel.loc['thickness|']/(RESISTANCES_parallel.loc['conductivity|']*RESISTANCES_parallel.loc['areas|'])
Rtot_parallel = 1.0/((RESISTANCES_parallel.loc["Rvalue|"]**-1).sum())

R_TOT = Rtot_series + Rtot_parallel
print 'The total resistance of the wall is '+str(R_TOT)+' °C/W'