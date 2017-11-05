def WallCalc(wallLayersSeries,wallLayersParallel,fractionInsulation,Matlib):
    ConvectionLayers=['InsideConv','outerConvWinter']
    Result=[]
    totalSeriesRes=0.000
    for everyL in wallLayersSeries:
        if(everyL['length']==Material_Library[everyL['material']]['length']):
            i=Material_Library[everyL['material']]['R']
        else:
            i=Material_Library[everyL['material']]['R']*(everyL['length']/Material_Library[everyL['material']]['length'])
        Result.append({everyL['material']:i})
        totalSeriesRes+=i
    for a in ConvectionLayers:
        Result.append({a:Material_Library[a]['R']})
        totalSeriesRes+=Material_Library[a]['R']
    R=0.00
    z=0.00
    for every in wallLayersParallel:
        if(every['length']==Material_Library[every['material']]['length']):
            j=Material_Library[every['material']]['R']
        else:
            j=Material_Library[every['material']]['R']*(every['length']/Material_Library[every['material']]['length'])
        Result.append({every['material']:j})
        y=totalSeriesRes+j
        Result.append({'totalR with only '+str(every['material']):y})
        z=(1/(y))
        if(every['material']=='glassfiber'):
            R+=(fractionInsulation*z)
        else:
            R+=((1-fractionInsulation)*z)
    Result.append({'the overall U':R})
    return Result
Material_Library={'outerConvWinter':{'R':0.030},'outerConvSummer':{'R':0.044},'InsideConv':{'R':0.12},
'woodbevel':{'length':(13*200),'R':0.14},'fiberboard':{'length':(13),'R':0.23},
'glassfiber':{'length':(25),'R':0.70},'woodstud':{'length':(90),'R':0.63},
'gypsum':{'length':(13),'R':0.079}}
wallLayersSeries=[{'material':'woodbevel','length':(13*200)},{'material':'fiberboard','length':13},
{'material':'gypsum','length':13},]
wallLayersParallel=[{'material':'glassfiber','length':90.00},{'material':'woodstud','length':90}]
fractionInsulation=0.75
tempDifference=24
Area=(0.8*50*2.5)
CALCULATION=WallCalc(wallLayersSeries,wallLayersParallel,fractionInsulation,Material_Library)
print 'the function returns this following list of results'
print CALCULATION
U=CALCULATION[-1]['the overall U']
Q=U*Area*tempDifference
print 'the rate of heat transfer Q is '+str(Q)+' W'