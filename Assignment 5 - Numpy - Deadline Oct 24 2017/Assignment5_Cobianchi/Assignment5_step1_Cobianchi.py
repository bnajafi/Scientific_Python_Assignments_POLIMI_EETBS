#import numpy library
import numpy as np

#define a dictionary of components
#Components = {"R_Inside":{"Unit_Area":0.25,"Convective_Coefficient":10},
#             "R_Foam":{"Unit_Area":0.25,"Length":0.03,"Thermal_Coefficient":0.026},
#              "R_Plaster": {"Unit_Area":0.25,"Length":0.02,"Thermal_Coefficient":0.22},
#              "R_Brick": {"Unit_Area":0.22,"Length":0.16,"Thermal_Coefficient":0.72},
#              "R_Outside": {"Unit_Area":0.25,"Convective_Coefficient":25}}#

Unit_Area = 0.25
Unit_Area_Brick = 0.22
Unit_Area_parallel = 0.015

#Define total resistance in series 
R_serie = np.array(["R_Inside","R_Foam","R_Plaster1","R_Plaster2","R_Outside"])
R_type1 = np.array(["conv","cond","cond","cond","conv"])
h = np.array([10,None,None,None,25])
k = np.array([None,0.026,0.22,0.22,None])
L = np.array([None,0.03,0.02,0.02,None])
Resistances_RValues1 = np.array(np.zeros(5))
Resistances_RValues1[R_type1 == "cond"] = L[R_type1 == "cond"]/ ((k[R_type1 == "cond"]) * Unit_Area)
Resistances_RValues1[R_type1 == "conv"] = 1.0 / ((h[R_type1 == "conv"]) * Unit_Area)
Resistances_Rtot1 = round(Resistances_RValues1.sum(),3)

#Define total resistance in parallel
R_name = np.array(["R_Plaster2","R_Brick","R_Plaster2"])
R_type2 = np.array(["cond","cond1","cond"])
k = np.array([0.22,0.72,0.22])
L = np.array([0.16,0.16,0.16])
Resistances_RValues2 = np.array(np.zeros(3))
Resistances_RValues2[R_type2 == "cond"] = 1/(L[R_type2 == "cond"]/ (k[R_type2 == "cond"]*Unit_Area_parallel))
Resistances_RValues2[R_type2 == "cond1"] = 1/(L[R_type2 == "cond1"]/ (k[R_type2 == "cond1"]*Unit_Area_Brick))
Resistances_Rtot2 = (round(Resistances_RValues2.sum(),3))

print ("The total resistence is: ")+str(Resistances_Rtot1+Resistances_Rtot2)