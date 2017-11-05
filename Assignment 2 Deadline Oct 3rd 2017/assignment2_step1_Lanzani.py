#parallel
Rp1=[0.015,0.16,0.22] #plaster
Rb=[0.22,0.16,0.72] #brick
Rp2=Rp1
ListOfResistances=[Rp1,Rb,Rp2]
totalinvR=0
for anyR in ListOfResistances:
    print anyR
    LanyR=anyR[1]
    AanyR=anyR[0]
    kanyR=anyR[2]
    RValueanyR=LanyR/(AanyR*kanyR)
    inv=1/RValueanyR
    totalinvR=totalinvR+inv
    print"so the calculated R is "+str(RValueanyR)
TotalRp=1/totalinvR    
print"Total parallel R is "+str(TotalRp)

#series
R1=[0.25,0.03,0.026] #foam
Rp1=[0.25,0.02,0.22] #plaster
Rp2=Rp1
ListOfResistances=[R1,Rp1,Rp2]
totalRs=0
for anyR in ListOfResistances:
    print anyR
    LanyR=anyR[1]
    AanyR=anyR[0]
    kanyR=anyR[2]
    RValueanyR=LanyR/(AanyR*kanyR)    
    print"so the calculated R is "+str(RValueanyR)
    totalRs=totalRs+RValueanyR 
print"Total series R is "+str(totalRs)

#convective
Rsi=[10,0.25]
Rse=[25,0.25]
ListOfResistances=[Rsi,Rse]
totalRc=0
for anyR in ListOfResistances:
    print anyR
    AanyR=anyR[0]
    hanyR=anyR[1]
    RValueanyR=1/(AanyR*hanyR)
    print"so the calculated R is "+str(RValueanyR)
    totalRc=totalRc+RValueanyR 
print"Total convective R is "+str(totalRc)

#total
Rtot=TotalRp+totalRs+totalRc
print"Total R is "+str(Rtot)

#Q
Aw=3*5
T1=20
T2=-10
Q=(T1-T2)/Rtot
A=0.25*1
Qw=Q*(Aw/A)
print 'Qw is '+ str(Qw)+ ' W'

    