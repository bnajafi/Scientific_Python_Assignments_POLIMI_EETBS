# -*- coding: utf-8 -*-
#insert the data known
WallComposition = {"WoodLapSiding":{"Rvalue":0.14,"length":0.013},"WoodFiberSheeting":{"Rvalue":0.23,"length":0.013},
                   "GypsumWall":{"Rvalue":0.079,"length":0.013},"Inside":{"Rvalue":0.12},"Outside":{"Rvalue":0.030},
                   "GlassFiberInsulation":{"Rvalue":2.45,"length":0.025},"WoodStud":{"Rvalue":0.63,"length":0.090}}

def Results(SBS,SAS,GFI,components):

    Resistance_A = 0
    for i in SBS:
        Resistance_A += components[i]["Rvalue"]

    Resistance_B = 0
    for j in SAS:
        Resistance_B += components[j]["Rvalue"]

    GFI = 0.75 #GlassFiberInsulation percentage
    U = round((GFI*(1/Resistance_A)+(1-GFI)*(1/Resistance_B)),3)
    
    return U


SerieBetweenStud = ["WoodLapSiding","WoodFiberSheeting","GypsumWall","Inside","Outside","GlassFiberInsulation"]
SerieAtStud = ["WoodLapSiding","WoodFiberSheeting","GypsumWall","Inside","Outside","WoodStud"]
FractionGFI = 0.75 #GlassFiberInsulation percentage

U_overall = Results(SerieBetweenStud,SerieAtStud,FractionGFI,WallComposition)

print "The Overall Heat Transfer Coefficient(U-factor) is : "+str(U_overall)+"[W/m^2 °C]"
print("------------------------------------------")


P = 50 #perimeter in m
H = 2.5 #height
GF = 0.20 #glazingFraction
Tout = -2
Tin = 22

Roverall = round((1/U_overall),3)
WallArea = (P*H)-(GF*P*H)
HeatLoss = round((U_overall*WallArea*(Tin-Tout)),3)
print "The Overall Unit Therml Resistance(R-Value) is : "+str(Roverall)+"[m^2 °C/W]"
print ("----------------------------------------")
print "The Heat Loss through the wall is: "+str(HeatLoss)+"[W]"
