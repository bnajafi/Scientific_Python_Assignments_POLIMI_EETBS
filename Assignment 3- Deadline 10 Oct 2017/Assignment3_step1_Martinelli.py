f_ins = 0.75 #insulated portion of wall in percentage

Tin = 22.0
Tout = -2.0

H = 2.5 #height
P = 50.0 #perimeter
fin_perc = 0.2 #percentage of windows

Material_library = {"stucco_13mm":0.023,"FaceBrick_100mm":0.075,"BuildingPaper":0.011,"Plywood_13mm":0.11,"insideSurface":0.12,"outsideSurfaceSummer":0.044,
"outsideSurfaceWinter":0.03,"woodFiberboard_13mm":0.23,"WoodBevelLappedSiding":0.14,"glassFiberInsulation_90mm":2.45,"woodStud_38x90mm":0.63,"gypsiumWallboard_13mm":0.079}

layers_wall_series = ["WoodBevelLappedSiding","woodFiberboard_13mm","gypsiumWallboard_13mm"]
layers_wall_par = ["glassFiberInsulation_90mm","woodStud_38x90mm"]
airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]

layers_wall_series_tot = layers_wall_series + airOnTwoSides

Rtot_series = 0
for anyLayer in layers_wall_series_tot:
    Rvalue_layer = Material_library[anyLayer]
    Rtot_series = Rtot_series + Rvalue_layer
print "the total value of resistance for the series wall is " + str(Rtot_series)

res_tot = []
for anyLayer in layers_wall_par:
    Rvalue_layer = Material_library[anyLayer]
    res_tot.append(Rvalue_layer + Rtot_series)
print "the resistances of the two kinds of wall in parallel are " + str(res_tot)

Utot_ins = 1/res_tot[0]
Utot_wood = 1/res_tot[1]

Utot = f_ins*Utot_ins + (1-f_ins)*Utot_wood
Rtot = 1/Utot

print "the total resistance of the wall is " + str(Rtot) + " (degC m2)/W"

Qwall = Utot*(H*P*(1-fin_perc))*(Tin-Tout)

print "the total heat flux through the wall is " + str(Qwall) + " W"