import os
os.chdir('C:/Users/Pc/Desktop/politecnico/Energy and Enviromental Technologies For Building Systems/assignment4_Micev')
import wallCalc_Micev as wc

series_layers=["gypsum_13mm","common_brick_100mm","fiberboard_13mm","wood_bevel"]
paralel_layers=["glassfiber_90mm","woodstud_90mm"]
fraction_insulation=0.7
Area_walls=105.8 #m^2
Area_door=2.2 #m^2
Area_ceillings=200 #m^2
door=["wood_50mm","insideSurface","outsideSurface_winter"]
roof=["roof"]
Twin=-4.8 # degree C - Winter temperature in Piacenza given in Weather data 
Tins=20 # degree C - desired temperature in a room in winter
deltaT_heating=Tins-Twin
wall_layers,Rwall_heating,Uwall_heating=wc.wallCalc_withParallel(series_layers,paralel_layers,fraction_insulation)
Udoor_heating=wc.wallCalc_onlyinSeries(door)
U_roof=wc.wallCalc_onlyinSeries(roof)
print " Thermal conductivity of wall in winter is: "+str(Uwall_heating)+" W/m^2 K"
print " Thermal conductivity of door in winter is: "+str(Udoor_heating)+" W/m^2 K"
print " Thermal conductivity of roof in winter is: "+str(U_roof)+" W/m^2 K"
Q_wall_heating=Area_walls*Uwall_heating*deltaT_heating
Q_door_heating=Area_door*Udoor_heating*deltaT_heating
Q_roof_heating=Area_ceillings*U_roof*deltaT_heating
Q_total_heating=Q_wall_heating+Q_door_heating+Q_roof_heating
print " "
print " Total heat transfer through walls in winter is: " + str(Q_wall_heating)+ " W"
print " Total heat transfer through door in winter is: " + str(Q_door_heating)+ " W"
print " Total heat transfer through roof in winter is: " + str(Q_roof_heating)+ " W"
print " " 
print " Total heat transfer through opaque surfaces in winter is: "+str(Q_total_heating)+ " W."
print " That means that We should provide heat power of "+str (Q_total_heating)+" W in order to gain desired temperature of 20 (for a opaque surfaces)."
