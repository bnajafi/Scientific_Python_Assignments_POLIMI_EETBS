#*****Areas are pre-calculated for ease, all units are in SI******
Rci=[10,0.25]             #Defining Convective resistance on the inner side as a list in(h,A) order
Rco=[25,0.25]             #Defining Convective resistance on the outer side as a list in(h,A) order
Rf=[0.03,0.026,0.25]      #Defining Conducive resistance of foam as a list in(L,k,A) order
Rp1=[0.02,0.22,0.25]      #Defining Conductive resistance of Plaster side1 as a list in (L,k,A) order
Rp2=[0.02,0.22,0.25]      #Defining Conductive resistance of Plaster side2 as a list in (L,k,A) order
Rpc1=[0.16,0.22,0.015]    #Defining Conductive resistance of Plaster ceilingside1 as a list in (L,k,A) order
Rpc2=[0.16,0.22,0.015]    #Defining Conductive resistance of Plaster ceilingside2 as a list in (L,k,A) order
Rb=[0.16,0.72,0.22]       #Defining Conductive resistance of Brick as a list in (L,k,A) order
ConvReS=[Rci,Rco]         #Defining covective resistances in series as a list where list items are also a list
CondReS=[Rf,Rp1,Rp2]      #Defining coductive resistances in series as a list where list items are also a list
CondReP=[Rpc1,Rpc2,Rb]    #Defining covective resistances in parallel as a list where list items are also a list
TotalConvReS=0            #Intializing total value of convective resistances as zero
TotalCondReS=0            #Intializing total value of conductive resistances in series as zero
TotalCondReP=0            #Intializing total value of conductive resistances in parallel as zero
for r in range(len(ConvReS)):
    TotalConvReS+=1/(r[0]*r[1])                                     #Calculating the total resistance value of convective resistances in series   
for p in range(len(CondReS)):
    TotalCondReS+=p[0]/(p[1]*p[2])                         #Calculating the total resistance value of conductive resistances in series    
for s in range(len(CondReP)):
    TotalCondReP+=1/((s[0]/(s[1]*s[2])))                   #Calculating the total resistance value of conductive resistances in parallel    
TotalCondReP=1/TotalCondReP                                                           #Inversing the value for parallel resistances and assigning again to the old variable
TotalRes=round((TotalConvReS+TotalCondReS+TotalCondReP ),2)                           #Calculating the effective total resistance value
T1=273+20                                                                             #in K, Indoor temperature
T2=273-10                                                                             #in K, Outdoor temperature
Unit=(3*5)/0.25                                                                       #Total number of units
Qtotal=int(Unit*((T1-T2)/TotalRes))                                                   #in Watt, Total heat transfer rate
print("The total effective thermal resistance is: "+str(TotalRes)+" degK/W")                  
print("The rate of heat transfer through the wall is "+str(Qtotal)+" Watt")