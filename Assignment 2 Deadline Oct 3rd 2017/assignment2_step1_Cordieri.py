# -*- coding: utf-8 -*-
R1=[10,0.25] #convectivity,area
R2=[25,0.25] #convectivity,area
R_conv=[R1,R2]
Rconvtot=0
for R in R_conv:
    Rconv=1/(R[0]*R[1])
    Rconvtot=Rconvtot+Rconv
Rf=[ 0.026,0.25,0.03]   #conductivity,area,thickness
Rp1=[0.22,0.25,0.02]    #conductivity,area,thickness
Rp2=Rp1
Rc_series=[Rf,Rp1,Rp2]
Rcseries_tot=0
for R in Rc_series:
    Rcseries=R[2]/(R[0]*R[1])
    Rcseries_tot=Rcseries_tot+Rcseries  
Rpc1=[0.22,0.015,0.16]  #conductivity,area,thickness
Rpc2=Rpc1               #conductivity,area,thickness
Rb=[0.72,0.22,0.16]
Rc_par=[Rpc1,Rpc2,Rb]
Rtotinv=0
for R in Rc_par:
    Rcpar=R[2]/(R[0]*R[1])
    Rtotinv=Rtotinv+1/(Rcpar)
Rcpar_tot=1/(Rtotinv)    
Rtot=Rcpar_tot+Rconvtot+Rcseries_tot
print "The total resistance of the wall is "+str(Rtot)+" °C/W"
T1=20
T2=-10
A=15
Q=(T1-T2)*A/(Rtot*0.25)
print "The rate of heat transfered trought the wall is "+str(Q)+" W"