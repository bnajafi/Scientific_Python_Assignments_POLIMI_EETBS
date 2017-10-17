#FUNCTION ASSIGNMENT 3

inseries=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
inparallel=["glass_fiber","wood_stud"]
firstratio=float(0.75)

def totalwall(S,P,FR):
    air=["outside_surface_winter","inside_surface"]
    material_library_dictionary={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
    "wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
    "gypsum_wallboard":0.079}
    series=S+air
   
    R=0
    resistence=[]
    for anymaterial in S:
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
    Rt=1/Utot
    
    results={"Total Thermal Resistence":Rt,"thermal resistence of the first layer":A,
    "thermal resistence of the second layer":B,"total U of the wall":Utot }
    
    return results
    
X=totalwall(inseries,inparallel,firstratio)
print X