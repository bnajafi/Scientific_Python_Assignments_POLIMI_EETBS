import os
os.chdir("/Users/tomassanchez/Desktop/files to send")
import wallCalculations_Sanchez as WC

    
layers_roof=["faceBreak_100mm",'AsphaltRoofing']
layers_door=["woodFiberboard_13mm",'WoodBevel']
layers_wallseries = ["GypsumBoard",'CommonBrick',"woodFiberboard_13mm"]
layers_wallparallel=['GlassFiber','woodStud']
Udoor=1/WC.wallCalc_onlyinSeries(layers_door)
Uroof=1/WC.wallCalc_onlyinSeries(layers_roof)
Uwall =1/WC.wallCalc_withParallel(layers_wallseries,layers_wallparallel)

Delta_T=26.2

HFwall=Delta_T*Uwall
HFroof=Delta_T*Uroof
HFdoor=Delta_T*Udoor

Awall=2.4*2*(10+20)
Aroof=200
Adoor=2.2

qwall=Awall*HFwall
qroof=Aroof*HFroof
qdoor=Adoor*HFdoor

print "the wall Q is "+ str(qwall)
print "the roof Q is "+ str(qroof)
print "the door Q is "+ str(qdoor)