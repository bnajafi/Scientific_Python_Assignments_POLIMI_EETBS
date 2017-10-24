import sys
import os
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()


import wallCalculations_Casalicchio as Wall

#INPUT WEATHER
Delta_T = 24.8 # K
            
#INPUT WALLS
Global_Heat_Transfer_Coeff = 0 # if absent put 0
Layers_In_Series=["Outside_Surface_Winter","Gypsum_Wallboard","Common_Brick","Wood_Bevel_Lapped_Siding","Wood_Fiberboard_Sheeting","Inside_Surface"]
Layers_In_Parallel=["Glass_Fiber_Insulation","Wood_Stud"]
N_Layers_In_Parallel=2
Ratio_Insulation=[0.7,0.3]
Area = 105.8 #m2
 
Results_Wall_Function=Wall.Wall_Function(Global_Heat_Transfer_Coeff,Layers_In_Series,Layers_In_Parallel, Ratio_Insulation, N_Layers_In_Parallel, Area, Delta_T)
print "\nWALLS"
print Results_Wall_Function

# INPUT DOOR
Global_Heat_Transfer_Coeff = 0 # if absent put 0
Layers_In_Series=["Outside_Surface_Winter","Door_Wood","Inside_Surface"]
Layers_In_Parallel=[]
N_Layers_In_Parallel=0
Ratio_Insulation=[1]
Area = 2.2 #m2

Results_Wall_Function=Wall.Wall_Function(Global_Heat_Transfer_Coeff,Layers_In_Series,Layers_In_Parallel, Ratio_Insulation, N_Layers_In_Parallel, Area, Delta_T)
print "\nDOOR"
print Results_Wall_Function

# INPUT CEILING
Global_Heat_Transfer_Coeff=0.25 # [m2C/W]
Layers_In_Series=[]
Layers_In_Parallel=[]
N_Layers_In_Parallel=0
Ratio_Insulation=[1]
Area = 200 #m2

Results_Wall_Function=Wall.Wall_Function(Global_Heat_Transfer_Coeff,Layers_In_Series, 
                                Layers_In_Parallel, Ratio_Insulation, N_Layers_In_Parallel, Area, Delta_T)
print "\nROOF"
print Results_Wall_Function