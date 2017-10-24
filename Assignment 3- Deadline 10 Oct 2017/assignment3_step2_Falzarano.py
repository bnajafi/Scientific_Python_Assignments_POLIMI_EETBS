 #we define the function
def U_calculation(List1,List2,float1):
    R_materials={"outside": 0.03, "woodbevel":0.14, "woodfiber": 0.23, "glassfiber":2.45, "stud": 0.63, "gypsum":0.079, "inside":0.12}
    layer_ser=["inside","woodbevel","woodfiber","gypsum","outside"]
    layer_par=["glassfiber","stud"]
    frac_area = 0.75
     
     
    R_series=0
     
    for n in layer_ser:
        R_series=R_series+R_materials[n]
        print("the reisistance of "+n+" is "+str(R_materials[n]))
        print ()
    print ("the total R between studs is "+str(R_series))
    print()
     
    Rtot=[]
     
    for i in layer_par:

        R=R_series+R_materials[i]
        Rtot=Rtot+[R]

    U_overall=(1/Rtot[0]*frac_area)+(1/Rtot[1]*(1-frac_area))
    y={ "R_ins":Rtot[0], "R_wood": Rtot[1], "U_overall":U_overall }
    return y
 
 
R_materials={"outside": 0.03, "woodbevel":0.14, "woodfiber": 0.23, "glassfiber":2.45, "stud": 0.63, "gypsum":0.079, "inside":0.12}
layer_ser=["inside","woodbevel","woodfiber","gypsum","outside"]
layer_par=["glassfiber","stud"]
frac_area = 0.75
 
result_this=U_calculation(layer_ser,layer_par,frac_area) 
print ("Results: "+str(result_this))



