import numpy as np
fraction=0.75

Material_library=np.array(["outsideSurfaceWinter","woodBevel","woodFiberboard_13mm","glassFiberInsulation_90mm","woodStud_90mm","gypsumWallboard_13mm","insideSurface"])
Resistance_value=np.array([0.030,0.14,0.23,2.45,0.63,0.079,0.12])


layers_wall_series=np.array(["outsideSurfaceWinter","woodBevel","woodFiberboard_13mm", "gypsumWallboard_13mm","insideSurface"])
layers_wall_parallel=np.array(["glassFiberInsulation_90mm","woodStud_90mm"])
fraction=float(0.75)

Resistanceinseries=np.zeros(layers_wall_series.size)
Resistanceinparallel=np.zeros(layers_wall_parallel.size)

for material in layers_wall_series:
    Resistanceinseries[material==layers_wall_series]=Resistance_value[Material_library==material]
    
Resistanceinseriestot=sum(Resistanceinseries)


for material in layers_wall_parallel:
    Resistanceinparallel[material==layers_wall_parallel]=Resistance_value[Material_library==material]+Resistanceinseriestot
    
U_overall = fraction*Resistanceinparallel[0]**-1 +(1-fraction)*Resistanceinparallel[1]**-1
 