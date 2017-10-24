
import sys
import os
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()


import walllCalculations_CHEN as Wall

Layers_throughInsulation=["GypsumWallboard_13mm","GlassFiberInsulation_90mm","OutsideSurfaceWinter","CommonBrick_100mm"
,"WoodBevelLappedSiding_13mm","WoodFiberboardSheeting_13mm","InsideSurfaceAir"]
Layers_throughStuds=["GypsumWallboard_13mm","WoodStud_90mm","OutsideSurfaceWinter","CommonBrick_100mm"
,"WoodBevelLappedSiding_13mm","WoodFiberboardSheeting_13mm","InsideSurfaceAir"]
door=["InsideSurfaceAir","OutsideSurfaceWinter", "Wood_50mm"]

results= Wall.wall_calculator([Layers_throughInsulation,Layers_throughStuds],0.70,door,0.25)
print results

A={"A_wall":105.8,"A_roof":200,"A_door":2.2} #m2
T=24.8 #Temperature_Difference,degreeC
HF={"HF_wall":results["the total U of the wall"]*T,"HF_roof":results["the total U of the roof"]*T,
"HF_door":results["the total U of the door"]*T} #W/m2
Q_heating={"Q_wall":A["A_wall"]*HF["HF_wall"],"Q_roof":A["A_roof"]*HF["HF_roof"],"Q_door":A["A_door"]*HF["HF_door"]}
Q_opaque=Q_heating["Q_wall"]+Q_heating["Q_roof"]+Q_heating["Q_door"]

print "The heating factors in opaque is: " +str(HF) +" W/m2"
print "The heating loads in opaque are: "+str(Q_heating) +" W"
print "The total heating load in opaque is: " + str(Q_opaque) +" W"