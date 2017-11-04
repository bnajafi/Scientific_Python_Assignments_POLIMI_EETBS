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

#convection parameters 
conv_o=[0.25,25]
conv_i=[0.25,10]
conv_vect=[conv_o,conv_i]
R_vect_conv=[]

for conv in conv_vect:
    Rconv=1/(conv[0]*conv[1])
    R_vect_conv.append(Rconv)
    
print ("the convective resistance values are: Ro= " +str(R_vect[0])+" Ri= "+str(R_vect[1])+" degC/W")
    
    

#component=[area,thickness,k]

foam=[0.25,0.03,0.026]
ex_plaster=[0.25,0.02,0.22]
int_plaster=[0.015,0.16,0.22]
brick=[0.22,0.16,0.72]

#parallel components

List_comp_parallel=[int_plaster,brick]
R_vector_parallel=[]


for component in List_comp_parallel:
    print "component details:"
    print component   
    res_value=component[1]/(component[0]*component[2])
    R_vector_parallel.append(res_value)
    print "calculated resistance for this component : "+str(res_value)+" degC/W"
    print "********************"
print "parallel resistances vector in order is: "+str(R_vector_parallel)

#series components

List_comp_series=[foam,ex_plaster]
R_vector_series=[]

for comp in List_comp_series:
    print "component details:"
    print comp   
    R_value=comp[1]/(comp[0]*comp[2])
    R_vector_series.append(R_value)
    print "calculated resistance for this component : "+str(R_value)+" degC/W"
    print "********************"
print "series resistances vector in order is: "+str(R_vector_series)

R_parallel=1/((1/R_vector_parallel[0])+(1/R_vector_parallel[0])+(1/R_vector_parallel[1]))
R_tot=R_parallel+R_vect_conv[0]+R_vect_conv[1]+R_vector_series[0]+R_vector_series[1]+R_vector_series[1]

print "\n The total resistance is : "+str(R_tot)+ " degC/W"

#heat transfer calculation
q=(Ti-To)/(R_tot*0.25)
Q=q*(A_tot)

print("\n The total heat transfer of the considered wall is: " +str(Q)+ " W")
    
