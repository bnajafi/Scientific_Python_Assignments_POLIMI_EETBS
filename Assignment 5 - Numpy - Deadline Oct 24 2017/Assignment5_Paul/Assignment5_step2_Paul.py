import numpy as np

material_names=np.array(["Wood bevel lapped siding","Wood fiberboard","Glass fiber insulation","Wood stud","Gypsum wallboard","insideSurface","outsideSurfaceWinter"])
material_Rvalues=np.array([0.14,0.23,2.45,0.63,0.079,0.12,0.03])
material_length=np.array([13,13,90,90,13,None,None])
layersInseries=["insideSurface","outsideSurfaceWinter","Wood bevel lapped siding","Wood fiberboard","Gypsum wallboard"]
betweenStuds,atStuds=layersInseries+["Glass fiber insulation"],layersInseries+["Wood stud"]
betweenStuds_Rvalues=np.zeros(7)
atStuds_Rvalues=np.zeros(7)
perimeter,height,glazingPercentage,outsideTemperature,insideTemperature,fractionBetweenstuds=50,2.5,20,-2,22,0.75

for layername in betweenStuds:
    layer_Rvalue=material_Rvalues[material_names==layername]
    betweenStuds_Rvalues[material_names==layername]=layer_Rvalue

betweenStuds_Rtot=betweenStuds_Rvalues.sum()

for layername in atStuds:
    layer_Rvalue=material_Rvalues[material_names==layername]
    atStuds_Rvalues[material_names==layername]=layer_Rvalue

atStuds_Rtot=atStuds_Rvalues.sum()

Uoverall=round((fractionBetweenstuds*(1/betweenStuds_Rtot)+(1-fractionBetweenstuds)*(1/atStuds_Rtot)),2)
Roverall=round((1/Uoverall),2)
wallArea=(1-(glazingPercentage/100.0))*perimeter*height
heatLoss=int(Uoverall*wallArea*(insideTemperature-outsideTemperature))
print("The overall heat transfer coefficient(U-factor) is : "+str(Uoverall)+" W/m^2 degC"+"\n"+"The overall unit therml resistance(R-Value) is : "+str(Roverall)+" m^2 degC/W"+"\n"+"The heat loss through the wall is: "+str(heatLoss)+" W")


