 # Assignment 2 - Part 1 #
 
 #CALCULATE THE TOTAL WALL RESISTANCE AND THE HEAT TRANSFER RATE THROUGH THE WALL# 

# conductive resistances in series #

R1 = [0.03,0.026,0.25] #foam                     #length, conductivity k, area  
R2 = [0.02,0.22,0.25] #vertical plaster layer 1
R3 = [0.02,0.22,0.25] #vertical plaster layer 2

L_R1 = R1[0]
k_R1 = R1[1]
A_R1 = R1[-1]

Rvalue_R1 = L_R1/(k_R1*A_R1)

condResistances_series = [R1,R2,R3]   #list of conductive resistances in series
TotalRes1 = 0
for Res in condResistances_series:
    L_Res = Res[0]
    k_Res = Res[1]
    A_Res = Res[-1]
    ResValue = L_Res/(k_Res*A_Res)
    print "Here's the new calculated resistance: "+str(ResValue)
    TotalRes1 = TotalRes1+ResValue
print "The total conductive resistance in series is: "+str(TotalRes1)+" degC/W"
print "***************************************************************************"
# conductive resistances in parallel #

R4 = [0.16,0.22,0.015] #horizontal plaster layer 1        #length, conductivity k, area
R5 = [0.16,0.72,0.22] #brick
R6 = [0.16,0.22,0.015] #horizontal plaster layer 2

condResistances_parallel = [R4,R5,R6]
TotalRes_rec=0
for Res in condResistances_parallel:
    L_Res = Res[0]
    k_Res = Res[1]
    A_Res = Res[-1]
    ResValue = L_Res/(k_Res*A_Res)
    print "Here's the new calculated resistance: "+str(ResValue)
    Res_rec = 1/ResValue    #calcolo il reciproco di ciascuna resistenza
    print "Here's the reciprocal of the new calculated resistance: " +str(Res_rec)
    TotalRes_rec = TotalRes_rec + Res_rec 
TotalRes2 = 1/TotalRes_rec
print "The total conductive resistance in parallel is: "+str(TotalRes2)+" degC/W"
print "***************************************************************************"
    
# convective resistances #

R7 = [10,0.25] #inner convective resistance   #convection heat transfer coefficient, area
R8 = [25,0.25] #outer convective resistance

convResistances = [R7,R8]
TotalRes3= 0 
for Res in convResistances:
    h_Res = Res[0]
    A_Res = Res[-1]
    ResValue = 1/(h_Res*A_Res)
    print "Here's the new calculated resistance: "+str(ResValue)
    TotalRes3 = TotalRes3+ResValue
print "The total convective resistance is: "+str(TotalRes3)+" degC/W"
print "********************************************************************"
    
TotalRes_wall = TotalRes1+TotalRes2+TotalRes3    
print "The total resistance of the wall is: "+str(TotalRes_wall)+" degC/W"
print "********************************************************************"

T_in = 20
T_out = -10
A_wall = 15

Q_wall = ((T_in-T_out)/TotalRes_wall)*(A_wall/0.25)
print "The rate of heat transfer through the wall is "+str(Q_wall)+ "W" 