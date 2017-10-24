# -*- coding: utf-8 -*-
#mainScript
#importare calc

#wallcalculations 
wallcomposition={"Gypsumwallboard":{"L":0.013,"R":0.079},
"Glassfiberinsulation":{"L":0.090,"R":2.45},
"CommonBrick":{"L":0.10, "R": 0.12} ,
"Woodfiberboard":{"L":0.013,"R":0.23} ,
"Woodbevellappedsiding":{"L":0.20, "R": 0.14},
"woodstud":{"L":0.090,"R": 0.63},
"Wood":{"L":0.050,"R":0.44},
"out":{"R":0.03},
"in":{"R":0.12}}

U_door=U_wall=0
Hbuilding=2.4 #m
Aroof=20*10 #m2
Adoor=1*2.2 #m2
Awalls=2.4*30*2-3*4*1.8-8*1.8-2.2
U_roof=0.25 #W/(m2*K)
deltaT_heating=20-(-4.8)  #°C
#deltaT_cooling=31.9-24 °C
DR=11.9 #°C
print (wallcomposition, "**")
listA= ["out","in","Gypsumwallboard","CommonBrick","Woodfiberboard","Woodbevellappedsiding"]
listB= ["Glassfiberinsulation","Woodstud"]
listseriedoor=["Wood","out","int"]

import os
os.chdir ("/Users/camillatagliabue/Desktop/Scientific_Python_Assignments_POLIMI_EETBS/Assignment 4 - Deadline 17 oct 2017")
import wallCalculations_CamillaTagliabue as WC
WC.wallCalc_onlyInSeries(listseriedoor,wallcomposition)
WC.wallCalc_withParallel (listA,listB,wallcomposition)
#WC.wallCalc_withParallel(listseriewall,listparallel,wallcomposition)

U_door=WC.wallCalc_onlyInSeries (listseriedoor,wallcomposition)
U_wall=WC.wallCalc_withParallel (listA,listB,wallcomposition)
print (U_door)
print (U_wall)

HFdoor=U_door*deltaT_heating
HFwalls=U_wall*deltaT_heating

Qtotal=HFdoor*Adoor+HFwalls*Awalls+Aroof*U_roof

#HF=U*deltaT_heating 