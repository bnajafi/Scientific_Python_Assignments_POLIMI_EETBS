import numpy as np

material_names = np.array (["WoodBevelLappedSiding","WoodFiberboardSheeting","GlassFiberInsulation","WoodStud","GypsumWallboard","OutsideSurfaceWinter","InsideSurface"])
Rvalues = np.array([0.14,0.23,2.45,0.63,0.079,0.03,0.12])

layers_series = np.array (["WoodBevelLappedSiding","WoodFiberboardSheeting","GypsumWallboard","OutsideSurfaceWinter","InsideSurface"])
layers_parallel = np.array (["GlassFiberInsulation","WoodStud"])
area_fraction_ins = 0.75

R_series = np.zeros(layers_series.size)
R_parallel = np.zeros(layers_parallel.size)
R_vector = np.zeros(layers_parallel.size)


for layerName in layers_series:
    R_series[layers_series==layerName] = Rvalues[material_names==layerName]

Rser = R_series.sum()


for layerName in layers_parallel:
    R_parallel[layers_parallel==layerName] = Rvalues[material_names==layerName]
    R_vector[layers_parallel==layerName] = R_parallel[layers_parallel==layerName] + Rser #R_vector is an array of two element,the first element takes into account GlassFiberInsulation, the second one takes into account Woodstud
    

U_overall = area_fraction_ins/R_vector[0]+(1-area_fraction_ins)/R_vector[1]

Area=0.8*2.5*50
T_outdoor=-2
T_indoor=22
Q_overall=U_overall*Area*(T_indoor-T_outdoor)

print("The overall trasmittance is: " + str(U_overall)+" W/m2K"+" the overall heat loss is: "+str(Q_overall)+" W")