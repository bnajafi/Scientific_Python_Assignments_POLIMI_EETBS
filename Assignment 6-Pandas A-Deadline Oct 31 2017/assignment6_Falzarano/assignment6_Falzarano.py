import numpy as np
import pandas as pd
#temperatures on the two sides of the wall
T_inf_1 = 20
T_inf_2 = -10

#I'm creating a table with all the layers and their characteristics

Layers = np.array(["air_1","foam","plastic1","plastic2","air_2","plastic3","brick","plastic4"])
Layer_type = np.array(["conv","cond","cond","cond","conv","cond","cond","cond"])

h = np.array([10,None,None,None,25,None,None,None])   #Convective resistances
k= np.array([None,0.026,0.22,0.22,None,0.22,0.72,0.22])   #Conductive resistances
Lenght= np.array([None,0.03,0.02,0.02,None,0.16,0.16,0.16])
Area = np.array([0.25,0.25,0.25,0.25,0.25,0.015,0.22,0.015])
Ser_Par = np.array(["ser","ser","ser","ser","ser","par","par","par"])


Layers_data_frame = pd.DataFrame([Layers,Layer_type,h,k,Lenght,Area,Ser_Par],index=["Name","Type","h","k","Lenght","Area","Ser_Par"],columns=[1,2,3,4,5,6,7,8])


print ("The wall composition is as follows:")
print (Layers_data_frame)
print ("***************************************************************************")
#resistances in parallel
res_par = (Layers_data_frame.loc["Lenght"]/(Layers_data_frame.loc["k"]*Layers_data_frame.loc["Area"]))[Layers_data_frame.loc["Ser_Par"]=="par"]
res_par_inv = 1/res_par
res_par_tot = 1/res_par_inv.sum()

#resistances in series - conductive
res_ser = (Layers_data_frame.loc["Lenght"]/(Layers_data_frame.loc["k"]*Layers_data_frame.loc["Area"]))[Layers_data_frame.loc["Ser_Par"]=="ser"]

#convective resistances
res_conv = (1/(Layers_data_frame.loc["h"]*Layers_data_frame.loc["Area"]))[Layers_data_frame.loc["Type"]=="conv"]

R_tot = res_par_tot + res_conv.sum() + res_ser.sum()

Q = (T_inf_1 - T_inf_2)/R_tot
print ("The heat loss through the wall unit is "+str(Q)+" W")
