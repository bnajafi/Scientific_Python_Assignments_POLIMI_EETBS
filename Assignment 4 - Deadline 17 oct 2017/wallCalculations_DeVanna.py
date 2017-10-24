def wallCalc_withParallel(S,P,FR):
    air=["outside_surface_winter","inside_surface"]
    material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
    "wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
    "gypsum_wallboard":0.079}
    series=S+air
   
    R=0
    resistence=[]
    for anymaterial in series:
        Rvalue_layer_series= material_library_dictionary[anymaterial]
        R=R+Rvalue_layer_series
        
    for anymaterial in P:
        Rvalue_layer_parallel= material_library_dictionary[anymaterial]
        resistence.append(R+Rvalue_layer_parallel) 
        
    A=resistence[0]#resistence of the first step 
    B=resistence[1]#resistence of the second step
    U1=1/resistence[0]
    U2=1/resistence[1]
    secondratio=float(1-FR)
    Utot=(U1*FR)+(U2*secondratio)
    
    results= Utot
    
    return results
    
    
def wallCalc_onlyInSeries(S):
    air=["outside_surface_winter","inside_surface"]
    material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
    "wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud_140mm":0.98,"glass_fiber":2.45,"inside_surface":0.12,
    "gypsum_wallboard":0.079,"wood_5cm":0.44,"steel_siding":0.00, "asphalt_shingle_roofing":0.077,"common_brick":0.12 }
    
    series=S+air
    R1=0
    for anymaterial in series:
        Rvalue_layer_series= material_library_dictionary[anymaterial]
        R1=R1+Rvalue_layer_series
        
    Utot1=1/R1
    results= Utot1
    return results