#Assignment5_step2_CHEN

import numpy as np

materials_names=np.array(["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
"WoodFiberboardSheeting_13mm","GlassFiberInsulation_90mm","WoodStud_90mm",
"GypsumWallboard_13mm","InsideSurfaceAir"])

materials_Rvalues=np.array([0.030,0.14,0.23,2.45,0.63,0.079,0.12])

Layers_throughInsulation=np.array(["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
"WoodFiberboardSheeting_13mm","GlassFiberInsulation_90mm",
"GypsumWallboard_13mm","InsideSurfaceAir"])
Layers_throughStuds=np.array(["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
"WoodFiberboardSheeting_13mm","WoodStud_90mm",
"GypsumWallboard_13mm","InsideSurfaceAir"])

RValue_throughInsulation =np.zeros(Layers_throughInsulation.size) 
RValue_throughStuds =np.zeros(Layers_throughStuds.size) 
    
for layerName in Layers_throughInsulation:
    RValue_throughInsulation[Layers_throughInsulation==layerName] = materials_Rvalues[materials_names==layerName]
    RValue_total_throughInsulation=RValue_throughInsulation.sum()
    
for layers in Layers_throughStuds:
    RValue_throughStuds[Layers_throughStuds==layers]=materials_Rvalues[materials_names==layers]
    RValue_total_throughStuds=RValue_throughStuds.sum()
    
Layers_parallel=np.array([Layers_throughInsulation,Layers_throughStuds])
RValue_parallel= np.array([RValue_total_throughInsulation,RValue_total_throughStuds])
Ratio=np.array([float(0.75),float(0.25)]) #insulation 0.75, while studs 1-ratio

Layers_Parallel_Ufactor=1/RValue_parallel
Layers_Parallel_UnitUfactor=Ratio*Layers_Parallel_Ufactor
Utot_Unit=Layers_Parallel_UnitUfactor.sum()
Rtot_Unit=1/Utot_Unit

A_wall=0.8*50*2.5 #The perimeter of the building is 50m, the height of the walls is 2.5m,the glazing constitutes 20 percent of the walls
Ti=22
To=-2
Q=Utot_Unit*A_wall*(Ti-To)
print "The overall unit U-factor is: "+ str(Utot_Unit)+ " W/m2*degreeC"
print "The overall unit thermal resistance is: "+str(Rtot_Unit)+ " m2*degreeC/W"
print "The rate of heat loss through the walls under design conditions is: "+str(Q) + " W"
   
    
    