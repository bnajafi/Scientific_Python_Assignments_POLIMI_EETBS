#dictionaries
#convective resistances
Ri={"name":Ri, "heat transfer coefficient":10,"area":0.25, "ResValue":0}
Ro={"name":Ro, "heat transfer coefficient":25,"area":0.25, "ResValue":0}
listOfResistances1=[Ri,Ro]
totalRes1=0
for anyResistance in listOfResistances1:
    
    h_anyResistance=anyResistance["heat transfer coefficient"]
    A_anyResistance=anyResistance["area"]
    name_anyResistance=anyResistance["name"]
    resValue_anyResistance1=1/(h_anyResistance*A_anyResistance)
    anyResistance["ResValue"]=resValue_anyResistance1
    print "here is the new resistance: "
    print anyResistance
    totalRes1=totalRes1+resValue_anyResistance1
    print "so the calculated resistance for" " name_anyResistance " "is: " +str(resValue_anyResistance1)
    print "**********"
    
print "so the total resistance value is: "+str(totalRes1)

#conductive resistances in series
Rf={"name": Rf, "length":0.03,"conductivity":0.026, "area":0.25, "ResValue":0}
Rp1={"name": Rp1, "length":0.02,"conductivity":0.22, "area":0.25, "ResValue":0}      
Rp2={"name": Rp2, "length":0.02,"conductivity":0.22, "area":0.25, "ResValue":0}
listOfResistances2=[Rf,Rp1,Rp2]
totalRes2=0
for anyResistance in listOfResistances2:
    L_anyResistance=anyResistance["length"]
    k_anyResistance=anyResistance["conductivity"]
    A_anyResistance=anyResistance["area"]
    name_anyResistance=anyResistance["name"]
    resValue_anyResistance2=L_anyResistance/(k_anyResistance*A_anyResistance)
    anyResistance["ResValue"]=resValue_anyResistance2
    print "here is the new resistance: "
    print anyResistance
    totalRes2=totalRes2+resValue_anyResistance2
    print "so the calculated resistance for" " name_anyResistance " "is: " +str(resValue_anyResistance2)
    print "**********"
    
print "so the total resistance value is: "+str(totalRes2)

#conductive resistances in parallel
Rpc1={"name": Rpc1, "length":0.16,"conductivity":0.22, "area":0.015, "ResValue":0}
Rpc2={"name": Rpc2, "length":0.16,"conductivity":0.22, "area":0.015, "ResValue":0}
Rb={"name": Rb, "length":0.16,"conductivity":0.72, "area":0.22, "ResValue":0}
listOfResistances3=[Rpc1,Rpc2,Rb]
inv_totalRes3=0
for anyResistance in listOfResistances3:
    L_anyResistance=anyResistance["length"]
    k_anyResistance=anyResistance["conductivity"]
    A_anyResistance=anyResistance["area"]
    name_anyResistance=anyResistance["name"]
    resValue_anyResistance3=L_anyResistance/(k_anyResistance*A_anyResistance)
    anyResistance["ResValue"]=resValue_anyResistance3
    print "here is the new resistance: "
    print anyResistance
    print "so the calculated resistance for" " name_anyResistance " "is: " +str(resValue_anyResistance3)
    print "*************"
    inv_resValue_anyResystance3=1/(L_anyResistance/(k_anyResistance*A_anyResistance))
    inv_totalRes3=inv_totalRes3+inv_resValue_anyResystance3
    totalRes3=1/inv_totalRes3
print "so the total resistance value is: "+str(totalRes3)
print "*************"
        
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