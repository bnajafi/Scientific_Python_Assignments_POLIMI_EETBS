# ASSIGNMENT 5 - part 2 #

import numpy as np

material_names=np.array(["outsideSurfaceWinter","insideSurface","woodStud_90mm","woodFiberboard_13mm",
"woodBevelLapped","gypsum","glassfiberInsulation_90mm"])
layers_types=  np.array(["onlyInSeries","onlyInSeries","parallel_atStuds","parallel_inCommon","parallel_inCommon","parallel_inCommon","parallel_betweenStuds"]) 
material_resistances= np.array([0.030,0.12,0.63,0.23,0.14,0.079,2.45])

ResValues_onlyInSeries= np.array(np.zeros(7))
ResValues_parallel_atStuds= np.array(np.zeros(7))
ResValues_parallel_betweenStuds= np.array(np.zeros(7))

condition_onlyInSeries=(layers_types=="onlyInSeries")

ResValues_onlyInSeries[condition_onlyInSeries]=material_resistances[condition_onlyInSeries] 
Rtot_onlyInSeries=ResValues_onlyInSeries.sum()


condition_parallel_atStuds= ((layers_types== "parallel_atStuds") | (layers_types== "parallel_inCommon") )
ResValues_parallel_atStuds[condition_parallel_atStuds]=material_resistances[condition_parallel_atStuds] 
Rtot_parallel_atStuds=ResValues_parallel_atStuds.sum()


condition_parallel_betweenStuds= ((layers_types== "parallel_betweenStuds") | (layers_types== "parallel_inCommon") )
ResValues_parallel_betweenStuds[condition_parallel_betweenStuds]=material_resistances[condition_parallel_betweenStuds] 
Rtot_parallel_betweenStuds=ResValues_parallel_betweenStuds.sum()

# let's calculate U

Rtot_atStuds= Rtot_onlyInSeries + Rtot_parallel_atStuds
Rtot_betweenStuds= Rtot_onlyInSeries + Rtot_parallel_betweenStuds 

U_atStuds=1/Rtot_atStuds
U_betweenStuds=1/Rtot_betweenStuds

f_insulation= 0.75
f_stud= 0.25
U_wall= U_atStuds*f_stud + U_betweenStuds*f_insulation
print "THE OVERALL HEAT TRANSFER COEFFICIENT U OF THE WALL IS: "+str(U_wall)+ "W/(degC)m^2 \n"

#Let's calculate the rate of heat loss through the walls of a house in Las Vegas, Nevada.

House_perimeter= 50
House_height= 2.5
T_out= -2
T_in= 22

House_area = (House_perimeter)*(House_height)

Q_loss_House= House_area*U_wall*(T_in-T_out)   #rate of heat loss through the house
 
#considering that the 20% of the wall area is occupied by glazing

Q_loss_wall= Q_loss_House*(1-0.2)
print "The rate of heat loss THROUGH THE WALLS of the house is: "+str(Q_loss_wall)+ "W"