import os
os.chdir("C:\Users\jude\Desktop\judes script code\WEEK 4")                        #Set the current directory to other to get File 1
import wallCalculations_Dontoh as W

#----Defining all values----
layersInseries_forParallel=["insideSurface","outsideSurfaceWinter","Wood bevel lapped siding","Wood fiberboard","Gypsum wallboard","Common brick"]
layersInParallel=["Glass fiber insulation","Wood stud"]
layers_forRoof=["insideSurface","outsideSurfaceWinter","Wood","Asphalt shingle roofing"]
layers_forDoor=["insideSurface","outsideSurfaceWinter","Wood"]
deltaT_heating,wall_Area,roof_Area,door_Area=20-(-4.8),105.8,20*10,1*2.2
 
#----Getting the U-values from imported functions of File1----
U_wall=W.wallCalc_withParallel(layersInseries_forParallel,layersInParallel)
U_door=W.wallCalc_OnlyInSeries(layers_forDoor,layers_forRoof)["U-Value of Door"]
U_roof=W.wallCalc_OnlyInSeries(layers_forDoor,layers_forRoof)["U-value of Roof"]

opaque_Surfaces={"Wall":{"U-value":U_wall,"Area":wall_Area,"Heating Load":0},"Door":{"U-value":U_door,"Area":door_Area,"Heating Load":0},"Roof":{"U-value":U_roof,"Area":roof_Area,"Heating Load":0}}
heat_Load_total=0

for key in opaque_Surfaces:
    opaque_Surfaces[key]["Heating Load"]=round((opaque_Surfaces[key]["U-value"]*deltaT_heating*opaque_Surfaces[key]["Area"]),1)
    heat_Load_total+=round((opaque_Surfaces[key]["U-value"]*deltaT_heating*opaque_Surfaces[key]["Area"]),1)
    
#Printing values
for key in opaque_Surfaces:                                                     
    print("The heating load of the "+key+" is: "+str(opaque_Surfaces[key]["Heating Load"])+ " Watt")

print("\nThe total heating load is: "+str(heat_Load_total)+" Watt")