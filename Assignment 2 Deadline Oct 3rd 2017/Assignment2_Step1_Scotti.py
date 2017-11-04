#list od resistances 

#list 1 : conductive 
Rf = [0.25, 0.03, 0.026] #foam: Area, L, k
Rp = [0.25, 0.02, 0.22] #plaster: Area, L, k

A_Rf = Rf [0]
L_Rf = Rf [1]
k_Rf = Rf [2]
R_value_Rf = L_Rf/(A_Rf*k_Rf)

ListOfResistances = [Rf,Rp]
totalResValueCond = 0
for anyresistance in ListOfResistances:
    print "This is the new conductive resistance "
    L_anyresistance = anyresistance [1]
    A_anyresistance = anyresistance [0]
    k_anyresistance = anyresistance [2]
    Rvalue_anyresistance = L_anyresistance/(k_anyresistance*A_anyresistance)
    totalResValueCond = totalResValueCond+Rvalue_anyresistance
    print Rvalue_anyresistance
    print "***********"

#list 2 : convective
R_int = [10, 0.25] #internal: h, Area
R_ext = [25, 0.25] #external: h, Area
h_R = R_int [0]
A_R = R_int [1]

R_value_intext = 1/(h_R*A_R)
ListOfResistancesConv = [R_int,R_ext]
totalResValueConv=0
for anyresistanceconv in ListOfResistancesConv:
    print "This is the new convective resistance "
    h_anyresistanceconv = anyresistanceconv [0]
    A_anyresistanceconv = anyresistanceconv [1]
    R_value_anyresistanceconv = 1/(h_anyresistanceconv*A_anyresistanceconv)
    totalResValueConv = totalResValueConv + R_value_anyresistanceconv
    print R_value_anyresistanceconv
    print "**************"

#list 3 : parallel
R_plast1 = [0.015, 0.16, 0.22] #plaster: Area, L, k
R_plast2 = [0.015, 0.16, 0.22] #plaster: Area, L, k
R_brick1 = [0.22, 0.16, 0.72] #brick: area, L, k
ListOfResistanceParallel = [R_plast1,R_plast2,R_brick1]
inv_totalResParallel=0
totalResParallel=0
for anyresistanceparallel in ListOfResistanceParallel:
    L_anyresistanceparallel = anyresistanceparallel [1]
    A_anyresistanceparallel = anyresistanceparallel [0]
    k_anyresistanceparallel = anyresistanceparallel [2]
    R_value_anyresistanceparallel=L_anyresistanceparallel/(k_anyresistanceparallel*A_anyresistanceparallel)
    inv_resValue =_anyresistanceparallel = 1/(L_anyresistanceparallel/(k_anyresistanceparallel*A_anyresistanceparallel))
    inv_totalResParallel=inv_totalResParallel + inv_resValue
    totalResParallel=1/inv_totalResParallel
    print "The calculated resistance is " + str(R_value_anyresistanceparallel)
    print "***************"
    print "The total parallel resistance is " + str(totalResParallel)
    print "******************"
    
#total final resistance
totalRes = totalResValueCond + totalResValueConv + totalResParallel
print "The final total resistance is" + str(totalRes)