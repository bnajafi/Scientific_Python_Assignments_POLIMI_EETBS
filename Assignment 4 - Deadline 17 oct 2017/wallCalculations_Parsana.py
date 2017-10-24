

material_library={'outsidesurface_winter':0.030,'wood_bevel_siding':0.14,'wood_fiberboard_13mm':0.23,
    'glass_fiber_90mm':2.45,'wood_stud_38*90mm':0.63,'gypsum_13mm':0.079,'inside_surface':0.12,'Wood_door_50mm':0.44,'asphaltshingles_roofing':0.077,'Wood_roof_100mm':0.88}
    
material_series1=['wood_bevel_siding','wood_fiberboard_13mm','glass_fiber_90mm','gypsum_13mm']
material_series2=['wood_bevel_siding','wood_fiberboard_13mm','wood_stud_38*90mm','gypsum_13mm']
material_door=['Wood_door_50mm']
material_roof=['asphaltshingles_roofing','Wood_roof_100mm']
airontwosides=['outsidesurface_winter','inside_surface']

def U_wall_layer(material_series1,material_series2):
    
    btwStud=material_series1+airontwosides
    atStud=material_series2+airontwosides
    
    Area_fracatStuds=0.30
    Area_fracbtwStuds=0.70
    
    R_btwStud=0
    R_atStud=0
    
    #for resistance between studs
    for layer in btwStud:
        R_layer1=material_library[layer]
        R_btwStud=R_layer1+R_btwStud
        
    U_R_btwStud=1/R_btwStud
    
    #for resistance at studs
    for layer in atStud:
        R_layer2=material_library[layer]
        R_atStud=R_layer2+R_atStud
       
    U_R_atStud=1/R_atStud
    
    wall_Utot=(U_R_btwStud*Area_fracbtwStuds)+(U_R_atStud*Area_fracatStuds)
    
    result={'Total U of Wall':wall_Utot}
    return result
    
results=U_wall_layer(material_series1,material_series2)
print results

def U_roof_door(material_door,material_roof):
    door_layer=material_door+airontwosides
    roof_layer=material_roof+airontwosides
    R_door=0
    R_roof=0
    
    #for resistance of door
    for layer in door_layer:
        R_door1=material_library[layer]
        R_door=R_door1+R_door
        
    U_R_door=1/R_door
    
    #for resistance at roof
    for layer in roof_layer:
        R_roof1=material_library[layer]
        R_roof=R_roof1+R_roof
       
    U_R_roof=1/R_roof
    
    result={'Total U of Roof is ':U_R_roof,'Total U of Door is ':U_R_door}
    return result

results=U_roof_door(material_door,material_roof)
print results
print"Unit of all the values of U is (W/m2K)"


    
    
    
