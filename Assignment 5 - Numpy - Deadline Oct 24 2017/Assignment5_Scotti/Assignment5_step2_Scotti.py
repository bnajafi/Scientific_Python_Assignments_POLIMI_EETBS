import numpy as np


material_names=np.array(["out","bevel","fiberboard","wallboard","fiber_90","stud_90","in"])
material_resistances=np.array([0.03,0.14,0.23,0.079,2.45,0.63,0.12])
ratio=0.75

Layers_serie = ["bevel", "fiberboard", "wallboard"]
Layers_parallel = ["fiber_90", "stud_90"]

layernames_mywall=np.array(["out","bevel","fiberboard","wallboard","fiber_90","stud_90","in"])
resistance_type=np.array(["serie","serie","serie","serie","parallel","parallel","serie"])
resistances=np.array([0.03,0.14,0.23,0.079,2.45,0.63,0.12])

R_serie_array=np.array(np.zeros(7))
R_parallel_array=np.array(np.zeros(7))

R_serie_array[resistance_type=="serie"]=resistances[resistance_type=="serie"]
R_parallel_array[resistance_type=="parallel"]=resistances[resistance_type=="parallel"]

R_serie=sum(R_serie_array)
R_parallel=(R_parallel_array[4]*R_parallel_array[5])/(R_parallel_array[4]+R_parallel_array[5])

R_tot=np.array(np.zeros(2))
R_tot[0]=R_serie+R_parallel_array[4]
R_tot[1]=R_serie+R_parallel_array[5]

U_tot = ratio * R_tot[0]**-1+(1-ratio)*R_tot[1]**-1