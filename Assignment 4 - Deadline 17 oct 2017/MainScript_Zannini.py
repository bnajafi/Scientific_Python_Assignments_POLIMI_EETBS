
import os
os.chdir("/Users/giordanozannini/gitfork/Assignment4")
import WallCalculation_Zannini as FC


DTwinter=24.8
Udoor=FC.CalcWallSeries(["Wood","outsideSurfWinter","insideSurf"],[50,1,1])
Uroof=FC.CalcWallSeries(["Wood","FoamInsulation","GypsumBoard","AsphaltRoofing","outsideSurfWinter","insideSurf"],[100,80,2,1,1,1])
Walldata= FC.CalcUtotWall(["WoodBevelLappedSidings","WoodFiberboardSheeting_13mm","GypsumBoard","insideSurf","outsideSurfWinter","CommonBrick_100mm"],
["WoodStud","GlassFiber_90mm"],0.75)  #the output of the function is a dictonary 
Uwall=Walldata["Overall heat transfert coeff"] #it takes only the value of Uwall from the dictonary
#areas in m^2
A_wall=105.8
A_ceiling=200
A_door=2.2

Qdoor=A_door*Udoor*DTwinter
Qroof=A_ceiling*Uroof*DTwinter
Qwall=A_wall*Uwall*DTwinter

print "**********************************"
print "The heating load of the wall is: "+str(Qwall)+" W"
print "The heating load of the roof is: "+str(Qroof)+" W"
print "The heating load of the door is: "+str(Qdoor)+" W"