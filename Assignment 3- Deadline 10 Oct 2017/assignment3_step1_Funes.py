# -*- coding: utf-8 -*-
#Dictionaries method
Materials_RValues = {"insideSurface":0.12,"outsideSurfaceWinter":0.03,"gypsumWallboard13mm":0.079,
"woodStuds90mm":0.63,"glassFiber25mm":2.45,"woodFiberboard13mm":0.23,"woodBevel200mm":0.14}

Materials_In_Series = ["insideSurface","outsideSurfaceWinter","gypsumWallboard13mm","woodFiberboard13mm","woodBevel200mm"]
Materials_In_Parallel = ["woodStuds90mm","glassFiber25mm"]
Wall_complete = Materials_In_Series + Materials_In_Parallel

Rseries = 0
for AnyMaterial in Materials_In_Series:
    RValue_layer = Materials_RValues [AnyMaterial]
    Rseries = Rseries + RValue_layer
print "The equivalent Resistance Value of the materials in series is: "+str(Rseries)+"(m2*°C/W)"

Rparallel = 99999999999999999999
for AnyMaterial in Materials_In_Parallel:
    RValue_layer = Materials_RValues [AnyMaterial]
    Rparallel = 1/((1/Rparallel) + (1/RValue_layer))
print "The equivalente Resistance Value of the materials in parallel is: "+str(Rparallel)+"(m2*°C/W)"

CenterWallJustGlassFiber = ["glassFiber25mm"]
WallFirstLayer = Materials_In_Series + CenterWallJustGlassFiber
RfirstLayer=0
for AnyMaterial in WallFirstLayer:
    RValue_layer = Materials_RValues [AnyMaterial]
    RfirstLayer = RfirstLayer + RValue_layer
print "The resistance of the wall considering just the insulation is: "+str(RfirstLayer)+"(m2*°C/W)"

CenterWallJustWoodStud = ["woodStuds90mm"]
WallSecondLayer = Materials_In_Series + CenterWallJustWoodStud
RsecondLayer=0
for AnyMaterial in WallSecondLayer:
    RValue_layer = Materials_RValues [AnyMaterial]
    RsecondLayer = RsecondLayer + RValue_layer
print "The resistance of the wall considering just the wood studs is: "+str(RsecondLayer)+"(m2*°C/W)"



fins=float (raw_input("Please enter the ratio between the area of the insulator and the total area: "))
Uins = (1/RfirstLayer)
Uwood = (1/RsecondLayer)
print "The heat transfer coefficient taking into account that there's only wood in the center is :"+str(Uwood)+"(W/m2*°C)"
print "The heat transfer coefficient taking into account that there's only glass fiber insulator in the center is :"+str(Uins)+"(W/m2*°C)"

Utot = Uins*fins + Uwood*(1-fins)
print "The overall heat transfer coefficient is: "+str(Utot)+"(W/m2*°C)"

Rtot = 1/Utot
print "The overall thermal resistance of the wall is: "+str(Rtot)+"(m2*°C/W)"

Perimeter = float(raw_input("Please enter the perimeter of the house in meters: "))
Height = float(raw_input("Please enter the height of the walls in meters: "))
PropOfWalls = float(raw_input("Please enter the proportion of the walls that is not glazing: "))
Tin = float(raw_input("Please enter the temperature of the inner environment: "))
Tout = float(raw_input("Please enter the temperature of the outer environment: "))

Atot = PropOfWalls*Perimeter*Height
Qwalls = Utot*Atot*(Tin-Tout)
print "The total heat transfered through the walls is :"+str(Qwalls)+"(W)"

