import numpy as np

resistances_names = np.array(["R_in","R_foam","R_plaster1_series","R_plaster1_parallel","R_brick","R_plaster2_parallel","R_plaster2_series","R_out"])
resistances_types = np.array(["conv","cond_series","cond_series","cond_parallel","cond_parallel","cond_parallel","cond_series","conv"])
resistances_h = np.array([10,None,None,None,None,None,None,25])
resistances_k = np.array([None,0.026,0.22,0.22,0.72,0.22,0.22,None])
resistances_L = np.array([None,0.03,0.02,0.16,0.16,0.16,0.02,None])
resistances_A = np.array([0.25,0.25,0.25,0.015,0.22,0.015,0.25,0.25])
Resistances_RValues = np.array(np.zeros(8)) #array where all the values are 0

condition_conv =(resistances_types == "conv")
RValues = 1.0/(resistances_h[condition_conv]*resistances_A[condition_conv])
Resistances_RValues[condition_conv] = RValues
R_total = Resistances_RValues[condition_conv].sum()

condition_cond_series =(resistances_types == "cond_series")
RValues = resistances_L[(resistances_types == "cond_series")]/(resistances_k[(resistances_types == "cond_series")]*resistances_A[(resistances_types == "cond_series")])
Resistances_RValues[condition_cond_series] = RValues
R_total = Resistances_RValues[condition_cond_series].sum()

condition_cond_parallel = (resistances_types == "cond_parallel")
RValues = resistances_L[(resistances_types == "cond_parallel")]/(resistances_k[(resistances_types == "cond_parallel")]*resistances_A[(resistances_types == "cond_parallel")])
Resistances_RValues[condition_cond_parallel] = (RValues)**(-1)
R_total = Resistances_RValues[condition_cond_parallel].sum()

R_tot = Resistances_RValues[condition_conv].sum()+Resistances_RValues[condition_cond_series].sum()+Resistances_RValues[condition_cond_parallel].sum()

print "the total resistance is " + str(R_tot) + " deg C*m^2/W"