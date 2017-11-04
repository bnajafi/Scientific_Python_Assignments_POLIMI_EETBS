# ASSIGNMENT 3 - PART 1#

Material_library= {"outsideSurfaceWinter":0.030, "outsideSurfaceSummer":0.044,"insideSurface":0.12,"stucco_25mm":0.037,"faceBrick_100mm":0.075,
"commonBrick_100mm":0.12,"woodStud_90mm":0.63,"woodFiberboard_13mm":0.23,"buildingPaper":0.011,"gypsum":0.079,"glassfiberInsulation_90mm":2.45,
"woodBevelLapped":0.14}     

AirOnTwoSides= ["outsideSurfaceWinter","insideSurface"]    #layers only in series
Layers_atStuds = ["gypsum","woodStud_90mm","woodFiberboard_13mm","woodBevelLapped"]     #layers in parallel
Layers_betweenStuds= ["gypsum","glassfiberInsulation_90mm","woodFiberboard_13mm","woodBevelLapped"]   #layers in parallel

#Let's calculate U for the layer at studs

Complete_Layers_atStuds= AirOnTwoSides+Layers_atStuds  #complete layers at studs

Rvalues_anyLayer_as=[]
Rtot_as=0
for anyLayer in Complete_Layers_atStuds:
    Rvalue_anyLayer=Material_library[anyLayer]
    Rvalues_anyLayer_as.append(Rvalue_anyLayer)
    Rtot_as=Rtot_as+Rvalue_anyLayer
print "The unit thermal resistances of the layers in series at studs are: "+str(Rvalues_anyLayer_as)+ " m^2(degC)/W"
print "The total unit thermal resistance calculated at studs is : "+str(Rtot_as)+ " m^2(degC)/W"
U_atStuds= 1/Rtot_as
print "Thus, the overall heat transfer coefficient is: "+str(U_atStuds)+ "W/(degC)m^2"   
print "**************************************************************************************"    

#Let's calculate U for the layer between studs, considering glass fiber insulation

Complete_Layers_betweenStuds= AirOnTwoSides+Layers_betweenStuds
Rtot_bs=0
Rvalues_anyLayer_bs=[]
for anyLayer in Complete_Layers_betweenStuds:
    Rvalue_anyLayer= Material_library[anyLayer]
    Rvalues_anyLayer_bs.append(Rvalue_anyLayer)
    Rtot_bs= Rtot_bs+Rvalue_anyLayer
print "The unit thermal resistances of the layers in series between studs is: "+str( Rvalues_anyLayer_bs)+ " m^2(degC)/W"
print "The total unit thermal resistance calculated between studs is : "+str(Rtot_bs)+ " m^2(degC)/W"
U_betweenStuds= 1/Rtot_bs
print "Thus, the overall heat transfer coefficient is: "+str(U_betweenStuds)+ "W/(degC)m^2" 
print "***************************************************************************************"

#The insulated cavity constitutes 75% of the heat transmission area while the studs constitutes 25%

f_insulation= 0.75
f_stud= 0.25
U_wall= U_atStuds*f_stud + U_betweenStuds*f_insulation
print "THE OVERALL HEAT TRANSFER COEFFICIENT U OF THE WALL IS: "+str(U_wall)+ "W/(degC)m^2 \n"

R_wall= 1/U_wall 
print "THE OVERALL UNIT THERMAL RESISTANCE R' OF THE WALL IS: " +str(R_wall) + "m^2(degC)/W \n"

#Let's calculate the rate of heat loss through the walls of a house in Las Vegas, Nevada.

House_perimeter= 50
House_height= 2.5
T_out= -2
T_in= 22

House_area = (House_perimeter)*(House_height)

Q_loss_House= House_area*U_wall*(T_in-T_out)   #rate of heat loss through the house
 
#considering that the 20% of the wall area is occupied by glazing

Q_loss_wall= Q_loss_House*(1-0.2)
print "The rate of heat loss THROUGH THE WALLS of the house is: "+str(Q_loss_wall)+ "W"

