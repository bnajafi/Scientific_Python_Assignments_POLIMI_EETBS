# -*- coding: utf-8 -*-
Hw = 3 # wall height in m 
Ww = 5 # wall width in m
Awall = Hw*Ww # wall area
Tamb1 = 20 # room temperature in ºC
Tamb2 = -10 # outside temperature in ºC
h1 = 10 # convection coefficient of room in W/m2·ºC
h2 = 25 # convection coefficient of outside in W/m2·ºC
kb = 0.72 # conduction coefficient of brick in W/m·ºC
kp = 0.22 # conduction coefficient of plaster in W/m·ºC
kf = 0.026 # conduction coefficient of foam in W/m·ºC

# I will divide the wall in three sections: the foam section, the plaster/brick section and the two plaster sections together
# I will calculate the area for a unit of 1m of wide and then scale it to the actual wall

# Foam section
Lf = 0.03 # foam depth in m
Af = 0.25 # foam area in m2
Rf = Lf/(kf*Af)

# Plaster section
Lp = 0.02 # plaster depth in m
Ap = 0.25 # plaster area in m2
Rp = 2*Lp/(kp*Ap)

# Brick/Plaster section
Lpb = 0.16 # plaster depth in m
Apb = 0.015 # plaster area in m2
Lb = 0.16 # brick depth in m
Ab = 0.22 # brick area in m2
Rpb = 1/(((2*kp*Apb)/Lpb)+((kb*Ab)/Lb))

# to calculate the total conductive resistances we add all the resistances

Rc = Rpb + Rf + Rp

# Now we add the resistance due to convection

Rh1 = 1/(Af*h1)
Rh2 = 1/(Ap*h2)

# Now we have the resistance for the whole unit

Ru = Rh1 + Rh2 + Rc
print "The total resistance is " + str(Ru) + " ºC/W"

Qu = (Tamb1 - Tamb2)/Ru # we calculate the heat flux in the unit in W

print "The heat flux in a unit is " + str(Qu) + " W"

#we scale the heat flux using the areas

Q = Qu * Awall/Af # in W
print "The total heat flux is " + str(Q) + " W"