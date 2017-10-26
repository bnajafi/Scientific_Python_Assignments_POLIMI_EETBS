# Assignment 5, Step 2
import numpy as np

materials_names= np.array(["Wood bevel lapped siding","Wood fiberboard sheeting,13mm","Glass fiber insulation,90mm","Wood stud,38mm*90mm","Gypsum wallboard,13mm","OutSurface 24km/h wind","InsideSurface still air"]) 
materials_Rvalues =np.array([0.14,0.23,2.45,0.63,0.079,0.03,0.12])

layerNames_serie = np.array(["Wood bevel lapped siding","Wood fiberboard sheeting,13mm","Gypsum wallboard,13mm","OutSurface 24km/h wind","InsideSurface still air"])
layerNames_parallel = np.array(["Glass fiber insulation,90mm","Wood stud,38mm*90mm"])


thisLayer_name = "Wood bevel lapped siding"
thisLayer_Rvalue = materials_Rvalues[materials_names==thisLayer_name]

layerNames_serie = np.array(["Wood bevel lapped siding","Wood fiberboard sheeting,13mm","Gypsum wallboard,13mm","OutSurface 24km/h wind","InsideSurface still air"])
RValue_serie = np.zeros(5)

for layerName in layerNames_serie:
    RValue_serie[layerNames_serie==layerName] = materials_Rvalues[materials_names==layerName]
    Resistances_RtotSerie=RValue_serie.sum()

layerNames_parallel = np.array(["Glass fiber insulation,90mm","Wood stud,38mm*90mm"])
RValue_parallel = np.zeros(2)

for layerName in layerNames_parallel:
    RValue_parallel[layerNames_parallel==layerName] = 1/materials_Rvalues[materials_names==layerName]
    Resistances_RtotParallel=RValue_parallel.sum()

Resistances_Rtot = Resistances_RtotParallel+Resistances_RtotSerie
U_tot = 1/Resistances_Rtot
print "SO the overall resistance is:" + str(Resistances_Rtot)+ "degC/W*m^2"
print "*****************************"
print"the total U value is:"+str(U_tot)+"(W/degC)"
print "*****************************"



