# -*- coding: utf-8 -*-

#Material Library
Material_Library = {"outside_surface_winter":0.030,"outside_surface_summer":0.44,
"wood_bevel":0.14,"wood_fiberboard_13mm":0.23,"face_brick_100mm":0.075,
"glass_fiber_90mm":2.45,"wood_stud_38mmx90mm":0.63,"gypsum_wallboard_13mm":0.079,
"inside_surface":0.12,"stucco_25mm":0.037,"acustic_tile":0.32}

#Temperatures
T1 = 22 #indoor temperature
T2 = -2 #outdoor temperature

#Walll's dimensions
p = 50 #wall's perimeter
H = 2.5 #wall's height
Perc_glazing = 0.2 #percent of the wall area that is occupied by glazing


serie_layer = ["wood_bevel","wood_fiberboard_13mm","gypsum_wallboard_13mm"]
parallel_layer = ["glass_fiber_90mm","wood_stud_38mmx90mm"]
air = ["outside_surface_winter","inside_surface"]
total_serie = air + serie_layer
ratio = [0.75,0.25] 

R_serie_tot = 0
R_tot = []
R_glass_serie =[]
R_glass =[]
R_stud_serie =[]
R_stud = []

for anyelement in total_serie:
    R_serie = Material_Library[anyelement]
    R_serie_tot = R_serie_tot + R_serie 
    print"Layer: "+anyelement + "; Resistence value : "+str(R_serie)+"m^2°C/W"

for anyelement_p in parallel_layer:
    R_paral = Material_Library[anyelement_p]
    R_p = R_serie_tot + R_paral
    R_tot.append(R_p)
    print"Layer: "+anyelement_p + "; Resistence value : "+str(R_paral)+"m^2°C/W"    
print "*********************************************"

for a in total_serie:
        R_s = Material_Library[a]
        R_glass_serie.append(R_s)
        R_stud_serie.append(R_s)
for an in parallel_layer:
    R_glass = R_glass_serie
    R_stud = R_stud_serie
    if an == "glass_fiber_90mm":
        i = Material_Library[an]
        R_glass.append(i)
    elif an == "wood_stud_38mmx90mm":
        j = Material_Library[an]
        R_stud.append(j)

print "Wall resistences:\n" + "Value of resistences between studs: " + str(R_glass)+ "\n" + "Value of resistences at studs: " + str(R_stud)
print "*********************************************"

print "Total resistance between studs is: "+str(R_tot[0])+" [(m^2*°c)/W]"
print "U factor between studs is: "+str(1/R_tot[0])+" [W/(m^2*°c)]"
print "Total resistance at studs is: "+str(R_tot[1])+" [(m^2*°c)/W]"
print "TU factor at studs is: "+str(1/R_tot[1])+" [W/(m^2*°c)]"
print "*********************************************"

U_total = ratio[0]/R_tot[0]+ratio[1]/R_tot[1]
R_total = 1/U_total
print "Total wall resistance is: "+str(R_total)+" [(m^2*°c)/W]"
print "Total U factor is: "+str(U_total)+" [W/(m^2*°c)]"
print "*********************************************"

area_wall = p*H*(1-Perc_glazing)
Q=1/R_total*area_wall*(T1-T2)
print"Q value is: "+str(Q)+" [W]"
