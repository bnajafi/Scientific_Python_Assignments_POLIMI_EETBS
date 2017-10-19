import os

os.chdir ("C:\Users//alice\Dropbox\Python4ScientificComputing_Fundamentals\Assignment 4")

import wallCalculations_Bortolotti as wC

Layers_Wall_series = ["WoodBevelLapperSiding_13mm*200mm","GypsumWallBoard_13mm","CommonBrick_100m","WoodFiberBoard_13mm"]
    
Layers_Wall_par = ["GlassFiberInsultation_90mm","WoodStud_38mm*90mm"]

Layer_Door = ["Wood_50mm"]

Layer_Roof = ["GlassFiberInsultation_90mm","WoodStud_38mm*90mm","WoodFiberInsulation_13mm"]

U_Roof = 0.25

Results_Wall = wC.wallCalc_withParallel(Layers_Wall_series,Layers_Wall_par,0.7)
Results_Door = wC.wallCalc_onlyInSeries(Layer_Door)
#Results_Roof = wC.wallCalc_onlyInSeries(Layers_Roof) U_roof is given by the example

U_Wall = Results_Wall["U_overall"]
U_Door = Results_Door["Utot_series"]
#U_Roof = Results_Roof["Utot_series"]

print "the U value of the Wall is " + str(U_Wall)
print "the U value of the Door is " + str(U_Door)
print "the U value of the Roof is " + str(0.25)

Tin_winter = 20
Tout_winter = -4.8
DeltaT_Heating = Tin_winter - Tout_winter


A_Wall = 105.8
A_Door = 2.4
A_Roof = 200

Q_Wall = U_Wall*DeltaT_Heating*A_Wall
Q_Door = U_Door*DeltaT_Heating*A_Door
Q_Roof = U_Roof*DeltaT_Heating*A_Roof

Q_tot = Q_Wall + Q_Door + Q_Roof

print "the total heat load from the opaque surfaces is " + str(Q_tot) + "W"