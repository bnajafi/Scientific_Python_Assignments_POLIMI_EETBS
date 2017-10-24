 #we define the function
def wallCalculations(List1,List2,float1):
    R_materials={"outside": 0.03,"wood":0.44, "woodbevel":0.14, "woodfiber": 0.23, "glassfiber":2.45, "stud": 0.63, "gypsum":0.079, "inside":0.12}   
     
    R_series=0
     
    for n in List1:
        R_n=R_materials[n]
        R_series=R_series+R_n
     
    R_p = 0.0
    Rtot = [] 
    for i in List2:
        R_p = R_series + R_materials[i]
        Rtot.append(R_p)

     
         

    U_overall=(1/Rtot[0]*float1)+(1/Rtot[1]*(1-float1))
    y={ "R_ins":Rtot[0], "R_wood": Rtot[1], "U_overall":U_overall }
    return y

 


#we define now a function which accepts only one list in order to compute the U value of door and roof
def a(oneList):
    R_materials={"outside": 0.03, "wood":0.44, "woodbevel":0.14, "woodfiber": 0.23, "glassfiber":2.45, "stud": 0.63, "gypsum":0.079, "inside":0.12}   
    
    R_sertot = 0.0
    for n in oneList:
        R_sertot = R_sertot + R_materials[n]
    
    U_tot = 1/R_sertot
    
    result = {"Total resistance":R_sertot, "Total U": U_tot}
    return result
    

    