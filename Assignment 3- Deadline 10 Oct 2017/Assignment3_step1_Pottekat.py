Mat_Lib={'outerConvWinter':{'R':0.030},'outerConvSummer':{'R':0.044},'InsideConv':{'R':0.12},
'wood_bevel':{'length':(13*200),'R':0.14},'fiber_board':{'length':(13),'R':0.23},
'glass_fiber':{'length':(25),'R':0.70},'wood_stud':{'length':(90),'R':0.63},
'gypsum':{'length':(13),'R':0.079}}
wallLayersSeries=[{'material':'wood_bevel','length':(13*200)},{'material':'fiber_board','length':13},
{'material':'gypsum','length':13},]
wallLayersParallel=[{'material':'glass_fiber','length':90.00},{'material':'wood_stud','length':90}]
fractionInsulation=0.75
tempDifference=24
Area=(0.8*50*2.5)
ConvectionLayers=['InsideConv','outerConvWinter']
totalSeriesRes=0.000
for everyL in wallLayersSeries:
    if(everyL['length']==Mat_Lib[everyL['material']]['length']):
        i=Mat_Lib[everyL['material']]['R']
    else:
        i=Mat_Lib[everyL['material']]['R']*(everyL['length']/Mat_Lib[everyL['material']]['length'])
    print i
    totalSeriesRes+=i
for a in ConvectionLayers:
    print Mat_Lib[a]['R']
    totalSeriesRes+=Mat_Lib[a]['R']
R=0.00
z=0.00
for every in wallLayersParallel:
    if(every['length']==Mat_Lib[every['material']]['length']):
        j=Mat_Lib[every['material']]['R']
    else:
        j=Mat_Lib[every['material']]['R']*(every['length']/Mat_Lib[every['material']]['length'])
    print j
    z=(1/(totalSeriesRes+j))
    if(every['material']=='glass_fiber'):
        R+=(fractionInsulation*z)
    else:
        R+=((1-fractionInsulation)*z)
print 'the overall U is '+str(R)+' W/m^2.degC'
U=R
Q=U*Area*tempDifference
print 'the rate of heat transfer Q is '+str(Q)+' W'