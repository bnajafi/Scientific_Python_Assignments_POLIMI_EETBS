# -*- coding: utf-8 -*-
def wall(layersSeries,layersParallel,f_areaPar):
    Material={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
    "InsideSurface":0.12,"OutsideSurfaceWinter":0.03}
    Air=["InsideSurface","OutsideSurfaceWinter"]
    Rtot=0
    Rparalleltot_rev=0
    Rseriestot=0
    ListWallResistances=[]
    LayersSeriesComplete=layersSeries+Air
    for anylayer in LayersSeriesComplete:
        Rseries=Material[anylayer]
        Rseriestot=Rseriestot+Rseries
        ListWallResistances.append(Rseries)   
    for anylayer1 in layersParallel:
        for anyf in f_areaPar:
         Rparallel=Material[anylayer1]
         Rparalleltot_rev=1/Rparallel*anyf+Rparalleltot_rev
         Rparalleltot=1/Rparalleltot_rev
         ListWallResistances.append(Rparallel)
    Rtot=Rparalleltot+Rseriestot
    results={"Rtot":Rtot,"Rparalleltot":Rparalleltot,"Rseriestot":Rseriestot,"Rvalue of all layers":ListWallResistances}
    return results
WallLayersSeries=["WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard"]
WallLayersParallel=["GlassFiberInsulation","Woodstud"]
f_wallAreaPar=[0.75,0.25]
Wall_results=wall(WallLayersSeries,WallLayersParallel,f_wallAreaPar)
print Wall_results