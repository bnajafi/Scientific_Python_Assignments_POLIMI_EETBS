#Assignment 3
#Shashwat Parsana
#Step 1

material_library={'outsidesurface_winter':0.030,'wood_bevel_siding':0.14,'wood_fiberboard_13mm':0.23,
'glass_fiber_90mm':2.45,'wood_stud_38*90mm':0.63,'gypsum_13mm':0.079,'inside_surface':0.12}

material_series1=['wood_bevel_siding','wood_fiberboard_13mm','glass_fiber_90mm','gypsum_13mm']
material_series2=['wood_bevel_siding','wood_fiberboard_13mm','wood_stud_38*90mm','gypsum_13mm']
airontwosides=['outsidesurface_winter','inside_surface']

btwStud=material_series1+airontwosides
atStud=material_series2+airontwosides

Area_fracatStuds=0.25
Area_fracbtwStuds=0.75

R_btwStud=0
R_atStud=0
Tin=22
Tout=-2

print('\n')
print'Resistance between Studs'
print'------------------------'
#for resistance between studs
for layer in btwStud:
    R_layer1=material_library[layer]
    R_btwStud=R_layer1+R_btwStud
    print'The layer is '+layer 
    print'The R value of this layer is ' +str(R_layer1)+'(degC*m2/W)'
    print'***************************************************'
U_R_btwStud=1/R_btwStud
print' The total resistance of layers between stud is ' +str(R_btwStud)+'(degC*m2/W)' +' and U is '+str(U_R_btwStud)+'(W/m2*degC)'
print'**************************************************************************'
print'**************************************************************************'


print('\n')
print'Resistance at Studs'
print'--------------------'
#for resistance at studs
for layer in atStud:
    R_layer2=material_library[layer]
    R_atStud=R_layer2+R_atStud
    print'The layer is '+layer 
    print'The R value of this layer is ' +str(R_layer2)+'(degC*m2/W)'
    print'***************************************************'

U_R_atStud=1/R_atStud
print' The total resistance of layers at stud is ' +str(R_atStud)+'(degC*m2/W)' +' and U is '+str(U_R_atStud)+'(W/m2*degC)'
print'**************************************************************************'
print'**************************************************************************'

print('\n')
Utot=(U_R_btwStud*Area_fracbtwStuds)+(U_R_atStud*Area_fracatStuds)
Rtot=1/Utot
print'The total Resistance value of wall is '+str(Rtot)+'(degC*m2/W)'
print'The total U of wall is '+str(Utot)+'(W/m2*degC)'


#heat loss
peri=50
H=2.5
A=0.8*peri*H

Qwall=A*Utot*(Tin-Tout)
print('\n')
print'The total heat loss through the wall is '+str(Qwall)+'(W)'
    



