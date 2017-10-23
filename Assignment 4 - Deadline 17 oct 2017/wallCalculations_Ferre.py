def wallCalc_withParallel(S,P,FR):
    air=["outside_surface_winter","inside_surface"]
    material_library = {"outside_surface_winter":0.030,"outside_surface_summer":0.44,
    "wood_bevel":0.14,"wood_fiberboard_13mm":0.23,"face_brick_100mm":0.075,
    "glass_fiber_90mm":2.45,"wood_stud_38mmx90mm":0.63,"gypsum_wallboard_13mm":0.079,
    "inside_surface":0.12,"stucco_25mm":0.037,"acustic_tile":0.32,"wood_5cm":0.44,
    "asphalt_shingle_roofing":0.077,"wood_140mm":0.98}
    series=S+air
   
    R=0
    resistence=[]
    for anymaterial_s in series:
        Rvalue_layer_series= material_library[anymaterial_s]
        R=R+Rvalue_layer_series
        
    for anymaterial_p in P:
        Rvalue_layer_parallel= material_library[anymaterial_p]
        resistence.append(R+Rvalue_layer_parallel) 
        
    U1=1/resistence[0]
    U2=1/resistence[1]
    secondratio=float(1-FR)
    Utot_withParallel=(U1*FR)+(U2*secondratio)
    Rt=1/Utot_withParallel
    
    results=Utot_withParallel
    
    return results
    
def wallCalc_onlyInSeries(Serie):
    AIR=["outside_surface_winter","inside_surface"]
    material_library = {"outside_surface_winter":0.030,"outside_surface_summer":0.44,
    "wood_bevel":0.14,"wood_fiberboard_13mm":0.23,"face_brick_100mm":0.075,
    "glass_fiber_90mm":2.45,"wood_stud_38mmx90mm":0.63,"gypsum_wallboard_13mm":0.079,
    "inside_surface":0.12,"stucco_25mm":0.037,"acustic_tile":0.32,"wood_5cm":0.44,
    "asphalt_shingle_roofing":0.077,"wood_140mm":0.98}
    SERIES=Serie+AIR
   
    r=0
    for anymaterial_s in SERIES:
        Rvalue_Layer_Series= material_library[anymaterial_s]
        r=r+Rvalue_Layer_Series
        
    Utot_onlyInSeries = 1/r
    RESULTS= Utot_onlyInSeries
    return RESULTS