R1=["conv",0.25,10] # inner convective res, Area, h1
R2=["cond",0.25,0.03,0.026] # foam layer, Area, lenght, conductivity
R3=["cond",0.25,0.02,0.22] # plaster layer, Area, lenght, conductivity
R4=["cond",0.22,0.16,0.72] #brick, Area, lenght, conductivity
R5=["cond",0.015,0.16,0.22] # plaste layer, Area, lenght, conductivity
R6=["conv",0.25,25] # outer convective res, Area, h2

#LISTS

ConvRes = [R1,R6]
SeriesRes = [R2,R3,R3]
ParallRes = [R4,R5,R5]

ConvResTot=0
for res in ConvRes:
    ConvResTot=ConvResTot+1/(res[1]*res[2])
 
R_inverse=0  #method to calculate parallel of resistances with command for
for res in ParallRes:
    R_inverse=R_inverse + 1/( res[2]/(res[1]*res[3]) )
ParallResTot=1/R_inverse

SeriesResTot=0
for res in SeriesRes:
    SeriesResTot=SeriesResTot + res[2]/(res[1]*res[3])
   
Rtot= ConvResTot+ParallResTot+SeriesResTot

print "The value of the total resistance is " + str(Rtot) + " K/W"