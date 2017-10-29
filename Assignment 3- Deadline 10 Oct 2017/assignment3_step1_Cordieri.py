# -*- coding: utf-8 -*-
Material={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
"InsideSurface":0.12,"OutsideSurfaceWinter":0.03}
WallLayersSeries=["WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard"]
WallLayersParallel=["GlassFiberInsulation","Woodstud"]
Air=["InsideSurface","OutsideSurfaceWinter"]
f_areaPar=[0.75,0.25]
Rtot=0
Rparalleltot_rev=0
Rseriestot=0
ListWallResistances=[]
LayersSeriesComplete=WallLayersSeries+Air
for anylayer in LayersSeriesComplete:
    Rseries=Material[anylayer]
    Rseriestot=Rseriestot+Rseries
    ListWallResistances.append(Rseries)
    print "this layer is: "+anylayer
    print"the value of R for this layer is: "+str(Rseries)+" m^2°C/W"
print "the total series layers resistance is "+str(Rseriestot)+" m^2°C/W"   
for anylayer1 in WallLayersParallel:
    for anyf in f_areaPar:
       Rparallel=Material[anylayer1]
       Rparalleltot_rev=1/Rparallel*anyf+Rparalleltot_rev
       Rparalleltot=1/Rparalleltot_rev
       ListWallResistances.append(Rparallel)
       print "this layer is: "+anylayer1
       print"the value of R for this layer is: "+str(Rparallel)+" m^2°C/W"   
print "the total parallel layers resistance is "+str(Rparalleltot)+" m^2°C/W"   
Rtot=Rparalleltot+Rseriestot
print "the total resistance is "+str(Rtot)+" m^2°C/W"   
print ListWallResistances