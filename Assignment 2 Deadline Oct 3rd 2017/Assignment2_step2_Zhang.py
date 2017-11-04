R1 = {"name":"indoor side","area":1.25,"h":10,"REsValue":0}
R2 = {"name":"outdoor side","area":1.25,"h":25,"REsValue":0}

A_R1=R1["area"]
h_R1=R1["h"]
RValue_R1=1/(A_R1*h_R1)

ListOfResistances = [R1,R2]
totalResValueConv=0
for anyResistance in ListOfResistances:
    
    
    A_anyResistance=anyResistance["area"]
    h_anyResistance=anyResistance["h"]
    name_anyResistance=anyResistance["name"]
    RValue_anyResistance=1/(A_anyResistance*h_anyResistance)
    anyResistance["ResValue"]=RValue_anyResistance
    print "here is the new resistance:"
    print anyResistance
    totalResValueConv=totalResValueConv+RValue_anyResistance
    print "So the calculated resistance for "+ name_anyResistance + str(RValue_anyResistance)
    print "******************"
print "So the total Resistance is: " + str(totalResValueConv)

R3={"name":"foam","area":1.25,"length":0.03,"k":0.026,"REsValue":0}
R4={"name":"plaster layer 1","area":1.25,"length":0.02,"k":0.22,"REsValue":0}
R8={"name":"plaster layer 1","area":1.25,"length":0.02,"k":0.22,"REsValue":0}

L_R3=R3["length"]
A_R3=R3["area"]
k_R3=R3["k"]
RValue_R3=L_R3/(A_R3*k_R3)

ListOfResistances = [R3,R4,R8]
totalResValueCond=0
for anyResistance in ListOfResistances:
    
    
    L_anyResistance=anyResistance["length"]
    A_anyResistance=anyResistance["area"]
    k_anyResistance=anyResistance["k"]
    name_anyResistance=anyResistance["name"]
    RValue_anyResistance=L_anyResistance/(A_anyResistance*k_anyResistance)
    anyResistance["ResValue"]=RValue_anyResistance
    print "here is the new resistance:"
    print anyResistance
    totalResValueCond=totalResValueCond+RValue_anyResistance
    print "So the calculated resistance for "+ name_anyResistance + str(RValue_anyResistance)
    print "******************"
print "So the total Resistance is: " + str(totalResValueCond)

R5={"name":"1.5 cm thick plaster layer 1","area":0.075,"length":0.16,"k":0.22,"REsValue":0}
R6={"name":"brick","area":1.1,"length":0.16,"k":0.72,"REsValue":0}
R7={"name":"1.5 cm thick plaster layer 2","area":0.075,"length":0.16,"k":0.22,"REsValue":0}

L_R5=R5["length"]
A_R5=R5["area"]
k_R5=R5["k"]
RValue_R5=L_R5/(A_R5*k_R5)

ListOfResistances = [R5,R6,R7]
totalResValuePara=0
for anyResistance in ListOfResistances:
    
    
    L_anyResistance=anyResistance["length"]
    A_anyResistance=anyResistance["area"]
    k_anyResistance=anyResistance["k"]
    name_anyResistance=anyResistance["name"]
    RValue_anyResistance=L_anyResistance/(A_anyResistance*k_anyResistance)
    anyResistance["ResValue"]=RValue_anyResistance
    print "here is the new resistance:"
    print anyResistance
    totalResValuePara=1/(totalResValuePara+RValue_anyResistance)
    print "So the calculated resistance for "+ name_anyResistance + str(RValue_anyResistance)
    print "******************"
print "So the total Resistance is: " + str(totalResValuePara)

Rtot=totalResValueConv+totalResValueCond+totalResValuePara
print "SO the overall resistance is:" + str(Rtot)+ "degC/W"

T1 = 20 # The indoor temperatures 
T2 = 10 # The outdoor temperatures 

Q = (T1-T2)/Rtot
Atot = 5*3
A = 5*(0.22+0.015+0.015)
Qtot = Q*Atot/A 
print "So the rate of heat transfer through the wall is:" + str(Qtot)+ "W"







