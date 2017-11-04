#assignment3_step2_Temporelli

def U_calculation(List1,List2,float1):
    Materials={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
    "InsideSurface":0.12,"OutsideSurfaceWinter":0.03}
    ListOfSeriesLayers=["InsideSurface","WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard","OutsideSurfaceWinter"]
    ListOfParallelLayers=["GlassFiberInsulation","Woodstud"]
    area_fraction_ins = 0.75
    
    
    R_series=0
    
    for anyLayer in ListOfSeriesLayers:
        R_anyLayer=Materials[anyLayer]
        R_series=R_series+R_anyLayer
        print("the reisistance of "+anyLayer+" is "+str(R_anyLayer))
        print "*****************"
    print ("the total R between studs is "+str(R_series))
    print"---------------------"
    
    Rtot=[]
    
    for i in ListOfParallelLayers:
        List=ListOfSeriesLayers.append(i)
        R=R_series+Materials[i]
        Rtot=Rtot+[R]
    
        
    #print("R_ins is: "+str(Rtot[0]))  
    #print("R_wood is:"+str(Rtot[1]))
    U_ins=Rtot[0]**-1
    U_wood=Rtot[1]**-1
    U_overall=(1/Rtot[0]*area_fraction_ins)+(1/Rtot[1]*(1-area_fraction_ins))
    results={ "R_ins":Rtot[0], "R_wood": Rtot[1], "U_overall":U_overall }
    return results


Materials={"WoodBevelLappedSliding":0.14,"WoodFiberboardSheeting":0.23,"GlassFiberInsulation":2.45,"Woodstud":0.63,"GypsumWallboard":0.079,
"InsideSurface":0.12,"OutsideSurfaceWinter":0.03}
ListOfSeriesLayers=["InsideSurface","WoodBevelLappedSliding","WoodFiberboardSheeting","GypsumWallboard","OutsideSurfaceWinter"]
ListOfParallelLayers=["GlassFiberInsulation","Woodstud"]
area_fraction_ins = 0.75

result_this=U_calculation(ListOfSeriesLayers,ListOfParallelLayers,area_fraction_ins) 
print ("Results: "+str(result_this))