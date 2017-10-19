import os 
os.chdir("/Users/Guglielmo/Desktop/BULDINGS/phyton/assignment 4")

import wallCalculations_DeVanna1 as WALL

inseries=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
inparallel=["glass_fiber","wood_stud"]
firstratio=float(0.75)
door=["wood_5cm"]
roof=["asphalt_shingle_roofing","wood_stud_140mm"]

Utotwall= WALL.wallCalc_withParallel(inseries,inparallel,firstratio)
Utotdoor= WALL.wallCalc_onlyInSeries(door)
Utotroof= WALL.wallCalc_onlyInSeries(roof)
Utot=[Utotwall,Utotdoor,Utotroof]
areas=[105.8, 2.2, 200]
index=range(3)
HF=[]
Q=[]

t_design_heating=-4.8 #from tables
tint=20 
AT=(tint-t_design_heating)

for anyindex in index:
    HF.append(Utot[anyindex]*AT)
    Q.append(HF[anyindex]*areas[anyindex])

print"the total U of the wall is:"+str(Utotwall)+" W/(deg*m)"
print"the total U of the door is:"+str(Utotdoor)+" W/(deg*m)"
print"the total U of the roof is:"+str(Utotroof)+" W/(deg*m)"
print"the total HF of the wall is:"+str(HF[0])+" W/(m^2)"
print"the total HF of the door is:"+str(HF[1])+" W/(m^2)"
print"the total HF of the roof is:"+str(HF[2])+" W/(m^2)"
print"the total Q of the wall is:"+str(Q[0])+" W"
print"the total Q of the door is:"+str(Q[1])+" W"
print"the total Q of the roof is:"+str(Q[2])+" W"

    
    

