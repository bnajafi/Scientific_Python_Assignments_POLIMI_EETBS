# -*- coding: utf-8 -*-
#O Muse, o alto ingegno, or m'aiutate
#o mente, che scrivesti ciò ch'io vidi
#qui si parrà la tua nobilitate

#data
width = 5
height = 3 
Tin = 20
Tout= -10

#convection
#area, coefficient
Hin = [0.25, 10]
Hout = [0.25, 25]

CONV = [Hin, Hout]

#the order corresponds to:
#[area, horizontal length, conductivity]
Rf = [0.25, 0.03, 0.026] #foam
Rp1 = [0.25, 0.02, 0.22]
Rb = [0.25, 0.16, 0.72]
Rp2 = [0.25, 0.02, 0.22]

SERIES = [Rf, Rp1, Rp2]

#parallel
R_f1 = [0.015, 0.16, 0.22]
R_b = [0.22, 0.16, 0.72]
R_f2 = [0.015, 0.16, 0.22]

PARALLEL = [R_f1, R_b, R_f2]

convection = 0
for anyelement in CONV:
    area = anyelement[0]
    coefficient = anyelement[1]
    Rconv = 1/(area*coefficient)
    convection = convection + Rconv
    
print ("resistance due to convection is ") + str(convection)

series = 0
for aanyelement in SERIES:
    area = aanyelement[0]
    length = aanyelement[1]
    coefficient = aanyelement[2]
    Rconv = length/(area*coefficient)
    series = series + Rconv
    
print ("series resistance due to conduction is ") + str(series)

paral = 0
for aaanyelement in PARALLEL:
    area = aaanyelement[0]
    length = aaanyelement[1]
    coefficient = aaanyelement[2]
    Rpar = length/(area*coefficient)
    paral = paral + 1/Rpar
parallel = 1/paral
    
print ("parallel resistance due to conduction is ") + str(parallel)
Rtot = convection + series + parallel
print ("total resistance is ") +str(Rtot) + (" C°/W")
Qarea = (Tin - Tout)/Rtot
print ("heath flow per area unit is ") +str(Qarea) +("W/ m^2")
area= width*height
Q = area * Qarea / 0.25
print ("heath flow is ")+str(Q) + ("W")

