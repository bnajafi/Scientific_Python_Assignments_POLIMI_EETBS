Tin=20
Tout=-4.8
Adoor=2.2
Aroof=200
Uroof=0.25
Awindow=36
Adoor=2.2
Awall=144-Awindow-Adoor
import os
os.chdir("C:\PY")
import wallCalculations_Diaz as WC
layers_wall_S=["woodBevel","woodFiberboard_13mm","woodStud_90mm","gypsumWallboard_13mm","brick_100mm"]
layers_wall_I=["woodBevel","woodFiberboard_13mm","glassFiberInsulation_90mm","gypsumWallboard_13mm","brick_100mm"]
ratio_I=0.70
results=WC.wallCalc_withParallel(layers_wall_S,layers_wall_I,ratio_I)
U_overall=results["Total U of the wall"]
layers_G=["wood_50mm"]
results2=WC.wallCalc_onlyInSeries(layers_G)
Utot_G=results2["U"]
Qwall=Awall*(Tin-Tout)*U_overall
print(Qwall)
Qdoor=Adoor*(Tin-Tout)*Utot_G
print(Qdoor)
Qroof=Aroof*(Tin-Tout)*Uroof
print(Qroof)

Q_tot_heating=Qwall+Qdoor+Qroof
print ("The total heating Q is "+str(Q_tot_heating)+" W")