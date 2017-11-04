# -*- coding: utf-8 -*-
Materials_Dictionary = {"Outside_surface":0.030,"Wood_bevel_lapped_siding":0.14,"Wood_fiberboard_sheeting13mm":0.23,"Glass_fiber_insulation90mm":2.45,"Wood_stud38*90mm":0.63,"Gypsum_wallboard13mm":0.079,"Inside_surface":0.12}
#Calculating resistance when lenght is different from table
Length_GlassFiber = 90

if Length_GlassFiber == 25:
    Rvalue = 0.7
else:
    Rvalue = float(Length_GlassFiber)*(0.7/25)
print "The resistance value for glass fiber is "+str(Rvalue)+" m^2*°C/W"

#Calculation of heat flux through the wall
WallPar = ["Glass_fiber_insulation90mm","Wood_stud38*90mm"]
WallSer = ["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting13mm","Gypsum_wallboard13mm"]
Air = ["Outside_surface","Inside_surface"]
AreaFraction= 0.75
RSeriesValues = []
RParallelValues = []
RAirValues = []
RSerTot = 0
RAirTot = 0

for AnyLayer in WallSer:
    RValueSer = Materials_Dictionary[AnyLayer]
    RSeriesValues.append(RValueSer)
    RSerTot = RSerTot + RValueSer   
    print "This layer is "+AnyLayer
    print "The resistance of " +AnyLayer +" is "+str(RValueSer) +" m^2*°C/W"
print "**********************************************************************************************"
print "The total value of the conductive resistances in series is "+str(RSerTot) +" m^2*°C/W"
print "**********************************************************************************************"

for AnyLayer in Air:
    RValueAir = Materials_Dictionary[AnyLayer]
    RAirValues.append(RValueAir)
    RAirTot = RAirTot + RValueAir   
    print "This layer is "+AnyLayer
    print "The convective resistance of " +AnyLayer +" is "+str(RValueAir) +" m^2*°C/W"
print "**********************************************************************************************"
print "The total value of the convective resistances is "+str(RAirTot) +" m^2*°C/W"

Uoverall = 0
for AnyLayer in WallPar:
    RValuePar = Materials_Dictionary[AnyLayer]
    RParallelValues.append(RValuePar)
    print "This layer is "+str(AnyLayer)
    print "The resistance of " +str(AnyLayer)+" is "+str(RValuePar) +" m^2*°C/W"
    Rsection = RSerTot + RAirTot + RValuePar
    Usection = 1 / Rsection
    if (AnyLayer=="Glass_fiber_insulation90mm"):
        AreaCoeff=AreaFraction
    else:
        AreaCoeff=1-AreaFraction
      
    Uoverall = Uoverall + Usection*AreaCoeff
    
    print "U of the section with "+AnyLayer +" is "+str(Usection)+" W/(m^2*°C)"
print "**********************************************************************************************"
print "The U_tot of the wall is "+str(Uoverall)+" W/(m^2*°C)"

Roverall = 1 / Uoverall

print "**********************************************************************************************"
print "The overall resistance of the wall is "+str(Roverall)+" m^2*°C/W"
print "**********************************************************************************************"
T1 = 22
T2 = -2
A = 100
Q_wall = Uoverall*A*(T1-T2)
print "The total heat flux through the wall is "+str(Q_wall)+" W"