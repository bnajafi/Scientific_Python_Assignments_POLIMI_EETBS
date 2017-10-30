import numpy as np

#material library
materials_names = np.array(["outside","woodbevel","woodfiber","glassfiber","stud","gypsum","inside"])
materials_res = np.array([0.03,0.14,0.23,2.45,0.63,0.079,0.12])
 
frac_area = 0.75


#sum of resistances in series
layer_ser = np.array(["outside","woodbevel","woodfiber","gypsum","inside"])
Rvalue_ser = np.zeros(layer_ser.size)

for n in layer_ser:
    Rvalue_ser[layer_ser==n] = materials_res[materials_names==n]



#now I add layers in parallel
layer_par = np.array (["glassfiber","stud"])
Rvalue_par = np.zeros(layer_par.size)


for m in layer_par:
    Rvalue_par[layer_par==m] = materials_res[materials_names==m]

#definition of two sets of layers

set_1 = np.append([Rvalue_ser],[Rvalue_par[0]])
set_2 = np.append([Rvalue_ser],[Rvalue_par[1]])

#U calculation
U_overall=(1/set_1.sum()*frac_area)+(1/set_2.sum()*(1-frac_area))
