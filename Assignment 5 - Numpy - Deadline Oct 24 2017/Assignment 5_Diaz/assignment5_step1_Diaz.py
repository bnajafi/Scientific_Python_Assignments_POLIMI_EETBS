import numpy as np

resistances_series_names=np.array(["R1","R2","R3","R4","R5"])
resistances_series_type=np.array(["conv","cond","cond","cond","conv"])
resistances_series_L=np.array([None,0.03,0.02,0.02,None])
resistances_series_k=np.array([None,0.026,0.22,0.22,None])
resistances_series_h=np.array([10,None,None,None,25])
area_series=0.25
RValues_S=np.array(np.zeros(5))
RValues_S[resistances_series_type=="conv"]=1.0/(area_series*resistances_series_h[resistances_series_type=="conv"])
RValues_S[resistances_series_type=="cond"]=resistances_series_L[resistances_series_type=="cond"]/(area_series*resistances_series_k[resistances_series_type=="cond"])

Rtot_Series=RValues_S.sum()



resistances_parallel_names=np.array(["R6","R7","R8"])
resistances_parallel_type=np.array(["cond","cond","cond"])
L_parallel=0.16
resistances_parallel_k=np.array([0.22,0.72,0.22])
area_parallel=np.array([0.015,0.22,0.015])
RValues_P=np.array(np.zeros(3))
RValues_P=1/(L_parallel/(area_parallel[resistances_parallel_type=="cond"]*resistances_parallel_k[resistances_parallel_type=="cond"]))
Rtot_Parallel=1/RValues_P.sum()



Rtot_System=Rtot_Series+Rtot_Parallel


print("The total resistance of the system is "+ str(Rtot_System)+" m^2C/W")

heightw=3
widthw=5
Tin=20
Tout=-10
Awall=heightw*widthw
Aunit=0.25*1


Qunit=(Tin-Tout)/Rtot_System


Qtot=Qunit*(Awall/Aunit)

print("\n")
print (  "The rate of heat transfer through the wall is  " + str (Qtot)+ " W" )
