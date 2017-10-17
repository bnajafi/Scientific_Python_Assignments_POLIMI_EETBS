# -*- coding: utf-8 -*-
T1= 20 #Indoor temperature
T2= -10 #Outdoor temperatureL1= 0.03 #Thickness of foam
H=0.25 #Total heigth

#Assuming the width equal to 1m
R1= [0.03,0.25,0.026] #Tickness, area and k of the foam
R2=[0.04,0.25,0.22] #Tickness, area and k of the plastic layers
R3= [0.16,0.015,0.22] #Tickness, area and k of the plastic layer over and below the brick
R4= [0.16,0.22,0.72] #Tickness, area and k of the brick
Rconv1= [0.25,10] #Area and h of inner side
Rconv2= [0.25,25] #Area and h of outer side

ListOfResistances_Series= [R1,R2]
totalResValue_ser= 0
for anyResistance in ListOfResistances_Series:
    L_anyResistance= anyResistance[0]
    A_anyResistance = anyResistance[1]
    k_anyResistance=anyResistance[2]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    totalResValue_ser = totalResValue_ser+RValue_anyResistance
print 'The total resistance in series is ' +str(totalResValue_ser) +(' °C/W')
print ' '

ListOfResistances_Parallel= [R3,R3,R4]
totalResValue_par= 0
for anyResistance in ListOfResistances_Parallel:
    L_anyResistance= anyResistance[0]
    A_anyResistance = anyResistance[1]
    k_anyResistance=anyResistance[2]
    RValue_anyResistance = L_anyResistance/(A_anyResistance*k_anyResistance)
    Recip=1/RValue_anyResistance
    totalResValue_par=totalResValue_par+Recip
print 'The total resistance in parallel is ' +str(1/totalResValue_par) +(' °C/W')
print ' '

ListOfResistances_Conv=[Rconv1,Rconv2]
totalResValue_Conv=0
for anyResistance in ListOfResistances_Conv:
    A_anyResistance = anyResistance[0]
    h_anyResistance=anyResistance[1]
    RValue_anyResistance = 1/(A_anyResistance*h_anyResistance)
    totalResValue_Conv = totalResValue_Conv+RValue_anyResistance
print 'The total convective resistance is ' +str(totalResValue_Conv) +(' °C/W')
print ' '

R_Tot=totalResValue_ser+1/totalResValue_par+totalResValue_Conv
print ('The total resistence is ') + str(R_Tot) + (' °C/W')
print ' '
Q=(T1-T2)/R_Tot #Q of the unit area
print ('The rate of heat transfer through the wall per unit area is ') +str(Q) + (' W')
print ' '
Htot=3 #Total height
Ltot=5 #Total width
print ' '
Qtot=Q*Ltot*Htot/H #Q total
print ('The total rate of heat transfer through the wall is ') +str(Qtot) + (' W')