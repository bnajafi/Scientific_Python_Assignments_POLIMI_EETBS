# -*- coding: utf-8 -*-
import numpy as np

resistance_names = np.array(['Inside_surface''Wood_bevel_lapped','Wood_fiberboard','Glass_fiber','Wood_stud',
'Gypsum','Outside_sourface',])
resistances_types_at_studs=np.array(['at_studs','at_studs','at_studs',None,'at_studs',
'at_studs','at_studs',])
resistances_types_between_studs=np.array(['between_studs','between_studs','between_studs','between_studs',None,
'between_studs','between_studs',])

farea=0.75

resistance_R = np.array([0.12,0.14,0.23,2.45,0.63,0.079,0.03])

#Calculating for wood stud
Resistances_RValues_at_studs= np.array(np.zeros(7))
Resistances_RValues_at_studs[resistances_types_at_studs=="at_studs"]=resistance_R[resistances_types_at_studs=="at_studs"]
Resistances_Rtot_at_studs=Resistances_RValues_at_studs.sum()
print 'The total value of R assuming a wall with stud is ' +str(Resistances_Rtot_at_studs) +' °C/W'
print ' '

#Calculating for glass fiber
Resistances_RValues_between_studs= np.array(np.zeros(7))
Resistances_RValues_between_studs[resistances_types_between_studs=="between_studs"]=resistance_R[resistances_types_between_studs=="between_studs"]
Resistances_Rtot_between_studs=Resistances_RValues_between_studs.sum()
print 'The total value of R assuming a wall with stud is ' +str(Resistances_Rtot_between_studs) +' °C/W'
print ' '

#HEAT TRANSFER COEFFICIENT

U_stud= (1-farea)/Resistances_Rtot_at_studs
U_glass= farea/Resistances_Rtot_between_studs
U_tot= U_glass+U_stud

print 'The overall heat transfer coefficient is ' +str(U_tot) +' W/°C'
R_tot=1/U_tot
print ' '
print 'The total resistence is ' +str(R_tot) +' °C/W'