# -*- coding: utf-8 -*-
#assignment4_step1_wallCalculation_Temporelli (only winter)

def wallCalc_withParallel(ListSeries,ListParallel,float1):
    Materials={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
    "InsideSurface":0.12,"OutsideSurfaceWinter":0.03, "CommonBrick":0.12}
    
    R_series=0
    
    for anyLayer in ListSeries:
        R_anyLayer=Materials[anyLayer]
        R_series=R_series+R_anyLayer
    
    Rtot=[]
    
    for i in ListParallel:
        List=ListSeries.append(i)
        R=R_series+Materials[i]
        Rtot=Rtot+[R]
    U_ins=Rtot[0]**-1
    U_wood=Rtot[1]**-1
    U_overall=(1/Rtot[0]*float1)+(1/Rtot[1]*(1-float1))
    result=U_overall
    return result

def wallCalc_onlyInSeries(ListSeries):
    Materials={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
    "InsideSurface":0.12,"OutsideSurfaceWinter":0.03,"WoodDoor":0.44, "Roof":4.00}
    R_series=0
    for anyLayer in ListSeries:
        R_anyLayer=Materials[anyLayer]
        R_series=R_series+R_anyLayer
    U_series=1/R_series
        
    result=U_series
    return result

#test

#ListOfSeriesLayersWall=["InsideSurface","WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard","OutsideSurfaceWinter","CommonBrick"]
#ListOfParallelLayers=["GlassFiberInsulation","Woodstud"]
#ListOfSeriesDoor=["InsideSurface","WoodDoor","OutsideSurfaceWinter"]
#ListOfSeriesRoof=["Roof"]
#area_fraction_ins = 0.70

#result_this=wallCalc_withParallel(ListOfSeriesLayersWall,ListOfParallelLayers,area_fraction_ins) 
#print ("Results: "+str(result_this))
#result_that=wallCalc_onlyInSeries(ListOfSeriesDoor)
#print ("Results: "+str(result_that))
#result_thisthat=wallCalc_onlyInSeries(ListOfSeriesRoof)
#print ("Results: "+str(result_thisthat))