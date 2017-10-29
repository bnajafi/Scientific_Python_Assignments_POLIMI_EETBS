#Dictionaries format

#Conduction resistances in series

Rf={"name":"foam","area":0.25,"length":0.03,"k":0.026,"REsValue":0} 
Rp1={"name":"plaster layer 1","area":0.25,"length":0.02,"k":0.22,"REsValue":0} 
Rp2={"name":"plaster layer 2","area":0.25,"length":0.02,"k":0.22,"REsValue":0} 
   

R_Cond_S=[Rf,Rp1,Rp2]

total_Re=0
for any_RS in R_Cond_S:  
    print("here is the new resistance ")
    L_anyResistance1=any_RS["length"]
    A_anyResistance1=any_RS["area"]
    k_anyResistance1=any_RS["k"]
    name_anyResistance1=any_RS["name"]
    Rvalue_anyResistance1= L_anyResistance1/(A_anyResistance1*k_anyResistance1)
    any_RS["ResValue"]=Rvalue_anyResistance1
    total_Re=total_Re+Rvalue_anyResistance1
    print ("the calculated resistance for "+name_anyResistance1+" is"+str(any_RS)) 
    print("******")
print("so the total resistance for conduction in series is "+str(total_Re)) 



#Convection resistances in series 

Rconv1={"name":"inside conv","area":0.25,"h":10,"REsValue2":0} 
Rconv2={"name":"outside conv","area":0.25,"h":25,"REsValue2":0} 



ListOfResistances2=[Rconv1,Rconv2]

total_Re2=0
for any_Re2 in ListOfResistances2:
    print("here is the new resistance ")
    h_anyResistance2=any_Re2["h"]
    A_anyResistance2=any_Re2["area"]
    name_anyResistance2=any_Re2["name"]
    Rvalue_anyResistance2= 1/(A_anyResistance2*h_anyResistance2)
    any_Re2["ResValue2"]=Rvalue_anyResistance2
    print ("the calculated resistance for "+name_anyResistance2+" is"+str(any_Re2)) 
    total_Re2=total_Re2+Rvalue_anyResistance2
    print("******")
print("so the total resistance for convection is "+str(total_Re2))

#Conduction resistances in parallel

Rbp1={"name":"plaster parallel 1","area":0.015,"length":0.16,"k":0.22,"REsValue3":0} 
Rb={"name":"brick layer","area":0.22,"length":0.16,"k":0.72,"REsValue3":0} 
Rbp2={"name":"plaster parallel 2","area":0.015,"length":0.16,"k":0.22,"REsValue3":0}




ListOfResistances3=[Rbp1,Rb,Rbp2]

total_Re3=0
for any_Re3 in ListOfResistances3:
    print("here is the new resistance ")
    L_anyResistance3=any_Re3["length"]
    A_anyResistance3=any_Re3["area"]
    k_anyResistance3=any_Re3["k"]
    name_anyResistance3=any_Re3["name"]
    Rvalue_anyResistance3=1/((L_anyResistance3/(A_anyResistance3*k_anyResistance3)))
    any_Re3["ResValue3"]=Rvalue_anyResistance3
    total_Re3=total_Re3+Rvalue_anyResistance3
    total_Re3p=1/total_Re3
    print ("the calculated resistance for "+name_anyResistance3+" is"+str(any_Re3))  
    print("******")
print("so the total resistance for conduction in parallel is "+str(total_Re3p))

h_wall=3
W_wall=5
T_in=20
T_out=-10
Awall=h_wall*W_wall
Aunit=0.25*1

R_tot=total_Re+total_Re2+total_Re3p
print("******************")
print("And the total resistance of the system is "+str(R_tot))
Q_unit=(T_in-T_out)/R_tot


Q_tot=Q_unit*(Awall/Aunit)

print("**************")
print (  "The rate of heat transfer through the wall is  " + str (Q_tot)+ " W" )
