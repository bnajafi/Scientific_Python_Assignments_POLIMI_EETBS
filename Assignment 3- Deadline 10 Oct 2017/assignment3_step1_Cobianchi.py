# -*- coding: utf-8 -*-
#Heat Transfer Through Walls

#insert the data known
WallComposition = {"WoodLapSiding":{"Rvalue":0.14,"length":0.013},"WoodFiberSheeting":{"Rvalue":0.23,"length":0.013},
                   "GypsumWall":{"Rvalue":0.079,"length":0.013},"Inside":{"Rvalue":0.12},"Outside":{"Rvalue":0.030},
                   "GlassFiberInsulation":{"Rvalue":2.45,"length":0.025},"WoodStud":{"Rvalue":0.63,"length":0.090}}

SerieBetweenStud=["WoodLapSiding","WoodFiberSheeting","GypsumWall","Inside","Outside","GlassFiberInsulation"]
SerieAtStud=["WoodLapSiding","WoodFiberSheeting","GypsumWall","Inside","Outside","WoodStud"]

Resistance_A = 0
for i in SerieBetweenStud:
    Resistance_A += WallComposition[i]["Rvalue"]
print ("The Resistance in Serie between stud is:  ")+str(Resistance_A)+"[m^2 °C/W]"

Resistance_B = 0
for j in SerieAtStud:
    Resistance_B += WallComposition[j]["Rvalue"]
print ("The Resistance in Serie at stud is:  ")+str(Resistance_B)+"[m^2 °C/W]"
print ("----------------------------------------")

FractionGFI = 0.75 #GlassFiberInsulation percentage
U = round((FractionGFI*(1/Resistance_A)+(1-FractionGFI)*(1/Resistance_B)),3)
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