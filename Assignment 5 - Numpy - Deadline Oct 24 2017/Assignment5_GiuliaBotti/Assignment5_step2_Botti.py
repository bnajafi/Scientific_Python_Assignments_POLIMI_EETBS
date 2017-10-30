# -*- coding: utf-8 -*-
import numpy as np
Resistances_names = np.array(["Outside_surface","Inside_surface","Glass_fiber","Wood_stud","Wood_bevel_lapped","Wood_fiberboard","Gypsum_wallboard"])
Resistances_values = np.array([0.030,0.12,2.45,0.63,0.14,0.23,0.079])
Area_Fraction = np.array([0.75,0.25])
WallPar_names = Resistances_names[np.array([False,False,True,True,False,False,False])]
WallPar_values = Resistances_values[np.array([False,False,True,True,False,False,False])]
print "The resistances in parallel are "+str(WallPar_names)+" m^2*°C/W"
WallSer_names = Resistances_names[np.array([False,False,False,False,True,True,True])]
WallSer_values = Resistances_values[np.array([False,False,False,False,True,True,True])]
print "The resistances in series are "+str(WallSer_names)+" m^2*°C/W"
Air_names = Resistances_names[np.array([True,True,False,False,False,False,False])]
Air_values = Resistances_values[np.array([True,True,False,False,False,False,False])]
print "The air resistances are "+str(Air_names)+" m^2*°C/W"
#Calculating total resistance
R_Series_tot = WallSer_values.sum()
R_Air_tot = Air_values.sum()
R_section = R_Series_tot+R_Air_tot+WallPar_values
U_section = 1/R_section
U_overall = U_section*Area_Fraction
R_overall = 1/U_overall.sum()
print "The total calculated resistance is "+str(R_overall)+" m^2*°C/W"
T1 = 22
T2 = -2
A = 100
Q_wall = A*(T1-T2)/R_overall
print "The total heat flux through the wall is "+str(Q_wall)+" W"