# -*- coding: utf-8 -*-
#Wall's dimensions
H = 3 #Height [m]
W = 5 #Width [m]

#Temperatures#
T1 = 20 #Indoor temperature [°C]
T2 = -10 #Outdoor temperature [°C]

#convection heat transfer coefficients
h1 = 10 #inner side convection heat transfer coefficients [W/m2°C]
h2 = 25 #outer side convection heat transfer coefficients [W/m2°C]

#Resistences
Rb = [0.16,0.22,0.72] #brick
Rplp1 = [0.16,0.015,0.22] #first parallel plastic layer
Rplp2 = [0.16,0.015,0.22] #second parallel plastic layer
Rpls1 = [0.02,0.25,0.22] #first series plastic layer
Rpls2 = [0.02,0.25,0.22] #second series plastic layer
Rf = [0.03,0.25,0.026] #foam
Ri = [0.25,10] #inner side convective resistence
Re = [0.25,25] #outer side convective resistence

#Lists of resistences
R_conv = [Ri,Re]
R_serie = [Rf,Rpls1,Rpls2]
R_paral = [Rplp1,Rb,Rplp2]

R_CONV=0
for anyelement in R_conv:
    A_conv = anyelement[0]
    h_conv = anyelement[1]
    R_valueC = 1/(A_conv*h_conv)
    R_CONV= R_CONV + R_valueC
print "Total convective resistence is: "+str(R_CONV) +"°C/W"

R_SER=0
for anyelement in R_serie:
    W_serie = anyelement[0]
    A_serie = anyelement[1]
    K_serie = anyelement[2]
    R_valueS = W_serie/(A_serie*K_serie)
    R_SER= R_SER + R_valueS
print "Total series resistence is: "+str(R_SER) +"°C/W"

R_PAR=0
for anyelement in R_paral:
    W_paral = anyelement[0]
    A_paral = anyelement[1]
    K_paral = anyelement[2]
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