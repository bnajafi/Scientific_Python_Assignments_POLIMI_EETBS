import numpy as np

def Rvalues_matrixdef(matlib, layers, rvalues) : 
    tot=np.zeros(layers.size)
    for index in layers:
        tot[index==layers]=rvalues[index==matlib]
    return tot

materials_lib=np.array(['Outside surface','Inside surface','Glass fiber insulation 90mm','Mineral fiber batt 25 mm','Urethane rigid foam 25 mm','Stucco 25mm','Face brick 100mm','Common brock 100mm','steel siding','Slag 13mm','Wood 25mm','Wood stud 2x4 in','Wood Stud 2x6 in','Clay tile 100mm','Acoustic tile','Asphalt shingle roofing','Building paper','Gypsum board 13mm','Wood fiberboard 13mm','Plywood 13mm','Cememnt mortar','Wood bevel siding 13x200mm'])
RValues_library=np.array([0.030,0.12,2.45,0.66,0.98,0.037,0.075,0.12,0.00,0.067,0.22,0.63,0.98,0.18,0.32,0.077,0.011,0.079,0.23,0.11,0.018,0.14])

layers_series=np.array(['Outside surface','Inside surface','Gypsum board 13mm','Wood fiberboard 13mm','Wood bevel siding 13x200mm'])

layers_parallel=np.array(['Glass fiber insulation 90mm','Wood stud 2x4 in'])

ratio_area=float(0.75)
    
series_tot=(Rvalues_matrixdef(materials_lib, layers_series, RValues_library)).sum()

parallel_tot=Rvalues_matrixdef(materials_lib, layers_parallel, RValues_library)+series_tot

U=1/parallel_tot

area=np.array([ratio_area, 1-ratio_area])

overall_U_Array= U*area

overall_U_Value= overall_U_Array.sum()

print overall_U_Value