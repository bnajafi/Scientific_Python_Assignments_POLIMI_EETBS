import numpy as np
resistance_names = np.array(["R1","R2","R3","R4","R5"])
resistances_types = np.array(["conv","condseries","condseries","condseries","conv"])
resistances_h = np.array([10,None,None,None,25])
resistances_k=  np.array([None,0.026,0.22,0.22,None])
resistances_L= np.array([None,0.03,0.02,0.02,None])
resistances_A= np.array([0.25,0.25,0.25,0.25,0.25])
Resistances_RValueseries= np.array(np.zeros(5))
Resistances_RValueseries[resistances_types=="condseries"] = resistances_L[resistances_types=="condseries"]/(( resistances_k[resistances_types=="condseries"])*(resistances_A[resistances_types=="condseries"]))
Resistances_RValueseries[resistances_types=="conv"] = 1.0 /( resistances_h[resistances_types=="conv"]*resistances_A[resistances_types=="conv"])
Resistances_Rtotseries=Resistances_RValueseries.sum()
resistance_namesparallel = np.array(["R6","R7","R8"])
resistances_typesparallel = np.array(["condparallel","condparallel","condparallel"])
resistances_k_parallel=  np.array([0.22,0.22,0.72])
resistances_L_parallel= np.array([0.16,0.16,0.16])
resistances_A_parallel= np.array([0.015,0.015,0.22])
Resistances_RValues_parallel= np.array(np.zeros(3))
Resistances_RValues_parallel= 1/(resistances_L_parallel/( resistances_k_parallel*resistances_A_parallel))
Resistances_Rtot_parallel=1/(Resistances_RValues_parallel.sum())
Resistancestotal=Resistances_Rtot_parallel+Resistances_Rtotseries
area_total=3*5 #m^2
area_unit=0.25*1 #m^2
t_in=20 #C temperature inside the room
t_out=-10 #C temperature outside the room
Q_unit=(t_in-t_out)/Resistancestotal
Q_wall=Q_unit*(area_total/area_unit)
print 'the value of total resistance of the unit is'+' '+str(Resistancestotal)+' '+'C/W'
print 'the heat transfer rate of the unit'+' '+str(Q_unit)+' '+'W'
print 'the heat transfer rate of the wall'+' '+str(Q_wall)+' '+'W'