# -*- coding: utf-8 -*-
import numpy as np
Hw = 3 # wall height in m 
Ww = 5 # wall width in m
Awall = Hw*Ww # wall area
Tamb1 = 20 # room temperature in ºC
Tamb2 = -10 # outside temperature in ºC

typepar=np.array(["plaster1","plaster2","brick"])
namespar=np.array(["cond","cond","cond"])
lengthspara=np.array([0.16,0.16,0.16])
kpara=np.array([0.22,0.22,0.72])
areapara=np.array([0.015,0.015,0.22])
Rpara=np.array(np.zeros(3))
Rpara=(kpara*areapara)/lengthspara
Rpara=1/Rpara.sum()


Aserie=0.25
typeseries=np.array(["foam","plaster","plaster","in","out"])
namesseries=np.array(["cond","cond","cond","conv","conv"])
lengthsseries=np.array([0.03,0.02,0.02,None,None])
kseries=np.array([0.026,0.22,0.22,None,None])
hseries=np.array([None,None,None,10,25])
Rseries=np.array(np.zeros(5))
Rseries[namesseries=="cond"] = lengthsseries[namesseries=="cond"]/ (kseries[namesseries=="cond"]*Aserie)
Rseries[namesseries=="conv"] = 1.0 / (hseries[namesseries=="conv"]*Aserie)
Rserietotal=Rseries.sum()

Rtotal=Rserietotal+Rpara

print "The total resistance is " + str(Rtotal) + " ºC/W"

Qu = (Tamb1 - Tamb2)/Rtotal # we calculate the heat flux in the unit in W

print "The heat flux in a unit is " + str(Qu) + " W"

#we scale the heat flux using the areas

Q = Qu * Awall/Aserie # in W
print "The total heat flux is " + str(Q) + " W"