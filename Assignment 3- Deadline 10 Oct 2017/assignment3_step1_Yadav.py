##Example- heat transfer through wall

##defining material library
Material_library= {"stucco_25mm":0.037,"facebrick_100mm":0.075,"Building paper":0.011,"insideSurface":0.12,"outsideSurfaceSummer":0.044,
"outsideSurfaceWinter":0.03,"woodBevelLappedsliding_200mm":0.14,"woodFiberBoard_13mm":0.23,"gypsum_13mm":0.079,
"glassFibreInsulation_25mm":2.52,"woodStud_90mm":0.63}


## forming lists  for reisitances in series and parallel
R_betweenStud=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","glassFibreInsulation_25mm","gypsum_13mm",
"insideSurface"]
R_atStud=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","woodStud_90mm","gypsum_13mm","insideSurface"]


## calculating total resistance without insulation
Rtot_stud=0
RvalueOfStud_loop=[]
for Rstud in R_atStud:
    RvalueOfStud= Material_library[Rstud]
    Rtot_stud=Rtot_stud+RvalueOfStud
    RvalueOfStud_loop.append(RvalueOfStud)
    
print "this value of R for this layer is :" + str(RvalueOfStud_loop)

print"the total R value without insulation  is "+ str(Rtot_stud) +" (W/m^2 DegC)"
print "*******!!!!!!!!!!!!!!!!!!************\n"
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
f_insu=0.75
f_stud=0.25

Utot= U_insu*f_insu+U_stud*f_stud
print "the value of overall heat transfer coefficient is  : " +str(Utot) + " (W/m^2 DegC)"
print "*******!!!!!!!!!!!!!!!!!!************\n"

## calcualting the total heat tranfer through the wall using overall heat transfer coefficient
Area=100 
Ti=22
Tout=-2
Q_wall= Utot*Area*(Ti-Tout)

print " Total heat transfer value from the wall is  :  " +str(Q_wall) + "  watts"
print "*******!!!!!!!!!!!!!!!!!!************\n"



    
    
    
    




