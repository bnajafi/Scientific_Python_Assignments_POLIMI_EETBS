# -*- coding: utf-8 -*-
import numpy as np

Wall_components = np.array(["Outside","WoodLapSiding","WoodFiberSheeting","GlassFiberInsulation","WoodStud","GypsumWall","Inside"])
Rvalues = np.array([0.030,0.14,0.23,2.45,0.63,0.079,0.12])

SerieBetweenStud = np.array(["Outside","WoodLapSiding","WoodFiberSheeting","GlassFiberInsulation","GypsumWall","Inside"])
SerieAtStud = np.array(["Outside","WoodLapSiding","WoodFiberSheeting","WoodStud","GypsumWall","Inside"])


RValue_SerieBetweenStud = np.zeros(SerieBetweenStud.size)
RValue_SerieAtStud = np.zeros(SerieAtStud.size)


for layer in SerieBetweenStud:
    RValue_SerieBetweenStud[SerieBetweenStud == layer] = Rvalues[Wall_components == layer]
    Resistances_Rtot1 = RValue_SerieBetweenStud.sum()
print ("The Resistance in Serie between stud is:  ")+str(Resistances_Rtot1)+"[m^2 °C/W]"

for layer in SerieAtStud:
    RValue_SerieAtStud[SerieAtStud == layer] = Rvalues[Wall_components == layer]
    Resistances_Rtot2 = RValue_SerieAtStud.sum()
print ("The Resistance in Serie at stud is:  ")+str(Resistances_Rtot2)+"[m^2 °C/W]"
print ("----------------------------------------")


FractionGFI = 0.75 #GlassFiberInsulation percentage
U = round((FractionGFI*(1/Resistances_Rtot1)+(1-FractionGFI)*(1/Resistances_Rtot2)),3)
print "The Overall Heat Transfer Coefficient(U-factor) is : "+str(U)+"[W/m^2 °C]"

P = 50 #perimeter in m
H = 2.5 #height
GF = 0.20 #glazingFraction
Tout = -2
Tin = 22

Roverall = round((1/U),3)
WallArea = (P*H)-(GF*P*H)
HeatLoss = round((U*WallArea*(Tin-Tout)),3)
print "The Overall Unit Therml Resistance(R-Value) is : "+str(Roverall)+"[m^2 °C/W]"
print ("----------------------------------------")
print "The Heat Loss through the wall is: "+str(HeatLoss)+"[W]"