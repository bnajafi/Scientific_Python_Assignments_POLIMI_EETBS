#series
R1=[0.03,0.026,0.25] #foam    #length, conductivity k, area  
R2=[0.02,0.22,0.25] #verticalplaster1
R3=[0.02,0.22,0.25] #verticalplaster2


ListOfResistances_Series= [R1,R2,R3]
totres_series=0;

for Res in ListOfResistances_Series:
    L_Res = Res[0]
    k_Res = Res[1]
    A_Res = Res[-1]
    ResValue = L_Res/(k_Res*A_Res)
    print"The resistance is: "+str(ResValue)+" degC/W" 
    totres_series = totres_series+ResValue
    print "***********"
print("The total resistance in series is: "+str(totres_series)+" degC/W") 
    

#parallel
R4=[0.16,0.22,0.015] #horizontalplaster1
R5=[0.16,0.72,0.22]  #brick
R6=[0.16,0.22,0.015] #horizontalplaster2

ListOfResistances_Parallel= [R4,R5,R6]
totres_rec=0;

for Res in ListOfResistances_Parallel:
    L_Res = Res[0]
    k_Res = Res[1]
    A_Res = Res[-1]
    ResValue = L_Res/(k_Res*A_Res)
    print"The resistance is: "+str(ResValue)+" degC/W" 
    print "***********"
    Res_rec = 1/ResValue 
    totres_rec = totres_rec+Res_rec
totres_parallel=1/totres_rec
    
print("The total resistance in parallel is: "+str(totres_parallel)+" degC/W") 


# convective resistances 

R7 = [10,0.25] #inner convective resistance   #convection heat transfer coefficient, area
R8 = [25,0.25] #outer convective resistance    

ListOfResistances_Convective=[R7,R8]
totres_convective=0

for Res in ListOfResistances_Convective:
    h_Res = Res[0]
    A_Res = Res[-1]
    ResValue = 1/(h_Res*A_Res)
    print"The resistance is: "+str(ResValue)+" degC/W" 
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
