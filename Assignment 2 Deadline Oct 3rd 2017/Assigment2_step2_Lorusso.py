# -*- coding: utf-8 -*-
#wall dimension
y = 3 #Height
x = 5 #thickness
#convection heat transfer coefficents
hin  = 10  #W/(m^2 °C)
hout = 25  #W/(m^2 °C)
#Temperature
Tin  = 20 #indoor temperature °C
Tout = -10 #outdoor temperature °C
#Resistences
Rin    = {"name":"inner side convective resistence","area":0.25,"h":10}
Rout   = {"name":"outer side convective resistence","area":0.25,"h":25}
Rbrick = {"name":"brick","thickness":0.16,"area":0.22,"k":0.72}
Rplp1  = {"name":"first parallel plastic layer","thickness":0.16,"area":0.015,"k":0.22}
Rplp2  = {"name":"second parallel plastic layer","thickness":0.16,"area":0.015,"k":0.22}
Rpls1  = {"name":"first series plastic layer","thickness":0.02,"area":0.25,"k":0.22}
Rpls2  = {"name":"second series plastic layer","thickness":0.02,"area":0.25,"k":0.22}
Rfoam  = {"name":"second series plastic layer","thickness":0.03,"area":0.25,"k":0.026}
#lists of resistences
R_conv  = [Rin,Rout]
R_serie = [Rfoam,Rpls1,Rpls2]
R_paral = [Rplp1,Rbrick,Rplp2]
R_CONV=0
for i in R_conv:
    A_resistence = i["area"]
    h_conv       = i["h"]
    R_valueC     = 1/(h_conv*A_resistence)
    R_CONV       = R_CONV+R_valueC
print "Total convective resistece is:"+str(R_CONV)+("°C/W")
R_SERIE=0
for i in R_serie:
    x_resistence  = i["thickness"]
    A_resistence  = i["area"]
    k_serie       = i["k"]
    R_valueS      = x_resistence/(k_serie*A_resistence)
    R_SERIE       = R_SERIE+R_valueS
print "Total serie resistece is:"+str(R_SERIE)+("°C/W")
R_PARAL=0
for i in R_paral:
    x_resistence  = i["thickness"]
    A_resistence  = i["area"]
    k_paral       = i["k"]
    R_valueP      = x_resistence/(k_paral*A_resistence)
    Rinv          = 1/R_valueP
    R_PARAL       = R_PARAL+Rinv
    print "Total parallel resistece is:"+str(R_PARAL)+("°C/W")
R_total =R_CONV+R_SERIE+R_PARAL
print "total resistance is:"+str(R_total)+("°C/W")
q= (Tin-Tout)/R_total
A=x*y
Q= A*q/0.25
print "total heat flow is:"+str(Q)+("W")
