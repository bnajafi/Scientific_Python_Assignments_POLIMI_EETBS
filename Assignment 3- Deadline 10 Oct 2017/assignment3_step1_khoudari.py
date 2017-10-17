Materials_library={"glassfiber_90mm":2.52,"stucco_25mm":0.037,"facebrick_100mm":0.075,"wood_25mm":0.22,
"woodstud_90mm":0.63,"woodstud_140mm":0.98,"plywood_13mm":0.11,"gypsum_13mm":0.079,"fiberboard_13mm":0.23,
"outsideSurface_winter":0.03,"outsideSurface_summer":0.044,"insideSurface":0.12,"wood_bevel":0.14}
series_materials=["wood_bevel","gypsum_13mm","fiberboard_13mm"] 
paralel_materials=["glassfiber_90mm","woodstud_90mm"] 
convection_resistances=["outsideSurface_winter","insideSurface"]
paralel_layer1=series_materials+convection_resistances+["glassfiber_90mm"]
paralel_layer2=series_materials+convection_resistances+["woodstud_90mm"]
for anyRes in series_materials:
    print " Resistance of "+str(anyRes)+" is equal to: "+str(Materials_library[anyRes])+" m^2*degree C/W "
    print " "
for anyRes in paralel_materials:
    print " Resistance of "+str(anyRes)+" is equal to: "+str(Materials_library[anyRes])+" m^2*degree C/W "
    print " "
fraction_cavity_insulation=0.75
fraction_woodstuds=1-fraction_cavity_insulation
sum=0
for anyRes in paralel_layer1:
    sum=sum+Materials_library[anyRes]
print " Total resistance of layers that are part of first layer of paralel ones is: "+str(sum)+" m^2*degree C/W"
U1=1/sum
print " "
print " Total heat transfer coefficient of first layer of paralel ones is: "+str(U1)+"  W/m^2*degree C"
print " "
sum1=0
for anyRes in paralel_layer2:
    sum1=sum1+Materials_library[anyRes]
print " Total resistance of layers that are part of second layer of paralel ones is: "+str(sum1)+" m^2*degree C/W"
U2=1/sum1
print " "
print " Total heat transfer coefficient of second layer of paralel ones is: "+str(U2)+" W/m^2*degree C "
print " "
total_heat_transfer_coefficient=fraction_cavity_insulation*1/sum+fraction_woodstuds*1/sum1
print " Total heat transfer coefficient of this wall is "+str(total_heat_transfer_coefficient)+" W/m^2*degree C"
print " " 
total_resistance=1/total_heat_transfer_coefficient
print " Total resistance of this wall is "+str(total_resistance)+" m^2 * degree C/W"
print " "
perimeter_of_wall=50
wall_height=2.5
glazing_area=0.2
Tin=22
Tout=-2
Qwall=perimeter_of_wall*wall_height*(1-glazing_area)*total_heat_transfer_coefficient*(Tin-Tout)
print "Total heat transfer through wall area is "+str(Qwall)+" W"


#Way 2. I solved the assignment before I see the guidelines posted on dropbox. It's solved using dictonaries.
material_library={"stucco":{"thickness":25,"resistance":0.037},"glassfiber":{"thickness":25,"resistance":0.7},
"wood_stud":{"thickness":90,"resistance":0.63},"gypsum":{"thickness":13,"resistance":0.079},
"wood_siding":{"thickness":13,"resistance":0.14},"wood":{"thickness":25,"resistance":0.22},"fiberboard":{"thickness":13,"resistance":0.23}}
convective_resistances={"OutsideSurfaceWinter":0.03,"InsideSurface":0.12}
materials1={"gypsum":13,"glassfiber":90,"fiberboard":13,"wood_siding":13}
materials2={"gypsum":13,"wood_stud":90,"fiberboard":13,"wood_siding":13}
for anyMat in materials1:
   material=material_library[anyMat]
   thickness_standard=float(material["thickness"])
   resistance=material["resistance"]
   thickness=materials1[anyMat]   
   materials1[anyMat]=(thickness/thickness_standard)*resistance
materials1
for anyMat in materials2:
    material=material_library[anyMat]
    thickness_standard=float(material["thickness"])
    resistance=material["resistance"]
    thickness=materials2[anyMat]   
    materials2[anyMat]=(thickness/thickness_standard)*resistance
materials2
sum=0
print " Calculation of resistances for layers between studs: "
print " "
for anyMat in materials1:
    sum=sum+materials1[anyMat]
    print "Resistance of layer of "+str(anyMat)+" is :"+str(materials1[anyMat])+" m^2 * degree C/W"
    print " "
sum1=sum+convective_resistances["OutsideSurfaceWinter"]+convective_resistances["InsideSurface"]  
print "Resistance of layer between studs is :"+str(sum1)+ " m^2 * degree C/W"
print "****************************************************"
sum=0
print " Calculation of values of resistances for all studs: "
print " "
for anyMat in materials2:
    sum=sum+materials2[anyMat]
    print "Resistance of layer of "+str(anyMat)+" is :"+str(materials2[anyMat])+" m^2 * degree C/W"
    print " "
sum2=sum+convective_resistances["OutsideSurfaceWinter"]+convective_resistances["InsideSurface"]  
print "Resistance of layer between studs is :"+str(sum2)+ " m^2 * degree C/W"
print "****************************************************"
fraction_cavity_insulation=0.75
fraction_woodstuds=0.25
total_heat_transfer_coefficient=fraction_cavity_insulation*1/sum1+fraction_woodstuds*1/sum2
print " Total heat transfer coefficient of this wall is "+str(total_heat_transfer_coefficient)+" W/m^2 *degree C"
print " " 
total_resistance=1/total_heat_transfer_coefficient
print " Total resistance of this wall is "+str(total_resistance)+" m^2 * degree C/W"
print " "
perimeter_of_wall=50
wall_height=2.5
glazing_area=0.2
Tin=22
Tout=-2
Qwall=perimeter_of_wall*wall_height*(1-glazing_area)*total_heat_transfer_coefficient*(Tin-Tout)
print " Total heat transfer through wall area is "+str(Qwall)+" W"



