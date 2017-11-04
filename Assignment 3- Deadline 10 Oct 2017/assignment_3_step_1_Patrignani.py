# -*- coding: utf-8 -*-
material_library = {"wood_bevel":0.14, "wood_fiberboard_13mm":0.23, "glass_fiber_90mm":2.45, "wood_stud":0.63, "gypsum_13mm":0.079, "inside_surface":0.12, "otside_surface":0.03}

ListOfLayersInSeries = ["wood_bevel", "wood_fiberboard_13mm", "gypsum_13mm", "inside_surface", "otside_surface"]
ListOfLayersInParallel = ["glass_fiber_90mm", "wood_stud"]
AreaRatioInsulation = 0.75


for anylayer in ListOfLayersInParallel:
    Rparallel=material_library[anylayer]
    Rseries = 0
    Rvalue = []
    for anylayer1 in ListOfLayersInSeries:
        Rvalue = material_library[anylayer1]
        Rseries = Rseries + Rvalue
    RAtStuds = Rseries + Rparallel #material_library["wood_stud"]
RBetweenStuds = Rseries  + Rparallel   #material_library["glass_fiber_90mm"]    
print "The in series resistence between the studs is "+str(RBetweenStuds)+" m2°C/W"
print "The in series resistance at the studs is " + str(RAtStuds) + " m2°C/W"


Uins = 1/RBetweenStuds
Uwood = 1/RAtStuds


Uoverall=Uins * AreaRatioInsulation + Uwood*(1-AreaRatioInsulation)
print "The total heat transfer coefficient of the wall is " + str(Uoverall) + " W/m2°C"


Qwall = Uoverall * 100 * (22-(-2))
print "The total heat flux across the wall is " + str(Qwall) + " W"