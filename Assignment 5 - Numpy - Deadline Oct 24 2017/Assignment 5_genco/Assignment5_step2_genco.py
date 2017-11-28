

import numpy as np

material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
"wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
"gypsum_wallboard":0.079}

Rlayer=np.array(["Rserie","Rserie",
"Rserie","Rparallelo","Rparallelo","Rserie",
"Rserie"])
Rvalues=np.array([0.030, 0.14,0.23, 2.45, 0.63, 0.12, 0.079])

R_serires_tot=np.array(np.zeros(7))
R_serires_tot[Rlayer=="Rserie"]=Rvalues[Rlayer=="Rserie"]
R_S_tot=R_serires_tot.sum()

R_parallel_tot=np.array(np.zeros(7))
R_parallel_tot[Rlayer=="Rparallelo"]=Rvalues[Rlayer=="Rparallelo"]
R_tot=np.array(np.zeros(2))
R_tot[0]=R_S_tot+R_parallel_tot[3]
R_tot[1]=R_S_tot+R_parallel_tot[4]

U=np.array(1/R_tot)


FR=float(0.75)

U_tot=U[0]*FR+U[1]*(1-FR)





