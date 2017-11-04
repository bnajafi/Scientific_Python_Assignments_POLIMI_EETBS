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
Hin = {"name": "in_convection", "area": 0.25, "coefficient": 10}
Hout = {"name": "out_convection", "area": 0.25, "coefficient": 25}

CONV = [Hin, Hout]

#the order corresponds to:
#[area, horizontal length, conductivity]
Rf = {"name":"foam series resistance", "area": 0.25,"length": 0.03,"k": 0.026} #foam
Rp1 = {"name":"plaster (1) series resistance", "area": 0.25,"length": 0.02,"k": 0.22}
Rp2 = {"name":"plaster (2) series resistance", "area": 0.25,"length": 0.02,"k": 0.22}

SERIES = [Rf, Rp1, Rp2]

#parallel
RPp1 = {"name":"plaster parallel resistance", "area": 0.015,"length": 0.16,"k": 0.22} #foam
RPb = {"name":"bricks parallel resistance", "area": 0.22,"length": 0.16,"k": 0.72} #foam
RPp2 = {"name":"plaster parallel resistance", "area": 0.015,"length": 0.16,"k": 0.22} #foam

PARALLEL = [RPp1, RPb, RPp2]

convection = 0
for anyelement in CONV:
    area = anyelement["area"]
    coefficient = anyelement["coefficient"]
    Rconv = 1/(area*coefficient)
    convection = convection + Rconv
    
print ("resistance due to convection is ") + str(convection)

series = 0
for aanyelement in SERIES:
    area = aanyelement["area"]
    length = aanyelement["length"]
    coefficient = aanyelement["k"]
    Rconv = length/(area*coefficient)
    series = series + Rconv
    
print ("series resistance due to conduction is ") + str(series)

paral = 0
for aaanyelement in PARALLEL:
    area = aaanyelement["area"]
    length = aaanyelement["length"]
    coefficient = aaanyelement["k"]
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

