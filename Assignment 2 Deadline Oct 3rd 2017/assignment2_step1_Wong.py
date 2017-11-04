# -*- coding: utf-8 -*-
Hw = 3 # wall height in m 
Ww = 5 # wall width in m
Awall = Hw*Ww # wall area
Tamb1 = 20 # room temperature in ºC
Tamb2 = -10 # outside temperature in ºC

# I will divide the wall in three sections: the foam section, the plaster/brick section and the two plaster sections together
# I will calculate the area for a unit of 1m of wide and then scale it to the actual wall

# Foam section
ReF=[0.03,0.25,0.026]#depth,area,conduction coefficient

# Plaster section
ReP=[0.02,0.25,0.22]#depth,area,conduction coefficient

# Brick/Plaster section
ReP1=[0.16,0.015,0.22]#depth,area,conduction coefficient of plaster 1
ReP2=[0.16,0.015,0.22]#depth,area,conduction coefficient of plaster 2
ReB=[0.16,0.22,0.72]#depth,area,conduction coefficient of brick

#Calculating the parallel resistances
PR = [ReP1,ReP2,ReB]#Here are the resistances in parallel
TR = [0,0,0]#Here is the list where we store the results, first the parallel, then the series and in then the convective resistance
z=1

for i in PR:
    k=i[0]/(i[1]*i[2])
    z=1/((1/z)+(1/k))
    
TR[0]=1/((1/z)-1)

#Calculating the series resistances
SR = [ReP,ReP,ReF]
z=0
for i in SR:
    k=i[0]/(i[1]*i[2])
    z=z+k

TR[1]=z

#Calculating the resistance due to convection
Rh1 = [0.25,10]#area and convection coefficient for the room
Rh2 = [0.25,25]#area and convection coefficient for the outside
CR=[Rh1,Rh2]
z=0
for i in CR:
    k=1/(i[0]*i[1])
    z=z+k

TR[2]=z

# Now we have the resistance for the whole unit

Ru = TR[0]+TR[1]+TR[2]
print "The total resistance is " + str(Ru) + " ºC/W"

Qu = (Tamb1 - Tamb2)/Ru # we calculate the heat flux in the unit in W

print "The heat flux in a unit is " + str(Qu) + " W"

#we scale the heat flux using the areas

Q = Qu * Awall/ReF[1] # in W
print "The total heat flux is " + str(Q) + " W"