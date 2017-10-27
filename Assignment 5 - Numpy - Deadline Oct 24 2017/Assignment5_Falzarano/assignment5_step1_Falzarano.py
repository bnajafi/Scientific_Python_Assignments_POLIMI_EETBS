# -*- coding: utf-8 -*-
import numpy as np

#temperatures on the two sides of the wall
T_inf_1 = 20
T_inf_2 = -10

#I first define lists with all the elements I need in the calculation referred to each layer of the wall
Layers = np.array(["air_1","foam","plastic1","plastic2","air_2","plastic3","brick","plastic4"])
Layer_type = np.array(["conv","cond","cond","cond","conv","cond","cond","cond"])

h = np.array([10,None,None,None,25,None,None,None])   #Convective resistances
k= np.array([None,0.026,0.22,0.22,None,0.22,0.72,0.22])   #Conductive resistances
Lenght= np.array([None,0.03,0.02,0.02,None,0.16,0.16,0.16])
Area = np.array([0.25,0.25,0.25,0.25,0.25,0.015,0.22,0.015])
Ser_Par = np.array(["ser","ser","ser","ser","ser","par","par","par"])

#here I define the arrays I will fill with resistance values
Res_cond= np.array(np.zeros(8))
Res_conv = np.array(np.zeros(8))
Res_par = np.array(np.zeros(8))
Res_par_inv = np.array(np.zeros(8))

#I divide the information on the layers in three sets, so I can find separately
#the convective resistance, conductive resistance in series and conductive resistance in parallel
M = (Layer_type=="cond")&(Ser_Par=="ser")
B = (Layer_type=="conv")
N = (Layer_type=="cond")&(Ser_Par=="par")


Res_cond[M] = Lenght[M]/ (k[M]*Area[M])
Res_conv[B] = 1/(h[B]*Area[B])
Res_par[N]= Lenght[N]/ (k[N]*Area[N])

Res_par_inv[N] = 1/Res_par[N]
Res_par_sum = 1/Res_par_inv.sum()

#I put all the resistances together in one array
R_ser_tot = Res_cond + Res_conv
R_tot = np.append([R_ser_tot],[Res_par_sum])

#now i have to switch from the array with all the resistances to the sum of all the values in parallel
R_sum = R_tot.sum()
print ("the total resistance of the wall unit is " + str(R_sum) + " °C/W")

#the calculation of Q is as follows
Q = (T_inf_1 - T_inf_2)/R_sum
print ("The heat loss through the wall unit is "+str(Q)+" W")



#whole wall data
Wall = np.array([0.25,3,5])
Wall_type = np.array(["unit_area","height","width"])

Q_wall = Q*Wall[1]*Wall[2]/Wall[0]


print ("The total heat loss through the wall is " + str(Q_wall) + " W")

