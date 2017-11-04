# -*- coding: utf-8 -*-
R1={"convectivity":10,"area":0.25}
R2={"convectivity":25,"area":0.25}
R_conv=[R1,R2]
Rconvtot=0
for R in R_conv:
    Rconv=1/(R["convectivity"]*R["area"])
    Rconvtot=Rconvtot+Rconv
print Rconvtot
Rf={"conductivity":0.026,"area":0.25,"thickness":0.03}   
Rp1={"conductivity":0.22,"area":0.25,"thickness":0.02}
Rp2=Rp1
Rc_series=[Rf,Rp1,Rp2]
Rcseries_tot=0
for R in Rc_series:
    Rcseries=R["thickness"]/(R["conductivity"]*R["area"])
    Rcseries_tot=Rcseries_tot+Rcseries
print Rcseries_tot   
Rpc1={"conductivity":0.22,"area":0.015,"thickness":0.16}
Rb={"conductivity":0.72,"area":0.22,"thickness":0.16}
Rpc2=Rpc1
Rc_par=[Rpc1,Rpc2,Rb]
Rtotinv=0
for R in Rc_par:
    Rcpar=R["thickness"]/(R["conductivity"]*R["area"])
    Rtotinv=Rtotinv+1/(Rcpar)
Rcpar_tot=1/(Rtotinv)    
print Rcpar_tot 
Rtot=Rcpar_tot+Rconvtot+Rcseries_tot
print "The total resistance of the wall is "+str(Rtot)+" °C/W"
T1=20
T2=-10
A=15
Q=(T1-T2)*A/(Rtot*0.25)
print "The rate of heat transfered trought the wall is "+str(Q)+" W"