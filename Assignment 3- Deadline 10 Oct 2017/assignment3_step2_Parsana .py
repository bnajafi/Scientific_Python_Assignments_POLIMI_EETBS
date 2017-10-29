#Assignment 3
#Shashwat Parsana
#Step 2

material_series1=['wood_bevel_siding','wood_fiberboard_13mm','glass_fiber_90mm','gypsum_13mm']
material_series2=['wood_bevel_siding','wood_fiberboard_13mm','wood_stud_38*90mm','gypsum_13mm']
Area_fracbtwStuds=0.75

def wall_layer(material_series1,material_series2,Area_fracbtwStuds):
    """First material series is with Glass fiber.Second is with wood studs and the area fraction ratio between stud should be taken into consideration"""
    material_library={'outsidesurface_winter':0.030,'wood_bevel_siding':0.14,'wood_fiberboard_13mm':0.23,
    'glass_fiber_90mm':2.45,'wood_stud_38*90mm':0.63,'gypsum_13mm':0.079,'inside_surface':0.12}
    
    airontwosides=['outsidesurface_winter','inside_surface']
    
    btwStud=material_series1+airontwosides
    atStud=material_series2+airontwosides
    
    Area_fracatStuds=0.25
    
    R_btwStud=0
    R_atStud=0
    Tin=22
    Tout=-2
    
    Rval_btwStud=[]
    Rval_atStud=[]
    
    #for resistance between studs
    for layer in btwStud:
        R_layer1=material_library[layer]
        R_btwStud=R_layer1+R_btwStud
        Rval_btwStud.append(R_layer1)
        
    U_R_btwStud=1/R_btwStud
    
    #for resistance at studs
    for layer in atStud:
        R_layer2=material_library[layer]
        R_atStud=R_layer2+R_atStud
        Rval_atStud.append(R_layer2)
       
    U_R_atStud=1/R_atStud
    
    Utot=(U_R_btwStud*Area_fracbtwStuds)+(U_R_atStud*Area_fracatStuds)
    Rtot=1/Utot
    
    #heat loss
    peri=50
    H=2.5
    A=0.8*peri*H
    
    Qwall=A*Utot*(Tin-Tout)
    print'The total Resistance value of wall is '+str(Rtot)+'(degC*m2/W)'
    print'The total U of wall is '+str(Utot)+'(W/m2*degC)'
    print'The total heat loss through the wall is '+str(Qwall)+'(W)'
    
    result={'Thermal Resistances between Studs':Rval_btwStud,'Resistances at Studs':Rval_atStud,
    'Total Resistance of layered wall':Rtot,'Total U':Utot,'Heat Transfered through wall':Qwall}
    return result
    
results=wall_layer(material_series1,material_series2,Area_fracbtwStuds)
print results
