#this program is going to ask all the properties, characteristics, number of layers and number of parallel layers of each layer, and calculate the heat transfer
#first it calculate the convection heat transfer
#then we inform it about number of layers
#for each layer we give the number of parallel layers that it has
#by entering the area, length, and K of each layer and each parallel layer, it will calculate the total resistance of the wall
#finally we enter the area of the wall

res_tot=0
r1=1

#calc of thermal convection
h_in=raw_input("enter convection coefficient of inner side of the wall    ")
h_in=float(h_in)
a_in=raw_input("enter area of inner side of the wall    ")
a_in=float(a_in)
h_out=raw_input("enter convection coefficient of outer side of the wall    ")
h_out=float(h_out)
a_out=raw_input("enter area of outer side of the wall    ")
a_out=float(a_out)

res_tot=1/(h_in*a_in)+1/(h_out*a_out) #convection terms resistance




#number of layers

no_layers=raw_input("indicate the number of conduction layers    ")
no_layers=int(no_layers)
i=0
for i in range(0,no_layers):
#number of parallel layers in each layer
    no_parallels=raw_input("indicate the number of parallel layers in layer number " + str(i+1) )
    no_parallel=int(no_parallels)
    p=0 
    
    
    r1=0
    #calc the resistance of each layer
    for p in range(0,no_parallel):
        if no_parallel>1:
            print("indicate the characteristics of parallel layer number "+str(p+1)+"  in layer number " +str(i+1)+ "  respictively    ")
        l=raw_input("please indicate the length of parallel layer number "+str(p+1)+" in layer number  "+str(i+1) ) 
        l=float(l)
        a=raw_input("and its area?    ")
        a=float(a)
        k=raw_input("also the thermal conductivity?    ")
        k=float(k)
        r=l/(k*a)
        r1+=1/r
    res_tot=res_tot+1/r1
    
    
print "The total Thermal Resistance of the wall is     "+ str(res_tot)+" degC/W"


#enter temperatures
t_in=raw_input("enter the inside temperature")
t_in=float(t_in)
t_out=raw_input("enter the outside temperature")    
t_out=float(t_out)

#calc thermal flow for unit of the wall

Q=(t_in-t_out)/res_tot
print "the thermal flow for the specified unit of wall's area is " +str( Q);
a_wall=raw_input(" Enter the area of the wall? ")
a_wall=float(a_wall)
q_tot=0

q_tot= (Q*a_wall)/a_in
print "The total thermal flowing through the wall is " +str(q_tot)+" W"
            
        
        
                 
  
    





