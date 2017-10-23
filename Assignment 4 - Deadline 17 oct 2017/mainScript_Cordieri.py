import sys
import os
ThisfileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisfileDirectory)
print os.getcwd()
import wall_Calculations_Cordieri as wcc
WallLayersSeries=["WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard","CommonBrick"]
WallLayersParallel=["GlassFiberInsulation","Woodstud"]
f=0.75
Uwall=wcc.wallCalc_withParallel(WallLayersSeries,WallLayersParallel,f)
DoorLayers=["Wood"]
RoofLayers=["CommonBrick","AsphaltShingleRoofing","ConcreteLight"]
Udoor=wcc.wallCalc_onlyInSeries(DoorLayers)
Uroof=wcc.wallCalc_onlyInSeries(RoofLayers)
DT=24.8
Aroof=200
Adoor=2.2
Awall=144
HFdoor=Udoor*DT
HFroof=Uroof*DT
HFwall=Uwall*DT
Qdoor=HFdoor*Adoor
Qroof=HFroof*Aroof
Qwall=HFwall*Awall
wall={"Uwall":Uwall,"HFwall":HFwall,"Qwall":Qwall}
roof={"Uroof":Uroof,"HFroof":HFroof,"Qroof":Qroof}
door={"Udoor":Udoor,"HFdoor":HFdoor,"Qdoor":Qdoor}
print wall
print roof
print door