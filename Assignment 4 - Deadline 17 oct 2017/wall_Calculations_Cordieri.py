def wallCalc_withParallel(layersSeries,layersParallel,f):
    Material={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
    "InsideSurface":0.12,"OutsideSurfaceWinter":0.03,"Wood":0.22,"CommonBrick":0.12,"AsphaltShingleRoofing":0.077,"ConcreteLight":1.17}
    Air=["InsideSurface","OutsideSurfaceWinter"]
    Rtot=[]
    Rseriestot=0
    LayersSeriesComplete=layersSeries+Air
    for anylayer in LayersSeriesComplete:
        Rseries=Material[anylayer]
        Rseriestot=Rseriestot+Rseries   
    for anylayer1 in layersParallel:
         Rparallel=Material[anylayer1]
         R=Rparallel+Rseriestot
         Rtot=Rtot+[R]
    Uwood=1/Rtot[1]
    Uins=1/Rtot[0]
    U_overall=Uwood*(1-f)+Uins*f
    results=U_overall
    return results
def wallCalc_onlyInSeries  (layersSeries):
     Material={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
    "InsideSurface":0.12,"OutsideSurfaceWinter":0.03,"Wood":0.22,"CommonBrick":0.12,"AsphaltShingleRoofing":0.077,"ConcreteLight":1.17}
     Air=["InsideSurface","OutsideSurfaceWinter"]
     Rseriestot=0
     LayersSeriesComplete=layersSeries+Air
     for anylayer in LayersSeriesComplete:
        Rseries=Material[anylayer]
        Rseriestot=Rseriestot+Rseries
        Useries=1/Rseriestot
        results=Useries
     return results              
    
       