import os
os.chdir ("/Users/FedericoGenco/Desktop")

import wallCalculation_genco as calc

inseries=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
inparallel=["glass_fiber","wood_stud"]
firstratio= float(0.75)
door=["wood_5cm"]
roof=["wood_stud","wood_5cm"]

Utot_wall= calc.wallCalc_withParallel(inseries,inparallel,firstratio)
Utot_door= calc.wallCalc_onlyInSeries (door)
Utot_roof= calc.wallCalc_onlyInSeries (roof)

T_d_heating=-4.8
T_int=20
deltaT= 24.8
area=[105.8,2.2,200]
Utot=[0.4904059,2.2727272727,0.934579]

HF=[]
Q=[]
index=range(3)

for anyindex in index:
    HF.append(Utot[anyindex]*deltaT)
    Q.append(HF[anyindex]*area[anyindex])

print "The values of U for wall, door and roof result "+str(HF)
print "The values of Q for wall, door and roof result "+str(Q)




    
    