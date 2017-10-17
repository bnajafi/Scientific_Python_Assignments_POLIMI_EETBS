# -*- coding: utf-8 -*-
mat_library={"in surface": 0.12,"wood lapped": 0.14,"wood sheeting": 0.23,"insulation": 2.45,"wood stud": 0.63,"gypsum wallboard": 0.079,"out surface": 0.03}
series=["wood lapped","wood sheeting","gypsum wallboard"]
paral=["insulation","wood stud",]
convection=["in surface","out surface"]
ratio=float(0.75)

#totals (sum)
Tparal=paral
Tseries=series+convection
wallresistance=[]
rser=0
for anylayer in Tseries:
    Rseries=mat_library[anylayer]
    rser=rser+Rseries
for anyylayer in Tparal:
    Rparal=mat_library[anyylayer]
    wallresistance.append(rser+Rparal)

Ufirst=1/wallresistance[0]
Usecond=1/wallresistance[1]

Utot=Ufirst*ratio+Usecond*(1-ratio)
Tin=22
Tout=-2
Perim=50
Heigth=2.5
Area=Perim*Heigth
disperding_percentage=1-0.2 #only the 80% of the area loses heat
Q=Utot*Area*disperding_percentage*(Tin-Tout)
print ("the resistances of the wall are ")+str(wallresistance)
print("the overall heat transfer coefficient is ")+str(Utot)
print("since the internal temperature is ")+str(Tin)
print("the external temperature is ")+str(Tout) 
print("(I thought that in Nevada it was hotter)")
print("the area is ")+str(Area)
print("the rate of loss heat is ")+str(Q)