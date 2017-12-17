# -*- coding: utf-8 -*-
import numpy as np

def wallCalc_withParallel(layers,resistances, types, AreaRatioInsulation):
    
    Rseries = resistances[types == "series"].sum()
    Rvalue = resistances[types == "parallel"] + Rseries
    
    U=1/Rvalue
    
    Uoverall=AreaRatioInsulation*U[0]+(1-AreaRatioInsulation)*U[1]
    
    print "The total heat transfer coefficient of the wall is " + str(Uoverall) + " W/m2°C"
    
    Qwall = Uoverall * 100 * (22-(-2))
    print "The total heat flux across the wall is " + str(Qwall) + " W"

    return Uoverall


def wallCalc_onlyInSeries(resistances_opaque):
    
    U = 1/(resistances_opaque.sum())
    print "The trasmittance of the opac element is " + str(U) +" W/m2 °C"
    return U


#layers = np.array(["gypsum_13mm", "common_brick", "glass_fiber_90mm", "wood_stud", "wood_fiberboard",  "wood_bevel", "inside_surface", "otside_surface"])
#resistances = np.array([0.079, 0.12, 2.52, 0.63, 0.23, 0.14, 0.12, 0.03])
#types = np.array(["series","series","parallel","parallel","series","series","series","series"])
#layers_opaque = np.array([ "wood_25mm", "inside_surface","outside_surface"])
#resistances_opaque = np.array([0.44, 0.12, 0.03])
#AreaRatioInsulation = 0.70

#wallCalc_withParallel(layers,resistances, types, AreaRatioInsulation) 
#wallCalc_onlyInSeries(resistances_opaque)