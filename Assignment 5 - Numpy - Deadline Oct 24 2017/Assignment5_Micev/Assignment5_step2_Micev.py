import numpy as np
list_of_items=np.array(["glassfiber_90mm","stucco_25mm","facebrick_100mm","wood_25mm","woodstud_90mm","woodstud_140mm","gypsum_13mm"
,"fiberboard_13mm","outsideSurface_winter","outsideSurface_summer","insideSurface","wood_bevel"])
list_of_resistances=np.array([2.52,0.037,0.075,0.22,0.63,0.98,0.079,0.23,0.03,0.044,0.12,0.14])
L1=["wood_bevel","gypsum_13mm","fiberboard_13mm","outsideSurface_winter","insideSurface"]
series_materials=np.array(L1)
L2=["glassfiber_90mm","woodstud_90mm"]
paralel_materials=np.array(L2)
fraction=0.75
P1=L1+["glassfiber_90mm"]
P2=L1+["woodstud_90mm"]
paralel_layer1=np.array(P1)
paralel_layer2=np.array(P2)
index_wood_bevel=list_of_items=="wood_bevel"
index_gypsum=list_of_items=="gypsum_13mm"
index_fiberboard=list_of_items=="fiberboard_13mm"
index_outside=list_of_items=="outsideSurface_winter"
index_surface=list_of_items=="insideSurface"
index_glassfiber=list_of_items=="glassfiber_90mm"
index_woodstud=list_of_items=="woodstud_90mm"
index_materials1=(index_wood_bevel)|(index_gypsum)|(index_fiberboard)|(index_outside)|(index_surface)|(index_glassfiber)
list_parallel1=list_of_items[index_materials1]
resistances_parallel1=list_of_resistances[index_materials1]
index_materials2=(index_wood_bevel)|(index_gypsum)|(index_fiberboard)|(index_outside)|(index_surface)|(index_woodstud)
list_parallel2=list_of_items[index_materials2]
resistances_parallel2=list_of_resistances[index_materials2]
U1=1/resistances_parallel1.sum()
print " Heat transfer coefficient of first layer of parallel layers is: "+str(U1)+" W/ degree C * m^2"
U2=1/resistances_parallel2.sum()
print " Heat transfer coefficient of second layer of parallel layers is: "+str(U2)+" W/ degree C * m^2"
total_heat_transfer_coefficient=U1*fraction+(1-fraction)*U2
print " Total heat transfer coefficient of this wall is: "+str(total_heat_transfer_coefficient)+" W/ degree C * m^2"
total_resistance=1/total_heat_transfer_coefficient
print " Total resistance of this wall is "+str(total_resistance)+" m^2 * degree C/W"
print " "
perimeter_of_wall=50
wall_height=2.5
glazing_area=0.2
Tin=22
Tout=-2
Qwall=perimeter_of_wall*wall_height*(1-glazing_area)*total_heat_transfer_coefficient*(Tin-Tout)
print " Total heat transfer through wall area is "+str(Qwall)+" W"



