def WallCalc(wallLayersSeries,wallLayersParallel,fractionInsulation,Matlib):
    ConvectionLayers=['InsideConv','outerConvWinter']
    totalSeriesRes=0.000
    for everyL in wallLayersSeries:
        if(everyL['length']==Matlib[everyL['material']]['length']):
            i=Matlib[everyL['material']]['R']
        else:
            i=(Matlib[everyL['material']]['R'])*(everyL['length'])/(Matlib[everyL['material']]['length'])
        totalSeriesRes+=i
    for a in ConvectionLayers:
        totalSeriesRes+=Matlib[a]['R']
    R=0.00
    z=0.00
    for every in wallLayersParallel:
        if(every['length']==Matlib[every['material']]['length']):
            j=Matlib[every['material']]['R']
        else:
            j=Matlib[every['material']]['R']*(every['length']/Matlib[every['material']]['length'])
        y=totalSeriesRes+j
        z=(1/(y))
        if(every['material']=='glassfiber'):
            R+=(fractionInsulation*z)
        else:
            R+=((1-fractionInsulation)*z)
    return R

def doorOderRoofcalc(ABC,Matlib):
    ConvectionLayers=['InsideConv','outerConvWinter']
    Res=0.00
    for a in ConvectionLayers:
        Res+=Matlib[a]['R']
    for everyL in ABC:
        if(everyL['length']==Matlib[everyL['material']]['length']):
            i=Matlib[everyL['material']]['R']
        else:
            i=Matlib[everyL['material']]['R']*(everyL['length']/Matlib[everyL['material']]['length'])
        Res+=i
    Value_U=(1.00/Res)
    return Value_U