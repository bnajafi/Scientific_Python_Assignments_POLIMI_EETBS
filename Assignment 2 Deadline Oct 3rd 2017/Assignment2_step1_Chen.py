#Assignment 2_Step 1_Chen

print "This is about conductive resistance in series: "
print "                                             "
R1=(0.25,0.03,0.026) #foam,unit area:0,length:1, k:2)
R2=(0.25,0.02,0.22) #inner plaster in series , unit area:0, length:1, k:2)
R3=(0.25,0.02,0.22) #outer plaster in series, unit area:0, length:1, k:2)
ListOfConductiveResistancesInSeries=[R1,R2,R3]
totalResValueInSeries=0
for anyresistance in ListOfConductiveResistancesInSeries:
    print "here is the new resistance in series:"
    print anyresistance
    L_anyresistance=anyresistance[1]
    A_anyresistance=anyresistance[0]
    k_anyresistance=anyresistance[2]
    Rvalue_anyresistance= L_anyresistance/(A_anyresistance*k_anyresistance)
    totalResValueInSeries=totalResValueInSeries+Rvalue_anyresistance
    print "So the calculated resistance in series is: " + str(Rvalue_anyresistance) + " degC/W"
    print "                                 "
print "So the total resistance value in series is:" + str(totalResValueInSeries) + " degC/W"
print "************************************************************************"

print "This is about conductive resistance in parallel: "
print "                                     "
R4=(0.015,0.16,0.22) #plaster above brick in parallel,unit area:0,L=1,k=2
R5=(0.015,0.16,0.22) #plaster below brick in parallel,unit area:0,L=1,k=2
R6=(0.22,0.16,0.72) #brick,unit area=0,L=1,k=2
ListOfConductiveResistanceInParallel=[R4,R5,R6]
totalResVaInParallel_MultiplicativeInverse=0
for anyResInParallel in ListOfConductiveResistanceInParallel:
    print "here is the new resistance in parallel: "
    print anyResInParallel
    L_anyResInParallel=anyResInParallel[1]
    A_anyResInParallel=anyResInParallel[0]
    k_anyResInParallel=anyResInParallel[2]
    Rvalue_anyResInParallel=L_anyResInParallel/(A_anyResInParallel*k_anyResInParallel)
    totalResVaInParallel_MultiplicativeInverse=totalResVaInParallel_MultiplicativeInverse+1/Rvalue_anyResInParallel
    totalResVaInParallel=1/totalResVaInParallel_MultiplicativeInverse
    print "so the calculated resistance value in parallel is: " + str(Rvalue_anyResInParallel) + " degC/W"
    print "                                         "
print "so the total resistance value in paralle is: " + str(totalResVaInParallel) + " degC/W"
print "************************************************************************"
    
print "This is about convective resistance: "
print "                             " 
R7=(0.25,10) #inner side,unit area=0,convection heat transfer coefficients=1
R8=(0.25,25) #outer side,unit area=0,convection heat transfer coefficients=1
ListOfConvectiveResistance=[R7,R8]
totalConRes=0
for anyConResistance in ListOfConvectiveResistance:
    print "here is the new convective resistance: "
    print  anyConResistance
    A_anyConResistance=anyConResistance[0]
    h_anyConResistance=anyConResistance[1]
    Rvalue_anyConResistance=1/(A_anyConResistance*h_anyConResistance)
    totalConRes=totalConRes+ Rvalue_anyConResistance
    print "so the calculated convective resistance is: " + str(Rvalue_anyConResistance) + " degC/W"
    print "                                     "
print "so the total convective resistance value is: " + str(totalConRes)+ " degC/W"
print "************************************************************************"
R=totalResValueInSeries+totalResVaInParallel+totalConRes #the overwall resistance of the wall

print "so the overall resistance of the wall is: " + str(R) + " degC/W"

T1=20 #The indoor temperature
T2=-10 #The outdoor temperature
Q0=(T1-T2)/R #The unit heat loss
print "so the unit heat loss of the wall is: " + str(Q0) + " W"
h=3 #total wall high
w=5 #total wall width
A=0.25 #unit area of the wall
Q=Q0*(h*w/A) #the total heat loss of the wall
print "so the total heat loss of the wall is: "+ str(Q) + " W"