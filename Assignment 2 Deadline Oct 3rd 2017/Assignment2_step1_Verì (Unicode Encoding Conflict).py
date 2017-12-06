#convective resistances
Ri=[10,0.25]# inlet side; heat transfer coefficient: 0; Area:1
Ro=[25,0.25]# outlet side; heat transfer coefficient: 0; Area:1
listOfResistances1=[Ri,Ro]
totalRes1=0
for anyResistance in listOfResistances1:
    print "here is the new resistance: "
    print anyResistance
    print "***********"
    h_anyResistance=anyResistance[0]
    A_anyResistance=anyResistance[1]
    resValue_anyResistance1=1/(h_anyResistance*A_anyResistance)
    totalRes1=totalRes1+resValue_anyResistance1
    print "so the calculated resistance is: "+str(resValue_anyResistance1)
    print "***********"
print "so the total resistance value is: " +str(totalRes1)

#conductive resistances in series
Rf=[0.03,0.026,0.25]# foam; length:0; conductivity:1; area:2
Rp1=[0.02,0.22,0.25]# plaster1; length:0; conductivity:1; area:2
Rp2=[0.02,0.22,0.25]# plaster2; length:0; conductivity:1; area:2
listOfResistances2=[Rf,Rp1,Rp2]
totalRes2=0
for anyResistance in listOfResistances2:
    print "here is the new resistance: "
    print anyResistance
    print "***********"
    L_anyResistance=anyResistance[0]
    k_anyResistance=anyResistance[1]
    A_anyResistance=anyResistance[2]
    resValue_anyResistance2=L_anyResistance/(k_anyResistance*A_anyResistance)
    totalRes2=totalRes2+resValue_anyResistance2
    print "so the calculated resistance is: "+str(resValue_anyResistance2)
    print "***********"
print "so the total resistance value is: " +str(totalRes2)

#conductive resistances in parallel
Rpc1=[0.16,0.22,0.015]# upper side of the plaster; length:0; conductivity:1; area:2
Rpc2=[0.16,0.22,0.015]# lower side of the plaster; length:0; conductivity:1; area:2
Rb=[0.16,0.72,0.22]# brick; length:0; conductivity:1; area:2
listOfResistances3=[Rpc1,Rpc2,Rb]
inv_totalRes3=0
for anyResistance in listOfResistances3:
    print "here is the new resistance: "
    print anyResistance
    print "***********"
    L_anyResistance=anyResistance[0]
    k_anyResistance=anyResistance[1]
    A_anyResistance=anyResistance[2]
    resValue_anyResistance3=L_anyResistance/(k_anyResistance*A_anyResistance)
    inv_resValue_anyResystance3=1/(L_anyResistance/(k_anyResistance*A_anyResistance))
    inv_totalRes3=inv_totalRes3+inv_resValue_anyResystance3
    totalRes3=1/inv_totalRes3
    print"so the calculated resistance is: "+str(resValue_anyResistance3)
    print "***********"
print "so the total resistance value is: " +str(totalRes3)
print "************"
#total resistance
totalRes=totalRes1+totalRes2+totalRes3
print "so the total resistance value is: "+str(totalRes)

# heat transfer unit
Tindoor=20
Toutdoor=(-10)
Qunit=(Tindoor-Toutdoor)/totalRes
#heat transfer through the wall
Awall=15
A=0.25
Qwall=Qunit*Awall/A
print "so the heat transfer through the wall is: " +str(Qwall)