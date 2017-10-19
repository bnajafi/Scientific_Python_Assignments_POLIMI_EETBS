#ASSIGNMENT 4

def wallcalc_withparaller(S,P,FR):
    air=["outside_surface_winter","inside_surface"]
    material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
    "wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
    "gypsum_wallboard":0.079,"wood_5cm":0.44}
    series=S+air
   
    R=0
    for anymaterial in S:
        Rvalue_layer_series= material_library_dictionary[anymaterial]
        R=R+Rvalue_layer_series
    resistence=[]   
    for anymaterial in P:
        Rvalue_layer_parallel= material_library_dictionary[anymaterial]
        resistence.append(R+Rvalue_layer_parallel) 
        
    U1=1/resistence[0]
    U2=1/resistence[1]
    secondratio=float(1-FR)
    Utot1=(U1*FR)+(U2*secondratio)
    Rt=1/Utot1
    
    results=Utot1
    
    return results
    
def wallcalc_onlyInSeries(S):
    air=["outside_surface_winter","inside_surface"]
    material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
    "wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
    "gypsum_wallboard":0.079,"wood_5cm": 0.44,}
    series=S+air
   
    R1=0
    
    for anymaterial in S:
        Rvalue_layer_series= material_library_dictionary[anymaterial]
        R1=R1+Rvalue_layer_series
        
    Utot2=1/R1
    Rt=1/Utot2
    
    results=Utot2
    
    return results
    