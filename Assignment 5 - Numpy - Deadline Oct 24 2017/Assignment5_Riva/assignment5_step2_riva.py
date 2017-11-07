#ASSIGNMENT 5

import numpy as np

material=np.array(["serie","serie","serie","paraller","paraller","serie","serie"])
r_material=np.array([0.030,0.14,0.23,2.45,0.63,0.12,0.079])

R_S_tot=np.zeros(7)
R_S_tot[material=="serie"]=r_material[material=="serie"]
R_S_final=R_S_tot.sum()

print R_S_tot
print R_S_final

R_P_tot=np.zeros(7)
R_P_tot[material=="paraller"]=r_material[material=="paraller"]

print R_P_tot

R1=R_S_final+R_P_tot[3]
R2=R_S_final+R_P_tot[4]

U1=1/R1
U2=1/R2

FR=float(0.75)

U_tot=U1*FR+U2*(1-FR)

print U_tot