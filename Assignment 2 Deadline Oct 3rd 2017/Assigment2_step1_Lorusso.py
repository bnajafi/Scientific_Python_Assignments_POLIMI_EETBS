# -*- coding: utf-8 -*-
#wall dimension
y = 3 #Height
x = 5 #thickness
#resistence wall
Rbrick = [0.16,0.22,0.72]    #thickness,area,conducibility
Rplp1  = [0.16,0.015,0.22]
Rplp2  = Rplp1
Rpls1  = [0.02,0.25,0.22]
Rpls2  = Rpls1
Rfoam  = [0.03,0.25,0.026]
#convection heat transfer coefficents
hin  = 10  #W/(m^2 °C)
hout = 25  #W/(m^2 °C)
Rin  = [0.25,10] #inner side convective resistance
Rout = [0.25,25] #outer side convective resistence 
#Temperature
Tin  = 20 #indoor temperature °C
Tout = -10 #outdoor temperature °C
#lists of resistences
R_conv  = [Rin,Rout]
R_serie = [Rfoam,Rpls1,Rpls2]
R_paral = [Rplp1,Rbrick,Rplp2]
R_CONV=0
for i in R_conv:
    A_resistence = i[0]
    h_conv       = i[1]
    R_valueC     = 1/(h_conv*A_resistence)
    R_CONV       = R_CONV+R_valueC
print "Total convective resistece is:"+str(R_CONV)+("°C/W")
R_SERIE=0
for i in R_serie:
    x_resistence  = i[0]
    A_resistence  = i[1]
    k_serie       = i[2]
    R_valueS      = x_resistence/(k_serie*A_resistence)
    R_SERIE       = R_SERIE+R_valueS
print "Total serie resistece is:"+str(R_SERIE)+("°C/W")
R_PARAL=0
for i in R_paral:
    x_resistence  = i[0]
    A_resistence  = i[1]
    k_paral       = i[2]
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
