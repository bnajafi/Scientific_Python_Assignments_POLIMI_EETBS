#assign the variables and calculate resistance
#in
area_wall=15
h_in=10
area_in=0.25
res_in=1/(h_in*area_in)
#foam
k_foam=0.026
area_foam=0.25
length_foam=0.03
res_foam=length_foam/(k_foam*area_foam)
#plaster
length_plaster=0.02
area_plaster=0.25
k_plaster=0.22
res_plaster1=length_plaster/(k_plaster*area_plaster)
#there is another plaster layer with same characteristics
res_plaster2=res_plaster1
#parallel layer 
length_parallel=0.16
area_plaster_p=0.015
res_plaster_p1=length_parallel/(area_plaster_p*k_plaster)
res_plaster_p2=res_plaster_p1
#brick
length_brick=0.16
area_brick=0.22
k_brick=0.72
res_brick=length_brick/(k_brick*area_brick)
res_tot_p=1/(1/res_brick+1/res_plaster_p1+1/res_plaster_p2)
#outer side
h_out=25
res_out=1/(h_out*area_in)
#total resistance calc
res_total=res_in+res_foam+res_plaster2+res_plaster1+res_tot_p+res_out
#calculation of heat
temp_in=20
temp_out=-10
q=(temp_in-temp_out)/res_total

q_tot=q*area_wall/area_foam
print("total resistance is "+str(res_total)+ " C/W")
print("The total heat transfer of the wall is " +str(q_tot)+" W")




