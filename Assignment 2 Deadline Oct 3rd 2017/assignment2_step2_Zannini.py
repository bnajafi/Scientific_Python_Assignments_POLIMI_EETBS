R1 = {"name": "AirIn","area":0.25,"convection coeff":10,"ResValue": 0}
R2 = {"name":"Foam","area":0.25, "lenght":0.03, "conductivity":0.026, "ResValue": 0}
R3 = {"name":"plaster1","area": 0.25, "lenght":0.02, "conductivity":0.22, "ResValue": 0}
R4 = {"name":"brick","area": 0.22, "lenght":0.16, "conductivity":0.72, "ResValue": 0}
R5 = {"name":"plaster2","area": 0.015, "lenght":0.16, "conductivity":0.22, "ResValue": 0}
R6 = {"name": "AirOut","area":0.25,"convection coeff":25,"ResValue": 0}

#Lists
ConvRes = [R1,R6]
SeriesRes = [R2,R3,R3]
ParallRes = [R4,R5,R5]

ConvResTot=0
for res in ConvRes:
    Rvalue = 1/(res["area"]*res["convection coeff"])
    res["ResValue"]=Rvalue   # update the list
    ConvResTot=ConvResTot+Rvalue

R_inverse=0   #method to calculate parallel of resistances with command for
for res in ParallRes:
    Rvalue = res["lenght"]/(res["area"]*res["conductivity"])
    res["ResValue"]=Rvalue   # update the list
    R_inverse=R_inverse + 1/( Rvalue )
ParallResTot=1/R_inverse   

SeriesResTot=0
for res in SeriesRes:
    Rvalue= res["lenght"]/(res["area"]*res["conductivity"])
    res["ResValue"]=Rvalue   # update the list
    SeriesResTot=SeriesResTot + Rvalue
   
Rtot= ConvResTot+ParallResTot+SeriesResTot

print "The value of the total resistance is " + str(Rtot) + " K/W"
