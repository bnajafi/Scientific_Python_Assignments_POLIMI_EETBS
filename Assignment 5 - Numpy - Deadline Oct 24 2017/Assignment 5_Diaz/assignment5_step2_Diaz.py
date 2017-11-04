import numpy as np
material_library_name= np.array(["outsideSurfaceWinter","woodBevel","woodFiberboard_13mm","glassFiberInsulation_90mm",
"woodStud_90mm","gypsumWallboard_13mm","insideSurface"]) 
library_Rvalues =np.array([0.03,0.14,0.23,2.45,0.63,0.079,0.12])
layers_wall_S=["woodBevel","woodFiberboard_13mm","woodStud_90mm","gypsumWallboard_13mm"]
layers_wall_I=["woodBevel","woodFiberboard_13mm","glassFiberInsulation_90mm","gypsumWallboard_13mm"]
airOnTwoSides=["outsideSurfaceWinter","insideSurface"]
layers_wall_complete1= np.array(layers_wall_S+airOnTwoSides)
layers_wall_complete2= np.array(layers_wall_I+airOnTwoSides)
ratio_I=0.75
ratio_I=float(ratio_I)
ratio_S=1-ratio_I
perimeter=50
height=2.5
Awall=0.8*perimeter*height
Tin=22
Tout=-2

RValues_complete1=np.zeros(layers_wall_complete1.size)
RValues_complete2=np.zeros(layers_wall_complete2.size)


Rtot_S=0
Rtot_I=0

for anyLayer1 in layers_wall_complete1:
    RValues_complete1[layers_wall_complete1==anyLayer1]=library_Rvalues[material_library_name==anyLayer1]
Rtot_S=RValues_complete1.sum()
Utot_S=1/Rtot_S

for anyLayer2 in layers_wall_complete2:
    RValues_complete2[layers_wall_complete2==anyLayer2]=library_Rvalues[material_library_name==anyLayer2]
Rtot_I=RValues_complete2.sum()
Utot_I=1/Rtot_I


U_overall=Utot_S*ratio_S+Utot_I*ratio_I
R_overall=1/U_overall
print("The Overall R Value of the system is "+str(R_overall)+" m2C/W")
print("The Overall U Value of the system is "+str(U_overall)+" W/m2C")


Q_wall=Awall*U_overall*(Tin-Tout)
print("The rate is heat loss through the wall is "+str(Q_wall)+" W")
    

