# -*- coding: utf-8 -*-
#Wall's dimensions
H = 3 #Height [m]
W = 5 #Width [m]

#Temperatures#
T1 = 20 #Indoor temperature [°C]
T2 = -10 #Outdoor temperature [°C]

#convection heat transfer coefficients
h1 = 10 #inner side convection heat transfer coefficient [W/m2°C]
h2 = 25 #outer side convection heat transfer coefficient [W/m2°C]

#Resistences
Ri = {"name":"inner side convective resistence","Area":0.25,"h":10}
Re = {"name":"outer side convective resistence","Area":0.25,"h":25}
Rb = {"name":"brick","thickness":0.16,"Area":0.22,"k":0.72}
Rplp1 = {"name":"first parallel plastic layer","thickness":0.16,"Area":0.015,"k":0.22}
Rplp2 = {"name":"second parallel plastic layer","thickness":0.16,"Area":0.015,"k":0.22}
Rpls1 = {"name":"first series plastic layer","thickness":0.02,"Area":0.25,"k":0.22}
Rpls2 = {"name":"second series plastic layer","thickness":0.02,"Area":0.25,"k":0.22}
Rf = {"name":"foam","thickness":0.03,"Area":0.25,"k":0.026}

#Lists of resistences
R_conv = [Ri,Re]
R_serie = [Rf,Rpls1,Rpls2]
R_paral = [Rplp1,Rb,Rplp2]

R_CONV=0
for anyelement in R_conv:
    A_conv = anyelement["Area"]
    h_conv = anyelement["h"]
    R_valueC = 1/(A_conv*h_conv)
    R_CONV= R_CONV + R_valueC
print "Total convective resistence is: "+str(R_CONV) +"°C/W"

R_SER=0
for anyelement in R_serie:
    W_serie = anyelement["thickness"]
    A_serie = anyelement["Area"]
    K_serie = anyelement["k"]
    R_valueS = W_serie/(A_serie*K_serie)
    R_SER= R_SER + R_valueS
print "Total series resistence is: "+str(R_SER) +"°C/W"

R_PAR=0
for anyelement in R_paral:
    W_paral = anyelement["thickness"]
    A_paral = anyelement["Area"]
    K_paral = anyelement["k"]
    R_P = W_paral/(A_paral*K_paral)
    R_valueP = 1/R_P
    R_PAR= R_PAR + R_valueP
print "Total parallel resistence is: "+str(R_PAR) +"°C/W"

R_tot = R_CONV + R_SER + R_PAR
print "Total resistence is: " +str(R_tot) + "°C/W"

q = (T1-T2)/R_tot
A = H*W
Q = A*q/0.25

print ("Total heath flow is ")+str(Q) + ("W")
