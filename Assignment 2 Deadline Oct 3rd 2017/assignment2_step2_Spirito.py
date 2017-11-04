 # Assignment 2 - Part 2 #
 
 #CALCULATE THE TOTAL WALL RESISTANCE AND THE HEAT TRANSFER RATE THROUGH THE WALL# 
 
 #conductive resistances in series#
 
R1= {"name":"foam","area":0.25,"lenght":0.03,"k":0.026}
R2= {"name":"vertical plaster layer 1","area":0.25,"lenght":0.02,"k":0.22}
R3= {"name":"vertical plaster layer 2","area":0.25,"lenght":0.02,"k":0.22}

condResistances_series = [R1,R2,R3]
TotalRes1=0
for Res in condResistances_series:
    L_Res= Res["lenght"]
    A_Res= Res["area"]
    k_Res= Res["k"]
    name_Res= Res["name"]
    ResValue= L_Res/(A_Res*k_Res)
    print "The calculated resistance of the "+name_Res+ " is "+str(ResValue)+" degC/W"
    TotalRes1= TotalRes1+ResValue
print "The total conductive resistance in series is "+str(TotalRes1)+ " degC/W" 
print "**************************************************************"

#conductive resistances in parallel#

R4= {"name":"brick","area":0.22,"lenght":0.16,"k":0.72}
R5= {"name":"horizontal plaster layer 1","area":0.015,"lenght":0.16,"k":0.22}
R6= {"name":"horizontal plaster layer 2","area":0.015,"lenght":0.16,"k":0.22}

condResistances_parallel = [R4,R5,R6]
TotalRes_rec=0
for Res in condResistances_parallel:
    L_Res= Res["lenght"]
    A_Res= Res["area"]
    k_Res= Res["k"]
    name_Res= Res["name"]
    ResValue= L_Res/(A_Res*k_Res)
    print "The calculated resistance of the "+name_Res+ " is "+str(ResValue)+" degC/W"
    Res_rec = 1/ResValue
    TotalRes_rec= Res_rec+TotalRes_rec
TotalRes2= 1/TotalRes_rec
print "The total conductive resistance in parallel is "+str(TotalRes2)+ " degC/W"
print "**************************************************************"

#convective resistances

R7= {"name":"inner side","area":0.25,"h":10}
R8= {"name":"outer side","area":0.25,"h":25}

convResistances= [R7,R8]
TotalRes3=0
for Res in convResistances:
    A_Res= Res["area"]
    h_Res= Res["h"]
    name_Res= Res["name"]
    ResValue= 1/(h_Res*A_Res)
    print "The calculated convective resistance of the "+name_Res+ " is "+str(ResValue)
    TotalRes3= TotalRes3+ResValue
print "The total convective resistance is "+str(TotalRes3)+ "degC/W"
print "**************************************************************"

TotalRes_wall=TotalRes1+TotalRes2+TotalRes3
print "The total resistance of the wall is "+str(TotalRes_wall)+ " degC/W"
print "**************************************************************"

T_in = 20
T_out = -10
A_wall = 15

Q_wall = ((T_in-T_out)/TotalRes_wall)*(A_wall/0.25)
print "The rate of heat transfer through the wall is "+str(Q_wall)+ "W" 



    

