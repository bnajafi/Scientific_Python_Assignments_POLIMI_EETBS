# -*- coding: utf-8 -*-
#assignment 2 - step 1

Tinf1=20 #indoor temperature  [°C]
Tinf2=-10 #outdoor temperature [°C]

#definition of convective resistances
Rconv1=[10,0.25] #[conv.coeffcient,area]
Rconv2=[25,0.25] #[conv.coeffcient,area]
ConvRes=[Rconv1,Rconv2] #list of convective resistances
Rconv=[] #empty list of concective resistances that I will fill in the following for loop

for conv in ConvRes:
    h_conv=conv[0]
    area_conv=conv[1]
    Rconv_value=1/(h_conv*area_conv)
    Rconv.append(Rconv_value)
print("The values of the convective resistances are: R1="+str(Rconv[0])+" and R2="+str(Rconv[1])+" [°C/W]")

#definition of conductive resistances in series
Rf=[0.03,0.026,0.25] #[thickness,conductivity,area]
Rp1=[0.02,0.22,0.25] #[thickness,conductivity,area]
Rp2=[0.02,0.22,0.25] #[thickness,conductivity,area]  
CondResSer=[Rf,Rp1,Rp2] #list of conductive resistances in series
Rcond_ser=[] #empty list of conductive resistances in series that I will fill in the following for loop
for cond in CondResSer:
    L_ser=cond[0]
    K_ser=cond[1]
    A_ser=cond[2]
    Rser_value=L_ser/(K_ser*A_ser)
    Rcond_ser.append(Rser_value)
print("The values of the conductive resistances in series are: Rf="+str(Rcond_ser[0])+" Rp1="+str(Rcond_ser[1])+" and Rp2="+str(Rcond_ser[2])+" [°C/W]")

#definition of conductive resistances in parallel
Rb=[0.16,0.72,0.22] #[thickness,conductivity,area]
Rc1=[0.16,0.22,0.015] #[thickness,conductivity,area]
Rc2=[0.16,0.22,0.015] #[thickness,conductivity,area]
CondResPar=[Rb,Rc1,Rc2]
Rcond_par=[] #empty list of conductive resistances in series that I will fill in the following for loop
for cond in CondResPar:
    L_par=cond[0]
    K_par=cond[1]
    A_par=cond[2]
    Rpar_value=L_par/(K_par*A_par)
    Rcond_par.append(Rpar_value)
print("The values of the conductive resistances in parallel are: Rb="+str(Rcond_par[0])+" Rc1="+str(Rcond_par[1])+" and Rc2="+str(Rcond_par[2])+" [°C/W]")
Rpar=[(1/Rcond_par[0]+1/Rcond_par[1]+1/Rcond_par[2])**(-1)]

#definition of the total resistance as a list containing all the computed resistances
Rtot=Rcond_ser+Rpar+Rconv

#for loop to calculate the total resistance
ResTot=0
for anyresistance in Rtot:
    ResTot=ResTot+anyresistance
print("The value of the total resistance is: Rtot="+str(ResTot)+" [°C/W]")

Qunit=(Tinf1-Tinf2)/ResTot #heat flow crossing the unit [W]
Hwall=3 #wall's height [m]
Wwall=5 #wall's depth [m]
Awall=Hwall*Wwall #wall's surface [m2]
Qwall=Qunit*Awall/(0.25) #heat flow crossing the entire wall [W]
print("By using the formula Qunit=(Tinf1-Tinf2)/Rtot, the heat flow crossing the unit is: "+str(Qunit)+" [W]")
print("In the end, the total heat flow crossing the entire wall is Qwall=Qunit*Awall/Aunit="+str(Qwall)+" [W]")
    
