# -*- coding: utf-8 -*-
Matetials_Dictionary = {"Wood_Bevel_Lapped_Siding":0.14,"Wood_Fiberboard_Sheeting":0.23,"Glass_Fiber_Insulation":2.45,"Wood_Stud":0.63,"Gypsum_Wallboard":0.079,"Outside_Surface_Winter":0.03,"Inside_Surface":0.12}

WallPar = ["Glass_Fiber_Insulation","Wood_Stud"]

WallSer = ["Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Gypsum_Wallboard"]

Air = ["Outside_Surface_Winter","Inside_Surface"]

AreaFraction= 0.75

RSeriesValues = []

RParallelValues = []

RAirValues = []

RSerTot = 0

RAirTot = 0

for AnyLayer in WallSer:
    RValueSer = Matetials_Dictionary[AnyLayer]
    RSeriesValues.append(RValueSer)
    RSerTot = RSerTot + RValueSer   
    print "This layer is "+AnyLayer
    print "The resistance of " +AnyLayer +" is "+str(RValueSer) +" m^2*°C/W"
print "**********************************************************************************************"
print "The total value of the conduvtive resistances in series is "+str(RSerTot) +" m^2*°C/W"
print "**********************************************************************************************"

for AnyLayer in Air:
    RValueAir = Matetials_Dictionary[AnyLayer]
    RAirValues.append(RValueAir)
    RAirTot = RAirTot + RValueAir   
    print "This layer is "+AnyLayer
    print "The convective resistance of " +AnyLayer +" is "+str(RValueAir) +" m^2*°C/W"
print "**********************************************************************************************"
print "The total value of the convective resistances is "+str(RAirTot) +" m^2*°C/W"

Uoverall = 0
for AnyLayer in WallPar:
    RValuePar = Matetials_Dictionary[AnyLayer]
    RParallelValues.append(RValuePar)
    print "This layer is "+AnyLayer
    print "The resistance of " +AnyLayer +" is "+str(RValuePar) +" m^2*°C/W"
    Rsection = RSerTot + RAirTot + RValuePar
    Usection = 1 / Rsection
    if (AnyLayer=="Glass_Fiber_Insulation"):
        AreaCoeff=AreaFraction
    else:
        AreaCoeff=1-AreaFraction
      
    Uoverall = Uoverall + Usection*AreaCoeff
    
    print "The conductivity of the section with "+AnyLayer+" is "+str(Usection)+" W/(m^2*°C)"
print "**********************************************************************************************"
print "The overall conductivity of the wall is "+str(Uoverall)+" W/(m^2*°C)"

Roverall = 1 / Uoverall

print "**********************************************************************************************"
print "The overall resistance of the wall is "+str(Roverall)+" m^2*°C/W"
print "**********************************************************************************************"
