# -*- coding: utf-8 -*-
Hw = float(raw_input("Specify the wall height")) # wall height in m 
Ww = float(raw_input("Specify the wall width")) # wall width in m
Awall = Hw*Ww # wall area
Tamb1 = float(raw_input("Specify the room temperature")) # room temperature in ºC
Tamb2 = float(raw_input("Specify the outside temperature")) # outside temperature in ºC
h1 = float(raw_input("Specify the convection coefficient of the room")) # convection coefficient of room in W/m2·K
h2 = float(raw_input("Specify the convection coefficient of the outside")) # convection coefficient of outside in W/m2·K
kb = float(raw_input("Specify the conduction coefficient of brick")) # conduction coefficient of brick in W/mK
kp = float(raw_input("Specify the conduction coefficient of plaster")) # conduction coefficient of plaster in W/mK
kf = float(raw_input("Specify the conduction coefficient of foam")) # conduction coefficient of foam in W/mK

# I will divide the wall in three sections: the foam section, the plaster/brick section and the two plaster sections together
# I will calculate the area for a unit of 1m of wide and then scale it to the actual wall
print "For the foam section"
# Foam section
Lf = float(raw_input("Specify the foam depth")) # foam depth in m
Af = float(raw_input("Specify the foam height")) # foam area in m2
Rf = Lf/(kf*Af)
print "For the plaster section"
# Plaster section
Lp = float(raw_input("Specify the plaster depth")) # plaster depth in m
Ap = float(raw_input("Specify the plaster height")) # plaster area in m2
Rp = 2*Lp/(kp*Ap)

print "For the Brick/plaster section"

# Brick/Plaster section
Lpb = float(raw_input("Specify the plaster depth")) # plaster depth in m
Apb = float(raw_input("Specify the plaster height")) # plaster area in m2
Lb = float(raw_input("Specify the brick depth")) # brick depth in m
Ab = float(raw_input("Specify the brick height")) # brick area in m2
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