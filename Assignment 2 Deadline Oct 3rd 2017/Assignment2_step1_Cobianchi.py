#Conduction in serie
R_foam = [0.25,0.03,0.026] #Unit Area,Length,Thermal Coefficient
R_plaster1 = [0.25,0.02,0.22] 
R_plaster2 = [0.25,0.02,0.22]
#Convection in serie
R_conv1 = [0.25,10] #Unit Area, Covective Coefficient
R_conv2 = [0.25,25]
#Conduction in parallel
R_p1 = [0.015,0.16,0.22] #Unit Area,Length,Thermal Coefficient
R_p2 = [0.015,0.16,0.22]
R_brick = [0.22,0.16,0.72]

#List of Vectors (Conduction)
Rcond = [R_foam,R_plaster1,R_plaster2]
TOT1 = 0 #initialize the counter

for i in Rcond:
    Rs1 = i[1]/(i[0]*i[2])
    TOT1 = TOT1 + Rs1

#List of Vectors (Convection)
Rconv = [R_conv1,R_conv2]
TOT2 = 0

for j in Rconv:
    Rs2 = 1/(j[0]*j[1])
    TOT2 = TOT2 + Rs2

#List of Vectors (Conduction in parallel)
R_cond_p = [R_p1,R_p2,R_brick]
TOT3 = 0

for k in R_cond_p:
    Rp = 1/(k[1]/(k[0]*k[2]))
    TOT3 = TOT3 + Rp

print ("Total Unit Resistance")
print round((TOT1+TOT2+TOT3),3)
