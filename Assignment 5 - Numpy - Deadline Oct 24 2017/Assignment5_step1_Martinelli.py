import numpy as np

#horizontal and vertical are inteded as seen in figure
H = 3.0
L = 5.0 #wall dimensions

Tin = 20.0
Tout = -10.0 #temperatures
A_S = 0.25

Names = np.array(["Int","Foam","Plaster","Plaster","Out"])
Types = np.array(["conv","cond","cond","cond","conv"])
h_res = np.array([10,None,None,None,25])
k_res = np.array([None,0.026,0.22,0.22,None])
L_res = np.array([None,0.03,0.02,0.02,None])
RValues = np.array(np.zeros(5))
RValues[Types=="cond"] = L_res[Types=="cond"]/(k_res[Types=="cond"]*A_S)
RValues[Types=="conv"] = 1.0/(h_res[Types=="conv"]*A_S)
Rtot_series = RValues.sum()

Names_par = np.array(["Plaster","Brick","Plaster"])
k_res_par = np.array([0.22,0.72,0.22])
L_res_par = np.array([0.16,0.16,0.16])
A_res_par = np.array([0.015,0.22,0.015])
RValues_par = np.array(np.zeros(3))
RValues_par = L_res_par/(k_res_par*A_res_par)
RValues_inv = 1/RValues_par
Rtot_parallel = (RValues_inv.sum())**(-1)

Rtot= Rtot_series + Rtot_parallel
print "the total resistance is: " + str(Rtot) + " (degC/W)"

Q = (Tin - Tout)/Rtot
print "the rate of heat transfer through the wall for each unit is "+str(Q)+ " (W)"
Qtot = (Q*H*L)/0.25
print "the total rate of heat transfer through the wall is "+str(Qtot)+ " (W)"