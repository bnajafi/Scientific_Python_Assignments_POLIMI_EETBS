import numpy as np


resistance_names_s = np.array(["R1","R2","R3","R4","R5"])
resistances_types_s = np.array(["conv","cond","cond","cond","conv"])
resistances_h_s = np.array([10,None,None,None,25])
resistances_k_s=  np.array([None,0.026,0.22,0.22,None])
resistances_L_s= np.array([None,0.03,0.02,0.02,None])
Resistances_RValues_s= np.array(np.zeros(5))
Resistances_RValues_s[resistances_types_s=="cond"] = resistances_L_s[resistances_types_s=="cond"]/ resistances_k_s[resistances_types_s=="cond"]
Resistances_RValues_s[resistances_types_s=="conv"] = 1.0 / resistances_h_s[resistances_types_s=="conv"]
Resistances_Rtot1=Resistances_RValues_s.sum()
Resistances_Rtot_s=Resistances_Rtot1/0.25


resistance_names_p= np.array(["R6","R7", "R8"])
resistances_types_p=np.array(["cond","cond","cond",])
resistances_k_p=np.array([0.22,0.72,0.22])
resistances_L_p= np.array([0.16,0.16,0.16])
resistances_A_p= np.array([0.015,0.22,0.015])
Resistance_RValues_p=np.array(np.zeros(3))
Resistance_RValues_p[resistances_types_p=="cond"]=resistances_k_p[resistances_types_p=="cond"]*resistances_A_p[resistances_types_p=="cond"]/ resistances_L_p[resistances_types_p=="cond"]
Resistances_Rtot2=Resistance_RValues_p.sum()
Resistances_Rtot_p=1.0/Resistances_Rtot2

Resistances_Rtot=Resistances_Rtot_s+Resistances_Rtot_p

T1=20
T2=-10
A_wall=15

Qtot=( (T1-T2)*A_wall)/(Resistances_Rtot*0.25)
print "the total heat tranfer through the wall is " +str(Qtot)+ "W"




