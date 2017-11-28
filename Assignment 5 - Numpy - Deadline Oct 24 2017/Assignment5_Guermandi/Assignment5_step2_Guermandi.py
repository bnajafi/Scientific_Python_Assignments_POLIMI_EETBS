import numpy as np
mat=np.array(["in surface","wood lapped","wood sheeting","insulation","wood stud","gypsum wallboard","out surface"])
r=np.array([0.12,0.14,0.23,2.45,0.63,0.079,0.03])
ratio=np.array([0.25,0.75])
series=np.array(["in surface","wood lapped","wood sheeting","gypsum wallboard","out surface"])
parallel=np.array(["wood stud","insulation"])
paral_r=np.array([2.45, 0.63])
Rseries=np.array(np.zeros(series.size))
Rparal=np.array(np.zeros(parallel.size))
Rwall=np.array(np.zeros(parallel.size))
Uwall=np.array(np.zeros(parallel.size))

for anylayer in series:
    Rseries[series==anylayer] = r[mat==anylayer]
R_series=Rseries.sum()
U_series=1.0/R_series

for anylayer in parallel:
    Rparal[parallel==anylayer] = r[mat==anylayer]

Rwall = Rparal+R_series
Uwall = 1.0 / Rwall * ratio
U=Uwall.sum()


print 'the total unit thermal resistance is '+str(U)
    