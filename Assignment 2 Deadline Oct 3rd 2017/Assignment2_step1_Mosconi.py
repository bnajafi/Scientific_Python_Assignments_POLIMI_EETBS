Ri=[0.25,10] # indoor convective resistance A , h
Ro=[0.25,25] # outdoor convective resistance A , h


Rf=[0.25,0.03,0.026] # foam conductive resistance A , L , k
Rp1=[0.25,0.02,0.22] # plaster conductive resistance A , L , k
Rp2=[0.25,0.02,0.22] # plaster conductive resistance A , L , k


Rpc1=[0.015,0.16,0.22] # plaster conductive resistance A , L , k
Rb= [0.22,0.16,0.72] # brick conductive resistance A , L , k
Rpc2=[0.015,0.16,0.22] # plaster conductive resistance A , L , k

Res_conductive= [ Rf, Rp1 , Rp2] # list of conductive res in series
Res_convective= [Ri , Ro] # list of convective res in series
Res_parallel= [Rpc1 , Rb , Rpc2] # list of conductive res in parallel

R_cond=0
for i in Res_conductive:
    print "The conductive resistance"
    print (str(i))
    R= i[1]/(i[0]*i[2])
    print "The calculated resistance is: "+ str(R)
    R_cond= R_cond+R
    print("****************")
print("The value of conductive reistance in series is "+str(R_cond))    
print ("--------------")
R_conv=0
for i in Res_convective:
    print "The convective resistance"
    print (str(i))
    R= 1/(i[0]*i[1])
    print "The calculated resistance is: "+ str(R)
    R_conv= R_conv+R
    print("****************")
print("The value of convective reistance in series is "+str(R_conv))  
print ("--------------")

k=0
for i in Res_parallel:
    print "The conductive resistance"
    print (str(i))
    R= i[1]/(i[0]*i[2])
    print "The calculated resistance is: "+ str(R)
    k= k+R**(-1)
    print("****************")
R_parallel= k**(-1)    
print("The value of conductive resitance in parallel is "+str(R_parallel))
print ("--------------")

R_tot= R_cond+R_conv+R_parallel
T1=20
T2=-10
Q_unit=(T1-T2)/(R_tot)
A_wall=15
A_unit=0.25
Q_wall=Q_unit*A_wall/A_unit
print("The heat rate through the wall is "+str(Q_wall)+" W")