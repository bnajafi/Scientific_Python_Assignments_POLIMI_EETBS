#assignemt 5 step 2 peri

#defining a generic library array
Mat_lib=np.array(["out_winter","wood_bevel","foam_ins","fiber_ins","wood_stud","gypsum","in_conv"])
Mat_res=np.array([0.03,0.14,0.98,2.52,0.63,0.079,0.12])
#defining my wall specs (series)
mywall_mat_series=np.array(["out_winter","wood_bevel",
"foam_ins","gypsum","in_conv"])

mywall_res_series=np.array(zeros(5))

#now i can fill this empty array using a loop cycle

for material in mywall_mat_series:
    mywall_res_series[mywall_mat_series==material]=Mat_res[Mat_lib==material]
    
U_series=1.0/mywall_res_series.sum()

mywall_mat_parallel=np.array(["fiber_ins","wood_stud"])

mywall_res_parallel=np.array(zeros(2))

#now i can fill this empty array using a loop cycle

for material in mywall_mat_parallel:
    mywall_res_parallel[mywall_mat_parallel==material]=Mat_res[Mat_lib==material]
    
U_parallel=1.0/mywall_res_parallel


ratio=0.70

U_section1=U_series+U_parallel[0]
U_section2=U_series+U_parallel[1]

U_tot=U_section1*ratio+U_section2*(1-ratio)

A_wall=2.5*50*0.8 
DT=24

Qtot=U_tot*DT*A_wall
print "****************************"
print "the total heat loss of the house, situated in Nevada, is: "+str(Qtot)+" W"
print "****************************"