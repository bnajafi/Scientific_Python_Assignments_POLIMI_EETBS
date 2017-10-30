# -*- coding: utf-8 -*-
#Building system assignment 3
#Edouard Thouvenin

import numpy as np

#Definition of the material library as a dictionnary

Rnames = np.array(['Outside_Surface_Winter','wood_25mm','Inside_Surface','Wood_Bevel',
    'Wood_Fiberboard','Glass_Fiber','Wood_Stud','Gypsum','cement'])
Rvalues = np.array([0.03, 0.22,0.12, 0.14,0.23,2.45,0.63,0.079, 0.018]) 
Rtype = np.array(["ser","useless","ser","ser","ser","para","para","ser","useless"])
arearatio = 0.75

R = Rvalues[Rtype =="ser"].sum() + Rvalues[Rtype =="para"]

Uoverall = arearatio / R[0] + (1 - arearatio) / R[1]

Roverall = 1/Uoverall


#Calculation of the global overall heat transfer and the global resistance


print "Here is the value of the global overall heat transfer Uoverall: " + str(Uoverall) + "W/m2°C"

print "Here is the value of the global overall Resistance Roverall: " + str(Roverall) + "m2°C/W"

