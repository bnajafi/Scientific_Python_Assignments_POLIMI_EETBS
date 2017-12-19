import numpy as np

f_ins = 0.75

resistances_names = np.array(["R_in","R_woodBevelLapperSiding","R_woodFiberBoard_13mm","R_gypsumWallBoard_13mm",
"R_glassFiberIsulation","R_woodStud_38mm*90mm","R_out"])
resistances_types = np.array(["conv","cond_series","cond_series","cond_series","cond_parallel","cond_parallel","conv"])
resistances_RValues = np.array([0.12,0.14,0.23,0.079,2.45,0.63,0.03])

condition_conv =(resistances_types == "conv")
RValues = resistances_RValues[condition_conv]
R_total = resistances_RValues[condition_conv].sum()

condition_cond_series = (resistances_types == "cond_series")
RValues = resistances_RValues[condition_cond_series]
R_total = resistances_RValues[condition_cond_series].sum()

R_tot = resistances_RValues[condition_conv].sum() + resistances_RValues[condition_cond_series].sum()

condition_cond_parallel = (resistances_types == "cond_parallel")
RValues = resistances_RValues[condition_cond_parallel]

U_tot_ins = 1.0/(R_tot + RValues[0])
U_tot_wood = 1.0/(R_tot + RValues[1])
U_overall = U_tot_ins*f_ins + (1-f_ins)*U_tot_wood

Rtotal = 1/U_overall

print "the heat transfer coefficient is " + str(U_overall) + " W/deg C*m^2"