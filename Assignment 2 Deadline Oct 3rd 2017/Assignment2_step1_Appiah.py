# Using List to for resistance calculations
A_wall = 15   # Area of wall [m^2]
A_unit = 0.25     #unit area ((H_brick+T_p2*2)*W_wall) 

T_1 = 20 #indoor temperature
T_2 = -10 #outdoor temperature

#List of resistances
R_f = [0.03,0.25,0.026]# Length, Area and conductivity of foam 
R_b = [0.16,0.22,0.72] # Length, Area and conductivity of brick  

R_p1 = [0.02,0.25,0.22] # thickness, Area and conductivity of Vertical Plaster side 1
R_p2 = [0.02,0.25,0.22] # thickness, Area and conductivity of Vertical Plaster side 2

R_c1 = [0.16,0.015,0.22] # Length, Area and conductivity of horizontal Plaster side 1
R_c2 = [0.16,0.015,0.22] # Length, Area and conductivity of horizontal Plaster side 2

R_1 = [0.25,10] # Area and convection heat transfer coefficient of inner
R_2 = [0.25,25] # Area and convection heat transfer coefficient of external 

# for parallel Resistance:
R_parallel = [R_c1,R_b,R_c2] # list of resistances in parallel
Total_Parallel = 9999999999999999999999999999999999999999999

for anyRes in R_parallel:
    print anyRes
    L_anyRes = anyRes[0]
    A_anyRes = anyRes[1]        
    k_anyRes = anyRes[2]
    RValue_anyRes = L_anyRes/(k_anyRes * A_anyRes)
    print "The calculated resistance is "+str( RValue_anyRes)+ " degC/W"
    Total_Parallel = 1/((1/Total_Parallel)+(1/RValue_anyRes))  #total resistance in Parallel calculation 
print "The equivalent Resistance in Parallel is "+str(Total_Parallel)+ " degC/W" 
print '********************************************************************'

# for series Resistance conductive:
Rcond_series = [R_f,R_p1,R_p2]
total_series1 = 0

for anyRes in Rcond_series:
    print anyRes
    L_anyRes = anyRes[0]
    A_anyRes = anyRes[1]        
    k_anyRes = anyRes[2]
    RValue_anyRes = L_anyRes/(k_anyRes * A_anyRes)
    print "The calculated resistance is "+str( RValue_anyRes)+ " degC/W"
    total_series1 += RValue_anyRes # total series resistances
print "The equivalent Resistance in series is "+str( total_series1)+ " degC/W" 
print '********************************************************************'

    
# for series Resistance Convective
Rconv_series = [R_1,R_2]
total_series2 =0

for anyRes in Rconv_series:
    print anyRes
    A_anyRes = anyRes[0]        
    h_anyRes = anyRes[1]
    RValue_anyRes = 1/(h_anyRes * A_anyRes)
    print "The calculated resistance is "+str( RValue_anyRes)+ " degC/W"
    total_series2 += RValue_anyRes # total series resistances
print "The equivalent Resistance in series is "+str( total_series2)+ " degC/W" 
print '********************************************************************'

# Total resistance
R_tot= Total_Parallel + total_series1 + total_series2

# Heat transfer
Q_unit = (T_1 - T_2) / R_tot #total heat transfer through the wall per unit width [W]
Q_wall = Q_unit * (A_wall/A_unit) #total heat transfer through the wall [W]

print 'The total thermal resistance is '+str(R_tot)+ ' degC/W'
print 'The rate of heat transfer through the wall is '+str(Q_wall)+ ' W'


    