#Lists

#Conduction resistances in series

R1=[0.25,0.03,0.026] # foam layer
R2=[0.25,0.02,0.22] # plaster layer 1
R3=[0.25,0.02,0.22] # plaster layer 2  

ListOfResistances1=[R1,R2,R3]

totalResValue1=0
for anyResistance1 in ListOfResistances1:
    print("here is the new resistance ")
    print (anyResistance1)
    L_anyResistance1=anyResistance1[1]
    A_anyResistance1=anyResistance1[0]
    k_anyResistance1=anyResistance1[2]
    Rvalue_anyResistance1= L_anyResistance1/(A_anyResistance1*k_anyResistance1)
    totalResValue1=totalResValue1+Rvalue_anyResistance1
    print ("the calculated resistance is "+str(Rvalue_anyResistance1)) 
    print("******")
print("so the total resistance for conduction in series is "+str(totalResValue1))

#Conduction resistances in parallel

R4=[0.015,0.16,0.22] # plaster parallel 1
R5=[0.22,0.16,0.72] # brick layer
R6=[0.015,0.16,0.22] # plaster parallel 2


ListOfResistances2=[R4,R5,R6]

totalResValue2=0
for anyResistance2 in ListOfResistances2:
    print("here is the new resistance ")
    print (anyResistance2)
    L_anyResistance2=anyResistance2[1]
    A_anyResistance2=anyResistance2[0]
    k_anyResistance2=anyResistance2[2]
    Rvalue_anyResistance2=1/((L_anyResistance2/(A_anyResistance2*k_anyResistance2)))
    totalResValue2=totalResValue2+Rvalue_anyResistance2
    totalResValue2p=1/totalResValue2
    print ("the calculated resistance is "+str(Rvalue_anyResistance2)) 
    print("******")
print("so the total resistance for conduction in parallel is "+str(totalResValue2p))



#Convection resistances 

R7=[0.25,10] # inside
R8=[0.25,25] # outside



ListOfResistances3=[R7,R8]

totalResValue3=0
for anyResistance3 in ListOfResistances3:
    print("here is the new resistance ")
    print (anyResistance3)
    h_anyResistance3=anyResistance3[1]
    A_anyResistance3=anyResistance3[0]
    Rvalue_anyResistance3= 1/(A_anyResistance3*h_anyResistance3)
    totalResValue3=totalResValue3+Rvalue_anyResistance3
    print ("the calculated resistance is "+str(Rvalue_anyResistance3)) 
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
