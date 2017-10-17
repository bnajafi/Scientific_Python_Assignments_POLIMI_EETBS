# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:25:45 2017

@author: edoua
"""

#conduction constante

kbrick = 0.72           
kplaster = 0.22
kfoam = 0.026

Lbrick = 0.16     #brick width
lbrick = 0.22     #brick length
Lplaster = 0.02    #plaster width (in the same sens than the brick)
lplaster = 0.015  #plaster length
Lfoam = 0.03       #foam width
lfoam = 2 * lplaster + lbrick   #foam length
d = 1           #Wall depth

Tin = 20        #Interior temperature
Tout = -10      #Exterior temperature
h1 = 10
h2 = 25

A = (lfoam * d) #area energy passing by
Awall = 3 * 5   #wall area

# Calculation of the resitances

R1 = 1 / (h1 * A)
R2 = 1 / (h2 * A)
Rf = Lfoam / (kfoam * A)
Rp1 = Lplaster / (kplaster * A)
Rp2 = Lplaster / (kplaster * A)
Rpc1 = Lbrick / (kplaster * lplaster * d)
Rpc2 = Lbrick / (kplaster * lplaster * d)
Rb = Lbrick / (kbrick * lbrick * d)

Rpara = 1 / ((1/Rb) + (1/Rpc1) + (1/Rpc2))      #Sum of Resistances in parallel

Rtot = R1 + R2 + Rf+ Rpara + Rp1 + Rp2          #Sum of resistances in "?"

print "The value of the total resistance is " + str(Rtot) + "°C/W"

Qunit = (Tin - Tout)/ Rtot          #heat transfer for one unit of the wall
Qwall = Qunit * Awall/A

print "The value of the heat transfer across the wall is " + str(Qwall) + " W"


