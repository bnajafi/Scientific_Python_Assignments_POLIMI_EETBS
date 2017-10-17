# -*- coding: utf-8 -*-
Hw = 3 # wall height in m 
Ww = 5 # wall width in m
Awall = Hw*Ww # wall area
Tamb1 = 20 # room temperature in ºC
Tamb2 = -10 # outside temperature in ºC

# I will divide the wall in three sections: the foam section, the plaster/brick section and the two plaster sections together
# I will calculate the area for a unit of 1m of wide and then scale it to the actual wall

# Foam section
ReF={"depth":0.03,"area":0.25,"k":0.026}

# Plaster section
ReP={"depth":0.02,"area":0.25,"k":0.22}

# Brick/Plaster section
ReP1={"depth":0.16,"area":0.015,"k":0.22}
ReP2={"depth":0.16,"area":0.015,"k":0.22}
ReB={"depth":0.16,"area":0.22,"k":0.72}

#Calculating the parallel resistances
PR = [ReP1,ReP2,ReB]#Here are the resistances in parallel
TR = [0,0,0]#Here is the list where we store the results, first the parallel, then the series and in then the convective resistance
z=1

for i in PR:
    k=i["depth"]/(i["area"]*i["k"])
    z=1/((1/z)+(1/k))
    
TR[0]=1/((1/z)-1)

#Calculating the series resistances
SR = [ReP,ReP,ReF]
z=0
for i in SR:
    k=i["depth"]/(i["area"]*i["k"])
    z=z+k

TR[1]=z

#Calculating the resistance due to convection
Rh1 = {"area":0.25,"h":10}#for the room
Rh2 = {"area":0.25,"h":25}#for the outside
CR=[Rh1,Rh2]
z=0
for i in CR:
    k=1/(i["area"]*i["h"])
    z=z+k

TR[2]=z

# Now we have the resistance for the whole unit

Ru = TR[0]+TR[1]+TR[2]
print "The total resistance is " + str(Ru) + " ºC/W"

Qu = (Tamb1 - Tamb2)/Ru # we calculate the heat flux in the unit in W

print "The heat flux in a unit is " + str(Qu) + " W"

#we scale the heat flux using the areas

Q = Qu * Awall/ReF["area"] # in W
print "The total heat flux is " + str(Q) + " W"