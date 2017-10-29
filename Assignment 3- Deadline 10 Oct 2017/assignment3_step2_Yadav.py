## forming lists  for reisitances in series and parallel
R_betweenStud=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","glassFibreInsulation_25mm","gypsum_13mm",
"insideSurface"]
R_atStud=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","woodStud_90mm","gypsum_13mm","insideSurface"]
A_betweenStud=0.75
A_atStud=0.25


##defining material library

def walllayer (R_betweenStud,R_atStud,A_betweenStud,A_atStud):
    Material_library= {"stucco_25mm":0.037,"facebrick_100mm":0.075,"Building paper":0.011,"insideSurface":0.12,"outsideSurfaceSummer":0.044,
    "outsideSurfaceWinter":0.03,"woodBevelLappedsliding_200mm":0.14,"woodFiberBoard_13mm":0.23,"gypsum_13mm":0.079,
    "glassFibreInsulation_25mm":2.52,"woodStud_90mm":0.63}
    
    Rtot_stud=0
    RvalueOfStud_loop=[]
    for Rstud in R_atStud:
        RvalueOfStud= Material_library[Rstud]
        Rtot_stud=Rtot_stud+RvalueOfStud
        RvalueOfStud_loop.append(RvalueOfStud)
        
    print "this value of R for this layer is :" + str(RvalueOfStud_loop)
    
    print"the total R value without insulation  is "+ str(Rtot_stud) +" (W/m^2 DegC)"
    
    
    ##calcualting total resistance with insulation 
    Rtot_insu=0
    RvalueOfinsu_loop=[]
    for Rinsu in R_betweenStud:
        RvalueOfinsu= Material_library[Rinsu]
        Rtot_insu=Rtot_insu+RvalueOfinsu
        RvalueOfinsu_loop.append(RvalueOfinsu)
        
    print "this value of R for this layer is :" + str(RvalueOfinsu_loop)
    
    print"the total R value with insulation is "+ str(Rtot_insu) +" (m^2 DegC/W)"
    
    print "*******!!!!!!!!!!!!!!!!!!************\n"
    
    ### calculating the overall heat transfer coefficient
    U_insu=1/Rtot_insu
    U_stud= 1/Rtot_stud
    
    Utot= U_insu*A_betweenStud+U_stud*A_atStud
    print "the value of overall heat transfer coefficient is  : " +str(Utot) + " (W/m^2 DegC)"
    print "*******!!!!!!!!!!!!!!!!!!************\n"
    
    ## calcualting the total heat tranfer through the wall using overall heat transfer coefficient
    Area=100 
    Ti=22
    Tout=-2
    Q_wall= Utot*Area*(Ti-Tout)
    
    print " Total heat transfer value from the wall is  :  " +str(Q_wall) + "  watts"
    print "*******!!!!!!!!!!!!!!!!!!************\n"
    
    results={"Rvalue of stud layers":RvalueOfStud_loop,"Rtot_stud":Rtot_stud,"Rvalue of insu layers" :RvalueOfinsu_loop,"Rtot_insu":Rtot_insu
    ,"overall heat transfer coefficient":Utot,"total heat tranfer through the wall":Q_wall}
    return results
results=walllayer (R_betweenStud,R_atStud,A_betweenStud,A_atStud)
print results

