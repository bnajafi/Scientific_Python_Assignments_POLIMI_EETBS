# -*- coding: utf-8 -*-
"""
CASALICCHIO VALERIA 10424146
"""
import numpy as np 

Names = np.array(["Outside_Surface_Winter","Inside_Surface","Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting",
                                                                "Glass_Fiber_Insulation","Wood_Stud","Gypsum_Wallboard"])
Resist = np.array([0.030,0.12,0.14,0.23,2.45,0.63,0.079])

Order = np.array(["series","series","series","series","parallel","parallel","series"])

Ratio_Insulation=float(0.75) 

Tot_R_Series = np.array(Resist[Order == "series"]).sum()

R_Parallel = np.array(Resist[Order == "parallel"])

Partial_R_Wall_Unit = R_Parallel+Tot_R_Series

Tot_R=Ratio_Insulation*(Partial_R_Wall_Unit[0])+(1-Ratio_Insulation)*(Partial_R_Wall_Unit[1])
Tot_U=1/Tot_R


print "\n***********************************************************************\n"
print " GLOBAL HEAT TRANSFER COEFFICIENT = "+str(round(Tot_U,4))+" [W/m2°C]"   
print " \n TOTAL THERMAL RESISTANCE = "+str(round(Tot_R,4))+" [m2°C/W]"   
print "\n***********************************************************************\n"
