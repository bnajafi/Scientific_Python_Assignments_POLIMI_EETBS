import os
os.chdir("/Users/Fede/Documents/Polimi/EETBS/Canopy")

import wallCalculation_Guermandi as FC

paral=["insulation", "wood stud"]
farea=[0.7, 0.3]
serie=["wood lapped", "wood sheeting", "gypsum wallboard", "100 mm common brick"]
roof = ["urethane rigid foam 50 mm", "100 mm common brick", "asphalt single roofing"]
door = ["door"]
U_wall = FC.wallCalc_withParallel(serie, paral, farea)
U_door = FC.wallCalc_onlyInSeries(door)
U_roof = FC.wallCalc_onlyInSeries(roof)

Area_walls=105.8
Area_Roof=200
Area_door=2.2
deltaT_heating=20-(-4.8)
Q_wall=U_wall*Area_walls*deltaT_heating
Q_roof=Area_Roof*U_roof*deltaT_heating
Q_door=Area_door*U_door*deltaT_heating
print('')
print('U of the wall is ')+str(U_wall)
print('Q disperded by wall is ')+str(Q_wall)
print('')
print('U of the roof is ')+str(U_roof)
print('Q disperded by roof is ')+str(Q_roof)
print('')
print('U of the door is ')+str(U_door)
print('Q disperded by door is ')+str(Q_door)
print('')