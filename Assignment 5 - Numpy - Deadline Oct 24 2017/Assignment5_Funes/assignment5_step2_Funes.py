import numpy as np

#Arrays of materials and their respective unit thermal resistances

materials_names= np.array(["insideSurface","outsideSurfaceWinter","gypsumWallboard13mm",
"woodStuds90mm","glassFiber25mm","woodFiberboard13mm","woodBevel200mm"]) 
materials_Rvalues =np.array([0.12, 0.03, 0.079, 0.63, 2.45, 0.23, 0.14])

#unit thermal resistance for Series is looked up 
fins = 0.75

layersInSeries = np.array(["insideSurface","outsideSurfaceWinter","gypsumWallboard13mm","woodFiberboard13mm","woodBevel200mm"]) 

RValues_Series = np.zeros(layersInSeries.size) 

for layerName in layersInSeries:
    RValues_Series[layersInSeries==layerName] = materials_Rvalues[materials_names==layerName]
#Total resistance for layers in series
Resistance_Tot_Series = RValues_Series.sum()
print "The equivalent resistance of the layers in Series is :"+str(Resistance_Tot_Series)

#unit thermal resistance for Parallel is looked up
layersInParallel = np.array(["glassFiber25mm","woodStuds90mm"]) # this is just a very simple example wall


RValues_Parallel = np.zeros(layersInParallel.size)

for layerName in layersInParallel:
    RValues_Parallel[layersInParallel==layerName] = materials_Rvalues[materials_names==layerName]
#Total resistance for layers in parallel
Resistance_Tot_Parallel = 1/((1/RValues_Parallel).sum())
print "The equivalent resistance of the layers in Parallel is :"+str(Resistance_Tot_Parallel)

#unit thermal resistance is found just considering the wood studs
FirstLayer = np.array([True, True, True, True, False, True, True,])
FirstLayernames = materials_names[FirstLayer]

RValues_Series = np.zeros(FirstLayernames.size) 

for layerName in FirstLayernames:
    RValues_Series[FirstLayernames==layerName] = materials_Rvalues[materials_names==layerName]
ResistanceTotFirst = RValues_Series.sum()
print "The unit thermal resistance just considering the wood studs is :"+str(ResistanceTotFirst)

Ufirst = 1/ResistanceTotFirst
print "The unit thermal coefficient just considering the wood studs is :"+str(Ufirst)

#unit thermal resistance is found just considering the glass fiber
SecondLayer = np.array([True, True, True, False, True, True, True,])
SecondLayernames=materials_names[SecondLayer]    

RValues_Series = np.zeros(SecondLayernames.size) 

for layerName in SecondLayernames:
    RValues_Series[SecondLayernames==layerName] = materials_Rvalues[materials_names==layerName]
ResistanceTotSecond = RValues_Series.sum()
print "The unit thermal resistance just considering the glass fiber is :"+str(ResistanceTotSecond)
Usecond = 1/ResistanceTotSecond
print "The unit thermal coefficient just considering the glass fiber is :"+str(Usecond)

UTot = Ufirst*(1-fins) + Usecond*fins
print "The total unit thermal coefficient is :"+str(UTot)
