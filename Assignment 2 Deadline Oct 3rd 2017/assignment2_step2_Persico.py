#series
R1={"name":"foam","area":0.25,"lenght":0.03,"k":0.026}
R2={"name":"verticalplaster1","area":0.25,"lenght":0.02,"k":0.22}
R3={"name":"verticalplaster2","area":0.25, "lenght":0.02,"k":0.22}

ListOfResistances_Series= [R1,R2,R3]
totres_series=0;

for Res in ListOfResistances_Series:
    L_Res= Res["lenght"]
    A_Res= Res["area"]
    k_Res= Res["k"]
    name_Res= Res["name"]
    ResValue= L_Res/(A_Res*k_Res)
    print"The resistance of "+str(name_Res)+" is: "+str(ResValue)+" degC/W" 
    totres_series = totres_series+ResValue
    print "***********"
print("The total resistance in series is: "+str(totres_series)+" degC/W") 

    
#parallel
R4={"name":"horizontalplaster1","area":0.015,"lenght":0.16,"k":0.22}
R5={"name":"brick","area":0.22,"lenght":0.16,"k":0.72}
R6={"name":"horizontalplaster2","area":0.015,"lenght":0.16,"k":0.22}

ListOfResistances_Parallel= [R4,R5,R6]
totres_rec=0;

for Res in ListOfResistances_Parallel:
    L_Res= Res["lenght"]
    k_Res= Res["k"]
    A_Res= Res["area"]
    name_Res= Res["name"]
    ResValue = L_Res/(k_Res*A_Res)
    print"The resistance of "+str(name_Res)+" is: "+str(ResValue)+" degC/W" 
    print "***********"
    Res_rec = 1/ResValue 
    totres_rec = totres_rec+Res_rec
totres_parallel=1/totres_rec
print("The total resistance in parallel is: "+str(totres_parallel)+" degC/W")  

# convective resistances 
R7= {"name":"innerside","area":0.25,"h":10}
R8= {"name":"outerside","area":0.25,"h":25}

ListOfResistances_Convective=[R7,R8]
totres_convective=0

for Res in ListOfResistances_Convective:
    h_Res= Res["h"]
    A_Res= Res["area"]
    name_Res= Res["name"]
    ResValue = 1/(h_Res*A_Res)
    print"The resistance of "+str(name_Res)+" is: "+str(ResValue)+" degC/W" 
    totres_convective = totres_convective+ResValue
    print "***********"
print("The total convective resistance is:"+str(totres_convective)+" degC/W") 

totres_wall=totres_series+totres_parallel+totres_convective
print "The total resistance of the wall is: "+str(totres_wall)+" degC/W"
print "***************"

Tin=20;
Tout=-10;
Q=(Tin-Tout)/totres_wall #Q of the unit area
print ("The rate of heat transfer through the wall per unit area is  "+str(Q)+" W")

Hwall=3 #Total height
Lwall=5 #Total width
Qwall=Q*(Lwall*Hwall)/0.25 #Q total
print ("The total rate of heat transfer through the wall is  "+str(Qwall)+" W")
