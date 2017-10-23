# -*- coding: utf-8 -*-
import numpy as np
area=0.25 #for 1 m width and 0.25 (the wall's pattern) heigth
resistance_names = np.array(["in_convection","foam","plaster","plaster","out convection"]) # 5 elements
resistances_types = np.array(["conv","cond","cond","cond","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02, 0.02,None])
Resistances_RValues= np.array(np.zeros(5))
Resistances_RValues[resistances_types=="cond"] = resistances_L[resistances_types=="cond"]/ (resistances_k[resistances_types=="cond"]*area)
Resistances_RValues[resistances_types=="conv"] = 1.0 / resistances_h[resistances_types=="conv"] / area
rs=Resistances_RValues.sum()

res_names = np.array(["brick","plaster"])
res_types = np.array(["cond_par","cond_par"])
res_l=np.array([0.16,0.16])
res_areas= np.array([0.22,0.03]) #for unit area
res_k=  np.array([0.72,0.22])
Res_RValues= np.array(np.zeros(2))
Res_RValues[res_types=="cond_par"] = res_l[res_types=="cond_par"]/ (res_k[res_types=="cond_par"]*res_areas[res_types=="cond_par"])
Res_RValues=1.0/Res_RValues
rp=(Res_RValues.sum())**(-1)

Rtot=rs+rp

print "total resistance is "+str(Rtot)+" C/W, for a 0.25 m^2 area"
Area=3.0*5
deltaT=20-(-4.8)
print "for a "+ str(Area)+' m^2 wall and a deltaT of '+str(deltaT)+' °C the heat flow is '+str(deltaT*Area/Rtot/area)