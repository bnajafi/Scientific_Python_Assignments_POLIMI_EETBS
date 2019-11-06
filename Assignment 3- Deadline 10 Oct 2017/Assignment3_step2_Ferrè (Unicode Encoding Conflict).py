# -*- coding: utf-8 -*-

def wall_resistence_calc (serie_layer,parallel_layer,ratio):
    Material_Library = {"outside_surface_winter":0.030,"outside_surface_summer":0.44,
    "wood_bevel":0.14,"wood_fiberboard_13mm":0.23,"face_brick_100mm":0.075,
    "glass_fiber_90mm":2.45,"wood_stud_38mmx90mm":0.63,"gypsum_wallboard_13mm":0.079,
    "inside_surface":0.12,"stucco_25mm":0.037,"acustic_tile":0.32}
    
    T1 = 22
    T2 = -2
    p = 50
    H = 2.5
    Perc_glazing = 0.2
    
    air = ["outside_surface_winter","inside_surface"]
    total_serie = air + serie_layer
    
    R_serie_tot = 0
    R_tot = []
    R_glass_serie =[]
    R_glass =[]
    R_stud_serie =[]
    R_stud = []
    
    for anyelement_s in total_serie:
        R_serie = Material_Library[anyelement_s]
        R_serie_tot = R_serie_tot + R_serie
    
    for anyelement_p in parallel_layer:
        R_paral = Material_Library[anyelement_p]
        R_p = R_serie_tot + R_paral
        R_tot.append(R_p)
    
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
    
    U_total = ratio[0]/R_tot[0]+ratio[1]/R_tot[1]
    R_total = 1/U_total

    area_wall = p*H*(1-Perc_glazing)
    Q=1/R_total*area_wall*(T1-T2)
    results = {"Value of resistences between studs":R_glass,
    "Value of resistences at studs":R_stud,"Total wall resistance":R_total,
    "Total U factor":U_total,"Q value":Q,"Total resistance between studs":R_tot[0],
    "Total resistance at studs":R_tot[1]}
    return results

serie_layer = ["wood_bevel","wood_fiberboard_13mm","gypsum_wallboard_13mm"]
parallel_layer = ["glass_fiber_90mm","wood_stud_38mmx90mm"]
ratio = [0.75,0.25] 
wall_final_results = wall_resistence_calc(serie_layer,parallel_layer,ratio)
print wall_final_results