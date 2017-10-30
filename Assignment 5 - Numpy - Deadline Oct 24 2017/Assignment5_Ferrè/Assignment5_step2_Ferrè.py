import numpy as np

material_library_name = np.array(["outside_surface_winter","wood_bevel","wood_fiberboard","glass_fiber","wood_stud","gypsum_wallboard","inside_surface"])
material_library_Rvalue= np.array([0.030,0.14,0.23,2.45,0.63,0.079,0.12])
resistances_types = np.array(["serie","serie","serie","parallel","parallel","serie","serie"])
resistances_serie = np.array(np.zeros(5))
resistances_serie = material_library_Rvalue[resistances_types=="serie"]
resistances_parallel = np.array(np.zeros(2))
resistances_parallel = material_library_Rvalue[resistances_types=="parallel"]
firstratio=float(0.75)
Rtot_serie=resistances_serie.sum()
R_tot= np.array(np.zeros(2))
R_tot = resistances_parallel+Rtot_serie
U_values=1/R_tot 
U_tot=(U_values[0]*firstratio)+(U_values[1]*(1-firstratio))
print ("Total U value is: ") +str(U_tot)