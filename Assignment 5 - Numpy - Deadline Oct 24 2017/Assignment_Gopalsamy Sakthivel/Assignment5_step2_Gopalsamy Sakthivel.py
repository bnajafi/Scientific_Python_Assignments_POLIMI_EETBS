import numpy as np
materials_names= np.array(['outerConvWinter','outerConvSummer','InsideConv','woodbevel','fiberboard',
'glassfiber','woodstud','gypsum'])
materials_Rvalues =np.array([0.030,0.044,0.12,0.14,0.23,2.52,0.63,0.079])
wallLayersSeries=np.array(['InsideConv','woodbevel','fiberboard','gypsum','outerConvWinter'])
RValue_series = np.zeros(wallLayersSeries.size)
for layerName in wallLayersSeries:
    RValue_series[wallLayersSeries==layerName] = materials_Rvalues[materials_names==layerName]
RTotSeries=RValue_series.sum()
wallLayersParallel=np.array(['glassfiber','woodstud'])
wallLayersParallelFractions=np.array([0.75,0.25])
RValues = np.zeros(wallLayersParallel.size)
for layerName in wallLayersParallel:
    RValues[wallLayersParallel==layerName] = wallLayersParallelFractions[wallLayersParallel==layerName]/( RTotSeries+materials_Rvalues[materials_names==layerName])
RTot=RValues.sum()
print 'the overall U is '+str(RTot)+' W/m^2.degC'
U=RTot
tempDifference=24
Area=(0.8*50*2.5)
Q=U*Area*tempDifference
print 'the rate of heat transfer Q is '+str(Q)+' W'