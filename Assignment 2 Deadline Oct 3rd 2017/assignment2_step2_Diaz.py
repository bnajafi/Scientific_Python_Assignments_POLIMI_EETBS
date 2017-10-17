#Dictionaries

#Conduction resistances in series

R1=[0.25,0.03,0.026] # foam layer
R2=[0.25,0.02,0.22] # plaster layer 1
R3=[0.25,0.02,0.22] # plaster layer 2

R1={"name":"foam","area":0.25,"length":0.03,"k":0.026,"REsValue":0} 
R2={"name":"plaster layer 1","area":0.25,"length":0.02,"k":0.22,"REsValue":0} 
R3={"name":"plaster layer 2","area":0.25,"length":0.02,"k":0.22,"REsValue":0} 
   

ListOfResistances1=[R1,R2,R3]

totalResValue1=0
for anyResistance1 in ListOfResistances1:  
    print("here is the new resistance ")
    L_anyResistance1=anyResistance1["length"]
    A_anyResistance1=anyResistance1["area"]
    k_anyResistance1=anyResistance1["k"]
    name_anyResistance1=anyResistance1["name"]
    Rvalue_anyResistance1= L_anyResistance1/(A_anyResistance1*k_anyResistance1)
    anyResistance1["ResValue"]=Rvalue_anyResistance1
    totalResValue1=totalResValue1+Rvalue_anyResistance1
    print ("the calculated resistance for "+name_anyResistance1+" is"+str(anyResistance1)) 
    print("******")
print("so the total resistance for conduction in series is "+str(totalResValue1)) 



#Conduction resistances in parallel

R4={"name":"plaster parallel 1","area":0.015,"length":0.16,"k":0.22,"REsValue2":0} 
R5={"name":"brick layer","area":0.22,"length":0.16,"k":0.72,"REsValue2":0} 
R6={"name":"plaster parallel 2","area":0.015,"length":0.16,"k":0.22,"REsValue2":0}




ListOfResistances2=[R4,R5,R6]

totalResValue2=0
for anyResistance2 in ListOfResistances2:
    print("here is the new resistance ")
    L_anyResistance2=anyResistance2["length"]
    A_anyResistance2=anyResistance2["area"]
    k_anyResistance2=anyResistance2["k"]
    name_anyResistance2=anyResistance2["name"]
    Rvalue_anyResistance2=1/((L_anyResistance2/(A_anyResistance2*k_anyResistance2)))
    anyResistance2["ResValue"]=Rvalue_anyResistance2
    totalResValue2=totalResValue2+Rvalue_anyResistance2
    totalResValue2p=1/totalResValue2
    print ("the calculated resistance for "+name_anyResistance2+" is"+str(anyResistance2))  
    print("******")
print("so the total resistance for conduction in parallel is "+str(totalResValue2p))



#Convection resistances 

R7={"name":"inside conv","area":0.25,"h":10,"REsValue3":0} 
R8={"name":"outside conv","area":0.25,"h":25,"REsValue3":0} 



ListOfResistances3=[R7,R8]

totalResValue3=0
for anyResistance3 in ListOfResistances3:
    print("here is the new resistance ")
    h_anyResistance3=anyResistance3["h"]
    A_anyResistance3=anyResistance3["area"]
    name_anyResistance3=anyResistance3["name"]
    Rvalue_anyResistance3= 1/(A_anyResistance3*h_anyResistance3)
    anyResistance3["ResValue3"]=Rvalue_anyResistance3
    print ("the calculated resistance for "+name_anyResistance3+" is"+str(anyResistance3)) 
    totalResValue3=totalResValue3+Rvalue_anyResistance3
    print("******")
print("so the total resistance for convection is "+str(totalResValue3))

heightw=3
widthw=5
Tin=20
Tout=-10
Awall=heightw*widthw
Aunit=0.25*1

Rtot_S=totalResValue1+totalResValue2p+totalResValue3
print("\n")
print("And the total resistance of the system is "+str(Rtot_S))
Qunit=(Tin-Tout)/Rtot_S


Qtot=Qunit*(Awall/Aunit)

print("\n")
print (  "The rate of heat transfer through the wall is  " + str (Qtot)+ " W" )
