M={'outerConvWinter':{'R':0.030},'outerConvSummer':{'R':0.044},'InsideConv':{'R':0.12},
'woodbevel':{'length':(13*200),'R':0.14},'fiberboard':{'length':(13),'R':0.23},
'glassfiber':{'length':(25),'R':0.70},'woodstud':{'length':(90),'R':0.63},
'gypsum':{'length':(13),'R':0.079},'commonbrick':{'length':(100),'R':0.12},'wood':{'length':(25),'R':0.22},
'concrete':{'length':(200),'R':1.9},'plaster':{'length':(13),'R':0.079}}
wallLayersSeries=[{'material':'woodbevel','length':(13*200)},{'material':'fiberboard','length':13},
{'material':'gypsum','length':13},{'material':'commonbrick','length':100}]
doorlayers=[{'material':'wood','length':(50)}]
rooflayers=[{'material':'concrete','length':500},{'material':'plaster','length':30}]
wallLayersParallel=[{'material':'glassfiber','length':90.00},{'material':'woodstud','length':90}]
fractionInsulation=0.70
tempDifference=24.8
Area_Walls=105.8
Area_Door=2.2
Area_Roof=200.00000
import wallCalculations_GopalsamySakthivel as FC
CALCULATION=FC.WallCalc(wallLayersSeries,wallLayersParallel,fractionInsulation,M)
Q_walls=CALCULATION*Area_Walls*tempDifference
Q_door=(FC.doorOderRoofcalc(doorlayers,M))*Area_Door*tempDifference
Q_roof=(FC.doorOderRoofcalc(rooflayers,M))*Area_Roof*tempDifference
Qtotal=Q_walls+Q_door+Q_roof
print Qtotal