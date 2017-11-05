print
print "Heat Loss Through a Composite Wall" # what the program do

#define the dimensions of the wall - cross section Area 
sizeA = float(raw_input("- enter the height of the wall in meters [m]: ")) 
sizeB = float(raw_input("- enter the width of the wall in meters [m]: "))

#compute the area 
Area = sizeA * sizeB
print "  Area of the Wall is: ", Area , "[m^2]"

#define the dimensions of the unit
unit_width = float(1.0) #fix variable. unit's width in [m].
unit_height = float(0.25) #fix variable. unit's height in [m]
unit_area = float(unit_width * unit_height)
print "  Area of the unit: " +str(unit_area)+ "[m^2]"

#this function computes the two convection resistances of inlet and outlet ambient
def convR(coefficient1, coefficient2, area):
    cR_1 = float(1/(coefficient1 * area))
    cR_2 = float(1/(coefficient2 * area))
    return (cR_1+cR_2)

#this function computes the three conduction series resistors
def condR(coeff1,coeff2,len1,len2,area):
    r_1 = float(len1/(coeff1*area))
    r_2 = float(len2/(coeff2*area))
    return (r_1 + 2*(r_2))
            
#compute the convection resistance (resistenze in serie)
h1 = float(raw_input("- enter the heat transfer coefficient inside: "))
h2 = float(raw_input("- enter the heat transfer coefficient outside: "))
R_tot_conv = float(convR(h1,h2,unit_area))
print "  The total convection resistance is: "+str(R_tot_conv)+ "[C/W]"

print

#compute the conduction resistance (resistenze in serie)
k1 = float(raw_input("- enter the thermal conductivity of foam in [W/mC]: "))
k2 = float(raw_input("- enter the thermal conductivity of plaster in [W/mC]: "))
L1 = float(raw_input("- enter the length of foam in [m]: "))
L2 = float(raw_input("- enter the lenght of plaster in [m]: "))
R_cond = float(condR(k1,k2,L1,L2,unit_area))

print "  The total conduction resistance (in serie) is: "+str(R_cond)+ "[C/W]"

#parallel series
k3 = float(raw_input("- enter the thermal conductivity of bricks in [W/mC]: "))
l2 = float(raw_input("- enter the length of plaster in [m]: "))
l3 = float(raw_input("- enter the length of brick in [m]: "))
A2 = 0.015 #section area of plaster
A3 = 0.22 #section area of brick
Rp1 = 1/condR(k3,1,l3,0,A3)
Rp2 = 1/condR(k2,1,l2,0,A2)
R_tot_parallel = Rp1 + 2*Rp2

print "  The total conduction resistance (in paralllel) is: "+str(R_tot_parallel)+ "[C/W]"
print
print

R_TOT = R_tot_parallel + R_cond
print "  The total Resistance is: "+str(R_TOT)+ "[C/W]"

Tin = 20 # Indoor temp of wall in C
Tout = -10 # outdoor temp of wall in C
Qunit =  (Tin-Tout)/R_TOT #total heat transfer through the unit in W 
Qtotal = Qunit*(Area/unit_area) # total heat transfer through the wall in W

print "  Total heat transfer through the wall per unit width is " +str(Qunit)+ "[W]"
print "  The total heat transfer through the wall is " + str(Qtotal)+  "[W]"