# -*- coding: utf-8 -*-
T1= 20 #Indoor temperature
T2= -10 #Outdoor temperatureL1= 0.03 #Thickness of foam
H=0.25 #Total heigth

#Assuming the width equal to 1m

R1= {'name':'foam','Thickness':0.03,'area':0.25,'k':0.026}
R2= {'name':'plastic layers','Thickness':0.04,'area':0.25,'k':0.22}
R3= {'name':'plastic layer over and below the brick','Thickness':0.16,'area':0.015,'k':0.22}
R4= {'name':'brick','Thickness':0.16,'area':0.22,'k':0.72}
Rconv1={'area':0.25,'h':10}
Rconv2={'area':0.25,'h':25}

ListOfResistances_Series= [R1,R2]
totalResValue_ser= 0
for anyResistance in ListOfResistances_Series:
    RValue_anyResistance = anyResistance['Thickness']/(anyResistance['area']*anyResistance['k'])
    totalResValue_ser = totalResValue_ser+RValue_anyResistance
print 'The total resistance in series is ' +str(totalResValue_ser) +(' °C/W')
print ' '

ListOfResistances_Parallel= [R3,R3,R4]
totalResValue_par= 0
for anyResistance in ListOfResistances_Parallel:
    RValue_anyResistance = anyResistance['Thickness']/(anyResistance['area']*anyResistance['k'])
    Recip=1/RValue_anyResistance
    totalResValue_par=totalResValue_par+Recip
print 'The total resistance in parallel is ' +str(1/totalResValue_par) +(' °C/W')
print ' '

ListOfResistances_Conv=[Rconv1,Rconv2]
totalResValue_Conv=0
for anyResistance in ListOfResistances_Conv:
    RValue_anyResistance = 1/(anyResistance['area']*anyResistance['h'])
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