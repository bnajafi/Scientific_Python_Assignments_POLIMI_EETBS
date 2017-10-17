#Assignment 3_Step1_Chen

Matrial_Library={"OutsideSurfaceWinter":0.030,"WoodBevelLappedSiding_13mm":0.14,
"WoodFiberboardSheeting_13mm":0.23,"GlassFiberInsulation_90mm":2.45,"WoodStud_90mm":0.63,
"GypsumWallboard_13mm":0.079,"InsideSurfaceAir":0.12}

#Making it into through insulation part and through the studs
Layers_throughInsulation=["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
"WoodFiberboardSheeting_13mm","GlassFiberInsulation_90mm",
"GypsumWallboard_13mm","InsideSurfaceAir"]

Layers_throughStuds=["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
"WoodFiberboardSheeting_13mm","WoodStud_90mm",
"GypsumWallboard_13mm","InsideSurfaceAir"]

Layers_Series=[Layers_throughInsulation,Layers_throughStuds]


Rtot_Series=[]
for series in Layers_Series:
    Rtot=0
    for anylayer in series:
        Rtot=Rtot+Matrial_Library[anylayer]
    Rtot_Series.append(Rtot) 
print "The total unit value in series are " + str(Rtot_Series)+ " m2*degreeC/W"


Ratio=float(0.75) #insulation 0.75, while studs 1-ratio
Layers_Parallel_Ufactor=[1/Rtot_Series[0]*Ratio,1/Rtot_Series[1]*(1-Ratio)]
print "The total unit Ufactor in parallel are: " + str(Layers_Parallel_Ufactor)+" W/m2*degreeC"

Utot=Layers_Parallel_Ufactor[0]+Layers_Parallel_Ufactor[1]
print "The overall U-factor is: "+ str(Utot)+ " W/m2*degreeC"
Rtot=1/Utot
print "The overall unit thermal resistance is: "+str(Rtot)+ " m2*degreeC/W"
A_wall=0.8*50*2.5 #The perimeter of the building is 50m, the height of the walls is 2.5m,the glazing constitutes 20 percent of the walls
Ti=22
To=-2
Q=Utot*A_wall*(Ti-To)
print "The rate of heat loss through the walls under design conditions is: "+str(Q) + " W"
   