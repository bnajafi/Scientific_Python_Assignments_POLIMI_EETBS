#Dictionary - Conduction in serie
R_foam = {"Unit_Area":0.25,"Length":0.03,"Thermal_Coefficient":0.026} 
R_plaster1 = {"Unit_Area":0.25,"Length":0.02,"Thermal_Coefficient":0.22} 
R_plaster2 = {"Unit_Area":0.25,"Length":0.02,"Thermal_Coefficient":0.22}

#Dictionary - Convection in serie
R_conv1 = {"Unit_Area":0.25,"Convective_Coefficient":10}
R_conv2 = {"Unit_Area":0.25,"Convective_Coefficient":25}

#Dictionary - Conduction in parallel
R_p1 = {"Unit_Area":0.015,"Length":0.16,"Thermal_Coefficient":0.22}
R_p2 = {"Unit_Area":0.015,"Length":0.16,"Thermal_Coefficient":0.22}
R_brick = {"Unit_Area":0.22,"Length":0.16,"Thermal_Coefficient":0.72}

#(Conduction)
Rcond = [R_foam,R_plaster1,R_plaster2]
TOT = [0,0,0] #initialize the counter

for i in Rcond:
    Rs1 = i["Length"]/(i["Unit_Area"]*i["Thermal_Coefficient"])
    TOT[0] = TOT[0] + Rs1

#(Convection)
Rconv = [R_conv1,R_conv2]

for j in Rconv:
    Rs2 = 1/(j["Unit_Area"]*j["Convective_Coefficient"])
    TOT[1] = TOT[1] + Rs2

#(Conduction in parallel)
R_cond_p = [R_p1,R_p2,R_brick]

for k in R_cond_p:
    Rp = 1/(k["Length"]/(k["Unit_Area"]*k["Thermal_Coefficient"]))
    TOT[2] = TOT[2] + Rp

print ("Total Unit Resistance")
print round((TOT[0]+TOT[1]+TOT[2]),3)
