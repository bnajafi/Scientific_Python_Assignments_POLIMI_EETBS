#parallel
Rp1={"area":0.015,"lenght":0.16,"conductivity":0.22}
Rp2=Rp1
Rb={"area":0.22,"lenght":0.16,"conductivity":0.72}
ListOfResistances=[Rp1,Rb,Rp2]
totalinvR=0
for anyR in ListOfResistances:
    print anyR
    LanyR=anyR["lenght"]
    AanyR=anyR["area"]
    kanyR=anyR["conductivity"]
    RValueanyR=LanyR/(AanyR*kanyR)
    inv=1/RValueanyR
    totalinvR=totalinvR+inv
    print"so the calculated R is "+str(RValueanyR)
TotalRp=1/totalinvR    
print"Total parallel R is "+str(TotalRp)

#series
R1={"area":0.25,"lenght":0.03,"conductivity":0.026}
Rp1={"area":0.25,"lenght":0.02,"conductivity":0.22}
Rp2=Rp1
ListOfResistances=[R1,Rp1,Rp2]
totalRs=0
for anyR in ListOfResistances:
    print anyR
    LanyR=anyR["lenght"]
    AanyR=anyR["area"]
    kanyR=anyR["conductivity"]
    RValueanyR=LanyR/(AanyR*kanyR)    
    print"so the calculated R is "+str(RValueanyR)
    totalRs=totalRs+RValueanyR 
print"Total series R is "+str(totalRs)

#convective
Rsi={"area":0.25,"h":10}
Rse={"area":0.25,"h":25}
ListOfResistances=[Rsi,Rse]
totalRc=0
for anyR in ListOfResistances:
    print anyR
    AanyR=anyR["area"]
    hanyR=anyR["h"]
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
