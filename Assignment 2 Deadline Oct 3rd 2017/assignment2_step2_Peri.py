#EX 3

#script using lists and for loop

#wall geometry
A=0.25

L=5.0
H=3.0
A_tot=H*L


#ambiental conditions (o=outdoor,i=indoor)
To=-10.0
Ti=20.0

#convection 
conv_o={"name":"R_conv_out","A":0.25,"h":25}
conv_i={"name":"R_conv_in","A":0.25,"h":10}

list_conv=[conv_o,conv_i]
Rconv_tot=0

for conv in list_conv:
    Rconv=1/(conv["h"]*conv["A"])
    Rconv_tot=Rconv_tot+Rconv

print ("total convection resistance is: "+str(Rconv_tot)+" degC/W")
    



#components using dictionaries si={"data":n,....}

s1={"material":"foam","A":0.25,"thickness":0.03,"k":0.026,"R":0}
s2={"material":"external_plaster","A":0.25,"thickness":0.02,"k":0.22,"R":0}
s3={"material":"internal_plaster","A":0.015,"thickness":0.16,"k":0.22,"R":0}
s4={"material":"brick","A":0.22,"thickness":0.16,"k":0.72,"R":0}

#parallel
List_comp_parallel=[s3,s4]



for component in List_comp_parallel:
    print "component details:"
    print component   
    res_value=component["thickness"]/(component["k"]*component["A"])
    component["R"]=res_value
    print "calculated resistance for this component : "+str(res_value)+" degC/W"
    print "********************"
#series
List_comp_series=[s1,s2]



for comp in List_comp_series:
    print "component details:"
    print comp   
    res_value=comp["thickness"]/(comp["k"]*comp["A"])
    comp["R"]=res_value
    print "calculated resistance for this component : "+str(res_value)+" degC/W"
    print "********************"
    
R_parallel=1/((1/s4["R"])+(1/s3["R"])+(1/s3["R"]))
R_tot=s1["R"]+2*s2["R"]+R_parallel+Rconv_tot

print "\n The total resistance is : "+str(R_tot)+ " degC/W"

#heat transfer calculation
q=(Ti-To)/(R_tot*0.25)
Q=q*(A_tot)

print("\n The total heat transfer of the considered wall is: " +str(Q)+ " W")
    

    
