import os
os.chdir("C:\Users\marco\Desktop\GIT\Python4ScientificComputing_Fundamentals")

import WallCalculation_Lanzani as WC

Layers_Wall_Serie = ["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","Gypsum_13mm","Inside_surface","CommonBrick_100mm"] 
Layers_Wall_Parallel= ["Insulation_Glass_Fiber_90mm","WoodStud_90mm"]
fraction=0.70
results_wall=WC.wallCalc_withParallel(Layers_Wall_Parallel,Layers_Wall_Serie,fraction)
Layers_door=["Outside_surface_Winter","Inside_surface","Wood_50mm"]
Layers_roof=["Outside_surface_Winter","Inside_surface","MineralFiberBat_150mm","WoodFiberboard",]
results_door=WC.wallCalc_onlyInSeries(Layers_door)
results_roof=WC.wallCalc_onlyInSeries(Layers_roof)
Uwall=0.438
DeltaHeating=24.8
HF_wall=results_wall*DeltaHeating
HF_door=results_door*DeltaHeating
HF_roof=results_roof*DeltaHeating
A_wall=105.8
A_roof=200
A_door=2.2
Q_wall=A_wall*HF_wall
Q_roof=A_roof*HF_roof
Q_door=A_door*HF_door
Qtot=Q_wall+Q_door+Q_roof