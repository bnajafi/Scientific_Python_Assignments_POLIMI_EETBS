Ri= {"name": "indoor convective resistance",  "area" :0.25 , "h":10 ,"ResValue":0}
Ro= {"name": "outdoor convective resistance",  "area" :0.25 , "h":25,"ResValue":0 }

Rf= {"name": "foam layer",  "area" :0.25 , "length": 0.03, "k":0.026 ,"ResValue":0}
Rp1= {"name": "plaster layer 1",  "area" :0.25 , "length": 0.02, "k":0.22 ,"ResValue":0}
Rp2= {"name": "plaster layer 2",  "area" :0.25 , "length": 0.02, "k":0.22 ,"ResValue":0}

Rpc1= {"name": "parallel plaster layer 1",  "area" :0.015 , "length": 0.16, "k":0.22 ,"ResValue":0}
Rb= {"name": "parallel brick layer",  "area" :0.22 , "length": 0.16, "k":0.72,"ResValue":0 }
Rpc2= {"name": "parallel plaster layer 2",  "area" :0.015 , "length": 0.16, "k":0.22 ,"ResValue":0}

Res_conductive= [ Rf, Rp1 , Rp2] # list of conductive res in series
Res_convective= [Ri , Ro] # list of convective res in series
Res_parallel= [Rpc1 , Rb , Rpc2] # list of conductive res in parallel

R_cond=0
for i in Res_conductive:
    print "The conductive resistance"
    print (str(i))
    R= i["length"]/(i["area"]*i["k"])
    print "The calculated resistance is: "+ str(R)
    R_cond= R_cond+R
    print("****************")
print("The value of conductive reistance in series is "+str(R_cond))    
print ("--------------")

R_conv=0
for i in Res_convective:
    print "The convective resistance"
    print (str(i))
    R= 1/(i["area"]*i["h"])
    print "The calculated resistance is: "+ str(R)
    R_conv= R_conv+R
    print("****************")
print("The value of convective reistance in series is "+str(R_conv))  
print ("--------------")

k=0
for i in Res_parallel:
    print "The conductive resistance"
    print (str(i))
    R= i["length"]/(i["area"]*i["k"])
    print "The calculated resistance is: "+ str(R)
    k= k+R**(-1)
    print("****************")
R_parallel= k**(-1)    
print("The value of conductive resitance in parallel is "+str(R_parallel))
print ("--------------")

R_list=[R_cond,R_conv, R_parallel]
R_tot=0
for AnyResistance in R_list:
    R_tot=R_tot+AnyResistance
print("Total resistance is "+str(R_tot))
T1=20
T2=-10
Q_unit=(T1-T2)/(R_tot)
A_wall=15
A_unit=0.25
Q_wall=Q_unit*A_wall/A_unit
print("The heat rate through the wall is "+str(Q_wall)+" W")
