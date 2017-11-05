# -*- coding: utf-8 -*-
#assignment 2 - step 2

Tinf1=20 #indoor temperature  [°C]
Tinf2=-10 #outdoor temperature [°C]

#definition and calculation of convective resistances
Rconv1={"Name":"Indoor air","h":10,"Area":0.25,"R_value":0} 
Rconv2={"Name":"Outdoor air","h":25,"Area":0.25,"R_value":0}
Rconv=[Rconv1,Rconv2]
for conv in Rconv:
    A_conv=conv["Area"]
    h_conv=conv["h"]
    conv["R_value"]=1/(A_conv*h_conv)
print("The values of the convective resistances are: R1="+str(Rconv1["R_value"])+" and R2="+str(Rconv2["R_value"])+" [°C/W]")

#definition and calculation of conductive resistances in series
Rf={"Name":"foam","Thickness":0.03,"Area":0.25,"Conductivity":0.026,"R_value":0}
Rp1={"Name":"first plaster layer","Thickness":0.02,"Area":0.25,"Conductivity":0.22,"R_value":0}
Rp2={"Name":"second plaster layer","Thickness":0.02,"Area":0.25,"Conductivity":0.22,"R_value":0}
CondResSer=[Rf,Rp1,Rp2]
for cond in CondResSer:
    L_ser=cond["Thickness"]
    K_ser=cond["Conductivity"]
    A_ser=cond["Area"]
    cond["R_value"]=L_ser/(K_ser*A_ser)
print("The values of the conductive resistances in series are: Rf="+str(Rf["R_value"])+" Rp1="+str(Rp1["R_value"])+" and Rp2="+str(Rp2["R_value"])+" [°C/W]")

#definition and calculation of conductive resistances in parallel
Rb={"Name":"brick","Thickness":0.16,"Area":0.22,"Conductivity":0.72,"R_value":0}
Rc1={"Name":"upper resistance","Thickness":0.16,"Area":0.015,"Conductivity":0.22,"R_value":0}
Rc2={"Name":"lower resistance","Thickness":0.16,"Area":0.015,"Conductivity":0.22,"R_value":0}
CondResPar=[Rb,Rc1,Rc2]
for cond in CondResPar:
    L_par=cond["Thickness"]
    K_par=cond["Conductivity"]
    A_par=cond["Area"]
    cond["R_value"]=L_par/(K_par*A_par)
print("The values of the conductive resistances in parallel are: Rb="+str(Rb["R_value"])+" Rc1="+str(Rc1["R_value"])+" and Rc2="+str(Rc2["R_value"])+" [°C/W]")
Rpar=(1/Rb["R_value"]+1/Rc1["R_value"]+1/Rc2["R_value"])**(-1)
Rparallel={"Name":"Equivalent resistance of Rb,Rc1,Rc2","R_value":Rpar}
Rtot=Rconv1["R_value"]+Rconv2["R_value"]+Rparallel["R_value"]+Rf["R_value"]+Rp1["R_value"]+Rp2["R_value"]

Hwall=3 #wall's height [m]
Wwall=5 #wall's depth [m]
Awall=Hwall*Wwall #wall's surface [m2]
Qwall=Qunit*Awall/(0.25) #heat flow crossing the entire wall [W]
print("The total resistance of the unit is: "+str(Rtot)+" [°C/W]")
print("By using the formula Qunit=(Tinf1-Tinf2)/Rtot, the heat flow crossing the unit is: "+str(Qunit)+" [W]")
print("In the end, the total heat flow crossing the entire wall is Qwall=Qunit*Awall/Aunit="+str(Qwall)+" [W]")







    
    
    


