R1= {"name":"glass 1","area":1.5,"length":0.008,"k":0.78,"ResValue":0}

#
total_resistance=0
totr=[0]
#convection

rci={"name":"inside","area":0.25,"length":0,"h":10,"ResValue":0}
rco={"name":"outside","area":0.25,"length":0,"h":25,"ResValue":0}
rconv=[rci,rco]
for i in rconv:                     #
    h=i['h']
    a=i['area']
    i['ResValue']=1/(a*h)
    totr.append(1/(a*h))

#parallel   
rpar1={"name":"par1","area":0.015,"length":0.16,"k":0.22,"ResValue":0}   
rpar2={"name":"par2","area":0.015,"length":0.16,"k":0.22,"ResValue":0}  
rpar3={"name":"par3","area":0.22,"length":0.16,"k":0.72,"ResValue":0}      
parallel=[rpar1,rpar2,rpar3]
rpar=0
for i in parallel:
    a=i['area']
    k=i['k']
    l=i['length']
    
    rpar+=(k*a)/l
rparallel=1/rpar
totr.append(rparallel)

#conduction 
rp1={"name":"plaster 1","area":0.25,"length":0.02,"k":0.22,"ResValue":0}      
rp2={"name":"plaster 2","area":0.25,"length":0.02,"k":0.22,"ResValue":0} 
rf={"name":"brick","area":0.25,"length":0.03,"k":0.026,"ResValue":0} 
rcond=[rp1,rp2,rf]
for i in rcond:
    k=i['k']
    l=i['length']
    a=i['area']
    totr.append(l/(k*a))

for i in totr:
    total_resistance+=i
    
T1=20
T2=-10
Q=(T1-T2)/total_resistance
print("total resistance is "+str(total_resistance)+ " C/W")
print("The heat transfer for the specified unit of wall is " +str(Q)+" W")
print ("The total heat transfer for the wall is "+ str((Q*15)/0.25))
    

