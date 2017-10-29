R1 = [10,1.25] #the indoor side,Area:1,convection heat transfer coefficient:0
R2 = [25,1.25] #the outdoor side,Area:1,convection heat transfer coefficient:0

A_R1=R1[1]
h_R1=R1[0]

ListOfResistances = [R1,R2]
totalResValueConv=0
for anyResistance in ListOfResistances:
    print "here is the new resistance:"
    print anyResistance
    A_anyResistance=anyResistance[1]
    h_anyResistance=anyResistance[0]
    RValue_anyResistance=1/(A_anyResistance*h_anyResistance)
    totalResValueConv=totalResValueConv+RValue_anyResistance
    print "So the calculated resistance is: " + str(RValue_anyResistance)+ "degC/W"
    print "******************"
print "So the total calculated resistance is: " + str(totalResValueConv)+ "degC/W"
    
R3 = [0.03,0.026,1.25] #foam,Length:0,conductivity:1,Area:2
R4 = [0.02,0.22,1.25] #plaster layer 1,Length:0,conductivity:1,Area:2
R8 = [0.02,0.22,1.25] #plaster layer 2,Length:0,conductivity:1,Area:2

L_R3=R3[0]
A_R3=R3[1]
k_R3=R3[2]

ListOfResistances = [R3,R4,R8]
totalResValueCond=0
for anyResistance in ListOfResistances:
    print "here is the new resistance:"
    print anyResistance
    L_anyResistance=anyResistance[0]
    A_anyResistance=anyResistance[2]
    k_anyResistance=anyResistance[1]
    RValue_anyResistance=L_anyResistance/(A_anyResistance*k_anyResistance)
    totalResValueCond=totalResValueCond+RValue_anyResistance
    print "So the calculated resistance is: " + str(RValue_anyResistance)+ "degC/W"
    print "******************"
print "So the total calculated resistance is: " + str(totalResValueCond)+ "degC/W"

R5 = [0.16,0.22,0.075] #1.5 cm thick plaster layer 1,Length:0,conductivity:1,Area:2
R6 = [0.16,0.72,1.1] #brick,Length:0,conductivity:1,Area:2
R7 = [0.16,0.22,0.075] #1.5 cm thick plaster layer 2,Length:0,conductivity:1,Area:2

L_R5=R5[0]
A_R5=R5[1]
k_R5=R5[2]

ListOfResistances = [R5,R6,R7]
totalResValuePara=0
for anyResistance in ListOfResistances:
    print "here is the new resistance:"
    print anyResistance
    L_anyResistance=anyResistance[0]
    A_anyResistance=anyResistance[2]
    k_anyResistance=anyResistance[1]
    RValue_anyResistance=L_anyResistance/(A_anyResistance*k_anyResistance)
    totalResValuePara=1/(totalResValuePara+RValue_anyResistance)
    print "So the calculated resistance is: " + str(RValue_anyResistance)+ "degC/W"
    print "******************"
print "So the total calculated resistance is: " + str(totalResValuePara)+ "degC/W"

Rtot = totalResValueConv+totalResValueCond+totalResValuePara
print "SO the overall resistance is:" + str(Rtot)+ "degC/W"

T1 = 20 # The indoor temperatures 
T2 = 10 # The outdoor temperatures 

Q = (T1-T2)/Rtot
Atot = 5*3
A = 5*(0.22+0.015+0.015)
Qtot = Q*Atot/A 
print "So the rate of heat transfer through the wall is:" + str(Qtot)+ "W"









