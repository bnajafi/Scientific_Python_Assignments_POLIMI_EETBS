# -*- coding: utf-8 -*-
#function that calculates the equivalent thermal resistance taking as an input a library of materials and a list of resistances in series

def wallCalc_onlyInSeries(library,ListInSeries,AirOnTwoSides):
    AllLayers=AirOnTwoSides+ListInSeries
    Rtot=0
    for anyvalue in AllLayers:
        Rtot=Rtot+library[anyvalue]
    Utot=1/Rtot
    return {"TotalThermalResistance":Rtot,"TotalUFactor":Utot}
    

def wallCalc_withParallel(Library,Series,Parallel,AirOnTwoSides,Fraction):
    AllLayers=AirOnTwoSides+Series+Parallel
    Rvalues=[]
    for anyres in AllLayers:
        Rvalues.append(Library[anyres])
    Rtot_values=[]
    for anylayer in Parallel:
        LayersComplete=AirOnTwoSides+Series
        LayersComplete.append(anylayer)
        Rtot=0
        for anyvalue in LayersComplete:
            #print"This layer is: "+anyvalue+" and its resistance is "+str(Library[anyvalue])+" [(m^2*°c)/W]\n"
            Rtot=Rtot+Library[anyvalue]
        Rtot_values.append(Rtot)
       # print"****************\n"
    U_overall=Fraction*1/Rtot_values[0]+(1-Fraction)*1/Rtot_values[1]
    R_overall=1/U_overall
    return {"TotalThermalResistance":R_overall,"TotalUFactor":U_overall}




 