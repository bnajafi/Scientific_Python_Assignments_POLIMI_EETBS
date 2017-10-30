# -*- coding: utf-8 -*-
import numpy as np

def wall_calculator(layers,resistances, types, AreaRatioInsulation):
    Rseries = resistances[types == "series"].sum()
    Rvalue = resistances[types == "parallel"] + Rseries
    
    U=1/Rvalue
    
    Uoverall=AreaRatioInsulation*U[0]+(1-AreaRatioInsulation)*U[1]
    
    print "The total heat transfer coefficient of the wall is " + str(Uoverall) + " W/m2°C"
    
    Qwall = Uoverall * 100 * (22-(-2))
    print "The total heat flux across the wall is " + str(Qwall) + " W"

    return


layers = np.array(["wood_bevel", "wood_fiberboard_13mm", "glass_fiber_90mm", "wood_stud", "gypsum_13mm", "inside_surface", "otside_surface"])
resistances = np.array([0.14, 0.23, 2.45, 0.63, 0.079, 0.12, 0.03])
types = np.array(["series","series","parallel","parallel","series","series","series"])
AreaRatioInsulation = 0.75

wall_calculator(layers,resistances, types, AreaRatioInsulation)