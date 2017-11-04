#
total_resistance=0
totr=[0]
#convection

rci=[10,0.25]
rco=[25,0.25]
rconv=[rci,rco]
for rconv in rconv:
    totr.append(1/(rconv[0]*rconv[1]))

#parallel   
rpar1=[0.16,0.22,0.015]    
rpar2=[0.16,0.22,0.015]    
rpar3=[0.16,0.72,0.22]       
parallel=[rpar1,rpar2,rpar3]
rpar=0
for i in parallel:
    rpar+=(i[1]*i[2])/i[0]
rparallel=1/rpar
totr.append(rparallel)

#conduction 
rp1=[0.02,0.22,0.25]      
rp2=[0.02,0.22,0.25] 
rf=[0.03,0.026,0.25]
rcond=[rp1,rp2,rf]
for x in rcond:
    totr.append(x[0]/(x[1]*x[2]))

for i in totr:
    total_resistance+=i
    
T1=20
T2=-10
Q=(T1-T2)/total_resistance
print("total resistance is "+str(total_resistance)+ " C/W")
print("The total heat transfer of the wall is " +str(Q)+" W")
print ("The total heat transfer for the wall is "+ str((Q*15)/0.25))
    

