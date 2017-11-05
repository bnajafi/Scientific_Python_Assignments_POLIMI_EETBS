import os
os.chdir("D:/POLIMI/first yr Sem 1/energy and Env Tech for Building systems/assignment")

import wallCalculations_Appiah as FC

material_seriesA =["WoodFiberboard","WoodBevel_13x200","WoodStud_90mm","Gypsum_13mm"] # List for the Woodstud
material_seriesB =["WoodBevel_13x200","WoodFiberboard","InsulationFiberGlass_90mm","Gypsum_13mm"] # List containing layers in series 
fraction =0.75

U_wall= FC.wall_calc_assignment(material_seriesA,material_seriesB,fraction)

listOflayer_series=["wood_50mm"]
U_of_Door = FC.wallCalc_onlyInSeries(listOflayer_series)

listOflayer_series=["wood_50mm","glassFiber","asphaltRoofing","woodfiberboard_13mm"]
U_Ceiling=FC.wallCalc_onlyInSeries(listOflayer_series)

# Determining the heating f    actor and heating load of the Wall, Door and ceiling
T1 = 20 
T0 = -4.8 
DELT_Heating = (T1-T0)

HF_Wall = U_wall * DELT_Heating # Heating factor of the wall
Area_wall = 0.8*50*2.5 # Area of wall with height = 2.5 and Perimeter = 50
Q_heating_wall = HF_Wall * Area_wall

HF_door = U_of_Door * DELT_Heating # Heating factor of the Door
Area_Door = 2.2 # Area of the Door, m^2
Q_heating_Door = HF_door * Area_Door

HF_Ceiling = U_Ceiling * DELT_Heating # Heating factor of the Ceiling
Area_Ceiling = 20*10 # Area of the Ceiling, m^2
Q_heating_Ceiling = HF_Ceiling * Area_Ceiling

Q_tot = Q_heating_wall + Q_heating_Door + Q_heating_Ceiling

Results = {"Q_heating_wall":Q_heating_wall,"Q_heating_Door":Q_heating_Door,"Q_heating_Door":Q_heating_Door}
print Results
print "**************************************************************************************************"
print " The Total Heating Load( Q_Heating) is "+str(Q_tot)+ " W"