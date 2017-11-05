# -*- coding: utf-8 -*-
#assignment 3 - step 2

Material_library={"WoodBevel":0.14,"WoodFiberboard_13mm":0.23,"GlassFiberIns_90mm":2.45,
"WoodStud_38x90mm2":0.63,"GypsumWallboard_13mm":0.079,"CommonBrick_100mm":0.12,"AcousticTile":0.32,
"BuildingPaper":0.011,"Plywood_13mm":0.11,"OutsideSurface":0.030,"InsideSurface":0.12}

LayersInsSeries=["WoodBevel","WoodFiberboard_13mm","GypsumWallboard_13mm"]
LayersParallel=["GlassFiberIns_90mm","WoodStud_38x90mm2"]

AreaFraction=0.75

def wall_calc(Library,Series,Parallel,Fraction):
    AirOnTwoSides=["InsideSurface","OutsideSurface"]
    AllLayers=AirOnTwoSides+Series+Parallel
    Rvalues=[]
    for anyres in AllLayers:
        Rvalues.append(Material_library[anyres])
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
    U_overall=AreaFraction*1/Rtot_values[0]+(1-AreaFraction)*1/Rtot_values[1]
    R_overall=1/U_overall
    return {"Thermal resistance of all layers":Rvalues,"TotalThermalResistance":R_overall,"TotalUFactor":U_overall}

result=wall_calc(Material_library,LayersInsSeries,LayersParallel,AreaFraction)
print "The overall U factor of the wall is: "+str(result["TotalUFactor"])+" [W/(m^2*°c)]"
print "The overall thermal resistance of the wall is: "+str(result["TotalThermalResistance"])+" [(m^2*°c)/W]"
Area=0.8*50*2.5
Tin=22
Tout=-2
Qwall=result["TotalUFactor"]*Area*(Tin-Tout)
print"The rate of heat loss through the walls of the house is: "+str(Qwall)+" [W]"