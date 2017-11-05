def wall_calc_assignment (listOfLayers_series,listOfLayers_parallel,ratio_area):
    """first input: all the layers in series including convective ones
    second input: two layers in parallel
    third input: ratio between first parallel layer(in input 2) and total area"""

    Material_library={"stucco_25mm": 0.037, "faceBrick_100mm": 0.075,
        "insideSurface":0.12, "outsideSurfaceSummer":0.044,
        "outsideSurfaceWinter":0.030,"woodfiberboard_13mm":0.23,"gypsumBoard":0.079,
        "woodStud":0.63,"woodBevel":0.14,"buildingPaper":0.011,"acousticTile":0.32,
        "slag_13mm":0.067,"glassFiber":2.45}
    Layer_air=["insideSurface","outsideSurfaceWinter"]
    listOfLayers_series=listOfLayers_series+Layer_air
    R_list=[]
    for Layer_par in listOfLayers_parallel:
        Rtot=0
        R_parallel=Material_library[Layer_par]
        for anyLayer in listOfLayers_series:
            R_anyLayer=Material_library[anyLayer]
            Rtot=Rtot+R_anyLayer
        R_list.append(Rtot+R_parallel)
    U_overall=(1/R_list[0]*ratio_area)+(1/R_list[1]*(1-ratio_area)) 
        
    return U_overall  
    
    

List_series=["woodBevel","woodfiberboard_13mm",
        "gypsumBoard"]
List_parallel=["glassFiber","woodStud"]
f=0.75
U=wall_calc_assignment(List_series,List_parallel,f)
A=0.8*50*2.5
Tin=22
Tout=-2
Q_overall=U*A*(Tin-Tout)

print ("the overall thermal trasnmittance value is "+str(U)+" W/m2/K")
print ("The overall heat rate is "+str(Q_overall)+"W") 