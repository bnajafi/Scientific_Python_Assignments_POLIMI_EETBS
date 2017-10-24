import numpy as np

materials_names= np.array(["Outside_surface_Winter","Inside_surface",
                           "Insulation_Glass_Fiber_90mm", "WoodStud_90mm", 
                           "WoodFiberboard","WoodBevel_13x200","Gypsum_13mm",
                           "Stucco_25mm","MineralFiber_25mm","Plywood_13mm"]) 
materials_Rvalues =np.array([0.03,0.12,2.45,0.63,0.23,0.14,0.079,0.037,0.66,0.11])
ratio=0.75

Layers_series= np.array(["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","Gypsum_13mm","Inside_surface"])
RValue_series= np.zeros(Layers_series.size)
for i in Layers_series:
    RValue_series[Layers_series==i]= materials_Rvalues[materials_names==i]
Rtot_series=RValue_series.sum()
print"Rtot series is "+str(Rtot_series)

    
Layers_parallel=np.array(["Insulation_Glass_Fiber_90mm","WoodStud_90mm"])
UValue_parallel=np.zeros(Layers_parallel.size)
for i in Layers_parallel:
    UValue_parallel[Layers_parallel==i]= 1/materials_Rvalues[materials_names==i]
Utot_parallel=0.75*UValue_parallel[0]+0.25*UValue_parallel[1]
Rtot_parallel=1/Utot_parallel
print "Rtot parallel is "+str(Rtot_parallel)

Layers_series1= np.array(["Outside_surface_Winter","Insulation_Glass_Fiber_90mm","WoodBevel_13x200","WoodFiberboard","Gypsum_13mm","Inside_surface"])
RValue_series1= np.zeros(Layers_series1.size)
for j in Layers_series1:
    RValue_series1[Layers_series1==j]= materials_Rvalues[materials_names==j]
Rtot_series1=RValue_series1.sum()
Utot_series1=1/Rtot_series1

Layers_series2= np.array(["Outside_surface_Winter","WoodBevel_13x200","WoodStud_90mm","WoodFiberboard","Gypsum_13mm","Inside_surface"])
RValue_series2= np.zeros(Layers_series2.size)
for k in Layers_series2:
    RValue_series2[Layers_series2==k]= materials_Rvalues[materials_names==k]
Rtot_series2=RValue_series2.sum()
Utot_series2=1/Rtot_series2

Utot=0.75*Utot_series1+0.25*Utot_series2
print "Utot wall is "+str(Utot)




