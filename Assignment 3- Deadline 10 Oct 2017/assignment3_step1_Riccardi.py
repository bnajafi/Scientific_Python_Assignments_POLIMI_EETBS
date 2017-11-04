# -*- coding: utf-8 -*-
#assignment 3 - step 1

Material_library={"WoodBevel":0.14,"WoodFiberboard_13mm":0.23,"GlassFiberIns_90mm":2.45,
"WoodStud_38x90mm2":0.63,"GypsumWallboard_13mm":0.079,"CommonBrick_100mm":0.12,"AcousticTile":0.32,
"BuildingPaper":0.011,"Plywood_13mm":0.11,"OutsideSurface":0.030,"InsideSurface":0.12}

AirOnTwoSides=["InsideSurface","OutsideSurface"]
LayersInsSeries=["WoodBevel","WoodFiberboard_13mm","GypsumWallboard_13mm"]
LayersParallel=["GlassFiberIns_90mm","WoodStud_38x90mm2"]
AllLayers=AirOnTwoSides+LayersInsSeries+LayersParallel

Rvalues=[]
for anyres in AllLayers:
    Rvalues.append(Material_library[anyres])
Rtot_values=[]

for anylayer in LayersParallel:
    LayersComplete=AirOnTwoSides+LayersInsSeries
    LayersComplete.append(anylayer)
    Rtot=0
    for anyvalue in LayersComplete:
        print"This layer is: "+anyvalue+" and its resistance is "+str(Material_library[anyvalue])+" [(m^2*°c)/W]\n"
        Rtot=Rtot+Material_library[anyvalue]
    Rtot_values.append(Rtot)
    print"****************\n"
    
print "The total resistance between studs is: "+str(Rtot_values[0])+" [(m^2*°c)/W]"
print "The U factor between studs is: "+str(1/Rtot_values[0])+" [W/(m^2*°c)]\n"
print "The total resistance at studs is: "+str(Rtot_values[1])+" [(m^2*°c)/W]"
print "The U factor at studs is: "+str(1/Rtot_values[1])+" [W/(m^2*°c)]\n"

AreaFraction=0.75

U_overall=AreaFraction*1/Rtot_values[0]+(1-AreaFraction)*1/Rtot_values[1]
print "The overall U factor of the wall is: "+str(U_overall)+" [W/(m^2*°c)]"
print "The overall thermal resistance of the wall is: "+str(1/U_overall)+" [(m^2*°c)/W]"
Area=0.8*50*2.5
Tin=22
Tout=-2
Qwall=U_overall*Area*(Tin-Tout)
print"The rate of heat loss through the walls of the house is: "+str(Qwall)+" [W]"




    

    