import numpy as np

# DEFINING 

material_names = np.array (["Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Glass_Fiber_Insulation","Wood_Stud","Gypsum_Wallboard","Outside_Surface_Winter","Inside_Surface"])
material_resistances = np.array([0.14,0.23,2.45,0.63,0.079,0.03,0.12])

layers_in_series = np.array (["Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Gypsum_Wallboard","Outside_Surface_Winter","Inside_Surface"])
layers_in_parallel = np.array (["Glass_Fiber_Insulation","Wood_Stud"])
area_fraction = 0.75


#INITIALIZING ARRAYS

R_series = np.zeros(layers_in_series.size)
R_parallel = np.zeros(layers_in_parallel.size)
Area_coefficient = np.zeros(layers_in_parallel.size)
R_section = np.zeros(layers_in_parallel.size)
U_section = np.zeros(layers_in_parallel.size)


# RESISTANCES IN SERIES

for layerName in layers_in_series:
    R_series[layers_in_series==layerName] = material_resistances[material_names==layerName]

Rser = R_series.sum()


# RESISTANCES IN PARALLEL

for layerName in layers_in_parallel:
    R_parallel[layers_in_parallel==layerName] = material_resistances[material_names==layerName]
    R_section[layers_in_parallel==layerName] = R_parallel[layers_in_parallel==layerName] + Rser
    
    if (layerName=="Glass_Fiber_Insulation"):
        Area_coefficient[layers_in_parallel==layerName] = area_fraction
    else:
        Area_coefficient[layers_in_parallel==layerName] = 1-area_fraction
   
    U_section[layers_in_parallel==layerName] = Area_coefficient[layers_in_parallel==layerName] / R_section[layers_in_parallel==layerName]
    
    
#TOTAL RESISTANCE
    
Utot =  U_section.sum()
Rtot = 1.0 / Utot

      