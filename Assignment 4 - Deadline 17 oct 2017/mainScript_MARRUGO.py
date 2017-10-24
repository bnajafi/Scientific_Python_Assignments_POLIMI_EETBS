#      Assigment 4 Functions for Calculation the heating load factor (HF) 
#             and the total heating load (Q-heating) 

print """Assigment 4 Functions for Calculation the heating load factor (HF) 
                and the total heating load (Q-heating) \n"""

import wallCalculations_MARRUGO as WC

# List of materials of the wall in series 
ListS=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting","Common_brick",
"Glass_fiber_insulation","Gypsum_wallboard"]

# List of materials of the wall in parallel 
ListP=["Wood_bevel_lapped_siding","Wood_fiberboard_sheeting","Common_brick",
"Wood stud","Gypsum_wallboard"]

# List of materials of the door in series 
ListD=["Wood"]

# List of materials of the roof in series 
ListR=["Asphalt_shingle_roofing","Plywood","Glass_fiber_insulation"]

#Using Wall functions to calculate the U-Factor according with the list of materials
walll=WC.matParallel(ListS,ListP,0.70)
door=WC.matSeries(ListD)
roof=WC.matSeries(ListR)

# Compute the delta of temperature in winter
TlowPiacenza=(-4.8)
Dtheating=20.0-(TlowPiacenza)

# Compute the Heating load factor in [W/m2]
Hfwall=(walll["Utotal_winter"])*Dtheating
Hfdoor=(door["Utotal_winter"])*Dtheating
Hfroof=(roof["Utotal_winter"])*Dtheating

# Defining the Areas of each element
length=20
width=10
height=2.4

AreaNonOpaque=14.4+14.4+7.2
AreaDoor=1*2.2
AreaRoof=length*width
AreaWall=((length*height)*2)+((width*height)*2)-AreaDoor-AreaNonOpaque

# Compute the Heating load of each element 
QheatWall=AreaWall*Hfwall
QheatDoor=AreaDoor*Hfdoor
QheatRoof=AreaRoof*Hfroof

# Compute the Total Heating load
QHeatingTotal=QheatWall+QheatDoor+QheatRoof

print "The Heating load of the wall is ",QheatWall,"W/m2 \n"
print "The Heating load of the door in W/m2 is ",QheatDoor,"W/m2 \n"
print "The Heating load of the roof in W/m2 is ",QheatRoof,"W/m2 \n"
print "The Total Heating load of the elements is ",QHeatingTotal,"W/m2 \n"