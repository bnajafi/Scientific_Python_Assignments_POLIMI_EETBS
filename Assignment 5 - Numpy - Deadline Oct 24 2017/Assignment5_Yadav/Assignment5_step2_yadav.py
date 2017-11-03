import numpy as np

Material_library= np.array(["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","glassFibreInsulation_25mm","woodStud_90mm","gypsum_13mm",
"insideSurface"])
Material_Rvalues=np.array([0.03,0.14,0.23,2.52,0.63,0.079,0.12])
Material_Length=np.array([None,13,13,90,90,13,None])
My_layer=(["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","gypsum_13mm","insideSurface"])
R_betweenStud,R_atStud=My_layer+["glassFibreInsulation_25mm"], My_layer+["woodStud_90mm"]
R_betweenStud_1=np.zeros(7)
R_atStud_1=np.zeros(7)
perimeter,height,glazingPercentage,outsideTemperature,insideTemperature,fractionBetweenstuds=50,2.5,20,-2,22,0.75


for layer in R_betweenStud:
    layer_Rvalue=Material_Rvalues[Material_library==layer]
    R_betweenStud_1[Material_library==layer]=layer_Rvalue

R_betweenStud_tot=R_betweenStud_1.sum()

for layer in R_atStud:
    layer_Rvalue=Material_Rvalues[Material_library==layer]
    R_atStud_1[Material_library==layer]=layer_Rvalue

R_atStud_tot=R_atStud_1.sum()

Uoverall=round((fractionBetweenstuds*(1/R_betweenStud_tot)+(1-fractionBetweenstuds)*(1/R_atStud_tot)),2)
Roverall=round((1/Uoverall),2)
wallArea=(1-(glazingPercentage/100.0))*perimeter*height
heatLoss=int(Uoverall*wallArea*(insideTemperature-outsideTemperature))
print("The overall heat transfer coefficient(U-factor) is : "+str(Uoverall)+" W/m^2 degC"+"\n"+"The overall unit therml resistance(R-Value) is : "+str(Roverall)+" m^2 degC/W"+"\n"+"The heat loss through the wall is: "+str(heatLoss)+" W")

