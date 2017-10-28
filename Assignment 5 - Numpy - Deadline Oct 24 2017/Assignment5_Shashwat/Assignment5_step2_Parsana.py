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
#At Studs
condition_parallel_atStuds= ((layers_types== "parallel_atStuds") | (layers_types== "parallel_inCommon") )
ResValues_parallel_atStuds[condition_parallel_atStuds]=material_resistances[condition_parallel_atStuds] 
Rtot_parallel_atStuds=ResValues_parallel_atStuds.sum()
#Between Studs
condition_parallel_betweenStuds= ((layers_types== "parallel_betweenStuds") | (layers_types== "parallel_inCommon") )
ResValues_parallel_betweenStuds[condition_parallel_betweenStuds]=material_resistances[condition_parallel_betweenStuds] 
Rtot_parallel_betweenStuds=ResValues_parallel_betweenStuds.sum()

#Calculation of U

Rtot_atStuds= Rtot_onlyInSeries + Rtot_parallel_atStuds
Rtot_betweenStuds= Rtot_onlyInSeries + Rtot_parallel_betweenStuds 

U_atStuds=1/Rtot_atStuds
U_betweenStuds=1/Rtot_betweenStuds

f_insulation= 0.75
f_stud= 0.25
Utot= U_atStuds*f_stud + U_betweenStuds*f_insulation
print'The total U of wall is '+str(Utot)+'(W/m2*degC)'

#Calculation of Heat Loss

House_perimeter= 50
House_height= 2.5
T_out=-2
T_in=22
House_area = (House_perimeter)*(House_height)
Q_loss_House= House_area*Utot*(T_in-T_out)
Qwall= Q_loss_House*(1-0.2)# 20 percent glazing
print'The total heat loss through the wall is '+str(Qwall)+'(W)'