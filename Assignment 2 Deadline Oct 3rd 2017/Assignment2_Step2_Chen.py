#Assignment 2_Step 2_Chen

#calculating the resistance in series

print "************************************************************************"
print "               #This is the resistance in Series#"
print "************************************************************************"
print "   "

R1={"type":"foam","unit area":0.25,"length":0.03,"conductivity":0.026,"SeResValue":0}
R2={"type":"inner plaster in series","unit area":0.25,"length":0.02,"conductivity":0.22,"SeResValue":0}
R3={"type":"outer plaster in series","unit area":0.25,"length":0.02,"conductivity":0.22,"SeResValue":0}

ListOfSeRes=[R1,R2,R3]
totalSeRes=0
for anySeRes in ListOfSeRes:
    
    A_anySeRes=anySeRes["unit area"]
    L_anySeRes=anySeRes["length"]
    k_anySeRes=anySeRes["conductivity"]
    type_anySeRes=anySeRes["type"]
    RValue_anySeRes=L_anySeRes/(A_anySeRes* k_anySeRes)
    anySeRes["SeResValue"]=RValue_anySeRes
    print "here is the new resistance in series: "
    print anySeRes
    print "         "
    print "so the Resistance Value for " + str(type_anySeRes) + " is: " + str(RValue_anySeRes) + " degC/W" 
    totalSeRes=totalSeRes+RValue_anySeRes
    print "    "
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"    
print "so the total resistance value in series is: " + str(totalSeRes) + " degC/W" 
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"    
print "   "
 
#calculating the resistance in parallel 
 
print "************************************************************************"
print "           #This is the resistance in Parallel#"
print "************************************************************************"

R4={"type":"plaster above brick in parallel","unit area":0.015,"length":0.16,"conductivity":0.22,"PaResValue":0}
R5={"type":"plaster below brick in parallel","unit area":0.015,"length":0.16,"conductivity":0.22,"PaResValue":0}
R6={"type":"brick","unit area":0.22,"length":0.16,"conductivity":0.72,"PaResValue":0}

ListOfPaRes=[R4,R5,R6]
totalPaRes_MutiplicativeInverse=0

for anyPaRes in ListOfPaRes:
    A_anyPaRes=anyPaRes["unit area"]
    L_anyPaRes=anyPaRes["length"]
    k_anyPaRes=anyPaRes["conductivity"]
    type_anyPaRes=anyPaRes["type"]
    RValue_anyPaRes= L_anyPaRes/( A_anyPaRes*k_anyPaRes)
    anyPaRes["PaResValue"]=RValue_anyPaRes
    print "   "
    print "here is the new resistance in parallel:"
    print anyPaRes
    print "      "
    print "so the resistance for " + str(type_anyPaRes) + " is " + str(RValue_anyPaRes)+" degC/W"
    totalPaRes_MutiplicativeInverse=totalPaRes_MutiplicativeInverse+1/RValue_anyPaRes
    totalPaRes=1/totalPaRes_MutiplicativeInverse

print "   "  
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"    
print "so the total resistance value in parallel is " + str(totalPaRes)+" degC/W" 
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"    
print "   "   

#caculating the convective resistance

print "************************************************************************"
print "               #This is the convective resistance#"
print "************************************************************************"
print "   "

R7={"type":"inner side","unit area":0.25,"htc":10,"ConResValue":0}
R8={"type":"outer side","unit area":0.25,"htc":25,"ConResValue":0}

ListOfConRes=[R7,R8]
totalConRes=0

for anyConRes in ListOfConRes:
    A_anyConRes=anyConRes["unit area"]
    h_anyConRes=anyConRes["htc"]
    type_anyConRes=anyConRes["type"]
    RValue_anyConRes=1/( h_anyConRes* A_anyConRes)
    anyConRes["ConResValue"]=RValue_anyConRes
    print "here is the new resistance: "
    print anyConRes
    print "         "
    print "so the Resistance Value for " + str(type_anyConRes) + " is: " + str(RValue_anyConRes) + " degC/W" 
    totalConRes=totalConRes+RValue_anyConRes
    print "    "
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"    
print "so the total convective resistance value is: " + str(totalConRes) + " degC/W" 
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"    
print "   "

#Total resistance of the wall

R=totalConRes+totalPaRes+totalSeRes
print "########################################################################"
print "so the total resistance of the wall is: " +str(R) + " degC/W"

T1=20 #The indoor temperature
T2=-10 #The outdoor temperature
Q0=(T1-T2)/R #The unit heat loss
print "so the unit heat loss of the wall is: " + str(Q0) + " W"
h=3 #total wall high
w=5 #total wall width
A=0.25 #unit area of the wall
Q=Q0*(h*w/A) #the total heat loss of the wall
print "so the total heat loss of the wall is: "+ str(Q) + " W"
print "########################################################################"