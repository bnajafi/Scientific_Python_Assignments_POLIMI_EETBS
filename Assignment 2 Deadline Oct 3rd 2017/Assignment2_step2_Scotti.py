#list of resistances

#dictionary1 : conductive resistances
Rf = {"name":"foam", "Area":0.25, "L":0.03, "k":0.026}
Rp = {"name":"plaster", "Area":0.25, "L":0.02, "k":0.22}

L_Rf = Rf["L"]
A_Rf = Rf["Area"]
k_Rf = Rf["k"]

R_value_Rf = L_Rf/(A_Rf*k_Rf)
ListOfResistances = [Rf,Rp]
totalResValueCond=0

for anyresistance in ListOfResistances:
    L_anyresistance = anyresistance ["L"]
    A_anyresistance = anyresistance ["Area"]
    k_anyresistance = anyresistance ["k"]
    name_anyresistance = anyresistance ["name"]
    RValue_anyresistance = L_anyresistance/(A_anyresistance*k_anyresistance)
    print "This is the new resistance " 
    print anyresistance
    totalResValueCond = totalResValueCond + RValue_anyresistance
    print "the resistance is" + str(totalResValueCond)
    print "*****************"

#dictionary2 : convective resistances
R_int = {"name":"internal", "h":10, "A":0.25}
R_ext = {"name":"external", "h":25, "A":0.25}

h_R_int = R_int ["h"]
A_R_int = R_int ["A"]

R_value_conv = 1/(h_R_int*A_R_int)
ListOfResistanceConv = [R_int,R_ext]
totalResValueConv=0
for anyResistanceConv in ListOfResistanceConv:
    h_anyResistanceConv = anyResistanceConv ["h"]
    A_anyResistanceConv = anyResistanceConv ["A"]
    name_anyResistanceConv = anyResistanceConv ["name"]
    RValue_anyResistanceConv = 1/(h_anyResistanceConv*A_anyResistanceConv)
    print "This is the new convective resistance "
    print RValue_anyResistanceConv
    totalResValueConv = totalResValueConv + RValue_anyResistanceConv
    print "The resistance is" + str(totalResValueConv)
    print "**************"

#dictionary3 : parallel resistances
R_plast1 = {"name":"plaster1", "Area":0.015, "L":0.16, "k":0.22}
R_plast2 = {"name":"plaster2", "Area":0.015, "L":0.16, "k":0.22}
R_brick1 = {"name":"brick", "Area":0.22, "L":0.16, "k":0.72}

L_R_plast1 = R_plast1["L"]
A_R_plast1 = R_plast1["Area"]
k_R_plast1 = R_plast1["k"]

R_value_RPlast1 = L_R_plast1/(A_R_plast1*k_R_plast1)
ListOfResistanceParallel = [R_plast1,R_plast2,R_brick1]

inv_totalResParallel=0
totalResValueParallel=0
for anyresistanceparallel in ListOfResistanceParallel:
    L_anyresistanceparallel = anyresistanceparallel ["L"]
    A_anyresistanceparallel = anyresistanceparallel ["Area"]
    k_anyresistanceparallel = anyresistanceparallel ["k"]
    name_anyresistanceparallel = anyresistanceparallel ["name"]
    R_value_anyresistanceparallel=L_anyresistanceparallel/(k_anyresistanceparallel*A_anyresistanceparallel)
    inv_resValue =_anyresistanceparallel = 1/(L_anyresistanceparallel/(k_anyresistanceparallel*A_anyresistanceparallel))
    inv_totalResParallel=inv_totalResParallel + inv_resValue
    totalResParallel=1/inv_totalResParallel
    print "The calculated resistance is " + str(R_value_anyresistanceparallel)
    print "***************"
    print "The total parallel resistance is " + str(totalResParallel)
    print "******************"
    
#total final resistance calculation
totRes=totalResValueCond + totalResValueConv + totalResParallel
print "The final total resistance is" + str(totRes)