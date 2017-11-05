#Assignment3_step1

Material_Library={"Outside_surface_winter":0.03, "Outside_surface_summer":0.044, "Inside_surface":0.12, 
"Cement_mortar_13mm":0.018, "Plywood_13mm":0.11, "Building_paper":0.011, "Acoustic_tile":0.32,
"Wood_stud_140mm":0.98, "Wood_stud_90mm":0.63, "Glass_fiber_90mm":2.45, "Glass_fiber_25mm":0.7, 
"Wood_fiberboard_13mm":0.23, "Wood_bevel_13mm":0.14, "Gypsum_wallboard_13mm":0.079}

Layers_series=["Wood_bevel_13mm", "Wood_fiberboard_13mm", "Gypsum_wallboard_13mm"]
Layers_parallel=["Glass_fiber_90mm", "Wood_stud_90mm"]

f1=float(0.75) #ratio between the area of the first parallel layer to the total one 

Layers_series.append("Inside_surface")

#season setting 
season="winter"
if season=="winter":
    Layers_series.append("Outside_surface_winter")
elif season=="summer":
    Layers_series.append("Outside_surface_summer")
else:
    print("Please select a season between winter or summer")

#Computing the total unit thermal resistance of each section
###
R_series=0
for anyLayer in Layers_series:
    R_series=R_series+Material_Library[anyLayer]
    
R=[]
for anyLayer in Layers_parallel:
    R_section_value=Material_Library[anyLayer]+R_series
    R.append(R_section_value)
    
    
#Overall U-factor

Utot=f1*R[0]**-1+(1-f1)*R[1]**-1

print('The overall U-factor of the wall is: ' +str(Utot)+' W/Km2')

#Rate of heat loss through the wall under design conditions (W)

p=0.2 # glazing percentage
P=50  # perimeter in m
H=2.5 # height in m
Tin=22
Tout=-2
Q_dot=(1-p)*P*H*Utot*(Tin-Tout) # watts
print('The rate of heat loss through the wall is: ' +str(Q_dot)+ ' W')
