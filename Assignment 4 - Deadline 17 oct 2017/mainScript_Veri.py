
import os
os.chdir("C:/Users/ale_v/Documents/Polimi/git_fork_clone2/gitFolderNew/Python4ScientificComputing_Fundamentals/alessVeri")
import wallCalculations_Veri as wallC_Veri
Material_library={"outsideSurface":0.03, "woodBevel":0.14, "woodFiberSheeting":0.23, "glassInsulation": 2.45,"woodStud":0.63, "gypsumWallboard":0.079, "insideSurface":0.12, "wood":0.44}
fArea=0.75
layers_series=["outsideSurface","woodBevel","woodFiberSheeting","gypsumWallboard","insideSurface"] 
layers_par=["glassInsulation", "woodStud"]

Uwalls=wallC_Veri.wallCalc_withParallel(layers_series,layers_par,fArea)
print "U value of the walls is: "+str(Uwalls)
layers=["outsideSurface", "insideSurface", "wood","commonBrick", "asphaltRoofing", "concreteLightweight", "cementMortar"]
Udoor=wallC_Veri.wallCalc_onlyInSeries(layers)
print "U value of the door is: "+str(Udoor)
U_roof=0.25
print "U value of the roof is: "+str(U_roof)
deltaT_heating=24.8
HF_walls=Uwalls*deltaT_heating
print "The heating factor of the walls is: "+str(HF_walls)
HF_door=Udoor*deltaT_heating
print "The heating factor of the door is: "+str(HF_door)
HF_roof=U_roof
print "The heating factor of the roof is: "+str(HF_roof)
A_walls=105.8
A_roof=200.0
A_door=2.2
Q_walls=HF_walls*A_walls
print "The heat transfer through the walls is: "+str(Q_walls)
Q_roof=HF_roof*A_roof
print "The heat transfer through the roof is: "+str(Q_roof)
Q_door=HF_door*A_door
print "The heat transfer through the door is: "+str(Q_door)