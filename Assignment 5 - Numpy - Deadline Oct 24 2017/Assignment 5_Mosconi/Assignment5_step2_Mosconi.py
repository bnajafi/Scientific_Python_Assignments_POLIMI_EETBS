import numpy as np


layerMaterialLibrary=np.array(["insideSurface","woodBevel","woodfiberboard_13mm",
        "gypsumBoard","outsideSurfaceWinter","woodStud","acousticTile",
        "buildingPaper","outsideSurfaceSummer","glassFiber"])
layerResistanceValue=np.array([0.12,0.14,0.23,0.079,0.030,0.63,0.32,0.011,0.044,2.45])

layerMaterial=np.array(["insideSurface","woodBevel","woodfiberboard_13mm",
        "gypsumBoard","outsideSurfaceWinter"])
layerMaterialParallel=np.array(["glassFiber","woodStud"])
f=0.75

RValueMaterial= np.zeros(layerMaterial.size)

for layerName in layerMaterial:
    RValueMaterial[layerName==layerMaterial] =layerResistanceValue[layerMaterialLibrary==layerName]

ResistanceSeries=np.sum(RValueMaterial)

R=np.zeros(layerMaterialParallel.size)

for layerName in layerMaterialParallel:
    R[layerMaterialParallel==layerName] =layerResistanceValue[layerMaterialLibrary==layerName]


parallelResistances=R+ResistanceSeries
U=1/parallelResistances[0]*f+1/parallelResistances[1]*(1-f)

Area=0.8*2.5*50
Tin=22
Tout=-2

Q_overall=U*Area*(Tin-Tout)
print ("the overall transmittance value is "+str(U)+" W/m2/K")
print ("The overall heat rate is "+str(Q_overall)+" W")  