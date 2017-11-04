import numpy as np

import os
os.chdir("C:\Users\LENOVO\Desktop\Codes\New folder")

import assignment5_4_wallCalculatio as WC
#WallCalculations
jointLayer=np.array(["outsidesurface","gypsumwallboard","woodfiber","woodbevellapped","insidesurface","commonbrick"])
jointR=np.array([0.03,0.079,0.23,0.14,0.12,0.12])
parLayer=np.array(["glassfiberinsulation","woodstud"])
parR=np.array([0.7*90/25,0.63])
ratio=0.7
UtotWall=WC.wallCalc_withParallel(jointLayer,jointR,parLayer,parR,ratio)
roofLayer=np.array(["insidesurface","outsidesurface","woodfiber","asphalt","glassfiberinsulation","gypsumwallboard","wood"])
roofR=np.array([0.12,0.03,0.23,0.077,0.7,0.079,0.22*2])
doorLayer=np.array(["insidesurface","outsidesurface","wood"])
doorR=np.array([0.12,0.03,0.22*2])
UtotRoof=WC.wallCalc_onlyInSeries(roofR)
UtotDoor=WC.wallCalc_onlyInSeries(doorR)

deltaT,area_wall,area_roof,area_door=20+4.8,105.8,200,2.2
print ("The Heating Load of the Walls is "+str(UtotWall*deltaT*area_wall)+" W")
print ("The Heating Load of the Door is "+str(UtotDoor*deltaT*area_door)+" W")
print ("The Heating Load of the Roof is "+str(UtotRoof*area_roof*deltaT)+" W")



