#Assignment 3_Step1_Chen
def wall_calc_assignment(Layers_Series,FractionOfInsulation):
    Matrial_Library={"OutsideSurfaceWinter":0.030,"WoodBevelLappedSiding_13mm":0.14,
    "WoodFiberboardSheeting_13mm":0.23,"GlassFiberInsulation_90mm":2.45,"WoodStud_90mm":0.63,
    "GypsumWallboard_13mm":0.079,"InsideSurfaceAir":0.12}
    
    #Making it into through insulation part and through the studs
    
    
    Layers_Series=[Layers_throughInsulation,Layers_throughStuds]

    Rtot_series=[]
    for series in Layers_Series:
        R=0
        for anylayer in series:
            R=R+Matrial_Library[anylayer]
        Rtot_series.append(R) 
    Ratio=FractionOfInsulation    
    Layers_series_Ufactor=[1/Rtot_series[0]*Ratio,1/Rtot_series[1]*(1-Ratio)]    
    Utot=Layers_series_Ufactor[0]+Layers_series_Ufactor[1]
    Rtot=1/Utot
    results={"The total resistance through insulation and studs":Rtot_series,"Total Resistance":Rtot,"the total U of the wall":Utot}
    return results
    
Layers_throughInsulation=["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
    "WoodFiberboardSheeting_13mm","GlassFiberInsulation_90mm",
    "GypsumWallboard_13mm","InsideSurfaceAir"]
    
Layers_throughStuds=["OutsideSurfaceWinter","WoodBevelLappedSiding_13mm",
"WoodFiberboardSheeting_13mm","WoodStud_90mm",
"GypsumWallboard_13mm","InsideSurfaceAir"]


results=wall_calc_assignment([Layers_throughInsulation,Layers_throughStuds],0.75)
print results
Utot=results["the total U of the wall"]

A_wall=0.8*50*2.5 #The perimeter of the building is 50m, the height of the walls is 2.5m,the glazing constitutes 20 percent of the walls
Ti=22
To=-2
Q=Utot*A_wall*(Ti-To)
print "The rate of heat loss through the walls under design conditions is: "+str(Q) + " W"
   