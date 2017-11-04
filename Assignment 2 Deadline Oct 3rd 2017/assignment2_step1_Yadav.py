##Lists format

## conductive Resistances in Series

Rf=[0.03,0.026,0.25]      #foam Conducive resistance (L=0.03;k=0.026;A=0.25) 
Rp1=[0.02,0.22,0.25]      #Plaster side1 Conductive resistance (L=0.02;k=0.22;A=0.25)
Rp2=[0.02,0.22,0.25]      #Plaster side2 Conductive resistance (L=0.02;k=0.22;A=0.25)

R_Cond_S=[Rf,Rp1,Rp2]
Re_total1=0
for any_RS in R_Cond_S:
    print("here is the new resistance ")
    print (any_RS)
    L_any_RS=any_RS[0]
    k_any_RS=any_RS[1]
    A_any_RS=any_RS[2]
    Rcond_any_RS= L_any_RS/(A_any_RS*k_any_RS)
    Re_total1=Re_total1 + Rcond_any_RS
    print ("the calculated resistance is "+str(Rcond_any_RS)) 
    print("******")
print("so the total resistance for conduction in series is "+str(Re_total1))

#Convection resistances in series 

Rconv1=[0.25,10] # inner side Convective resistance (h=10 ; A=0.25)
Rconv2=[0.25,25] # outer side Convective resistance (h=25 ; A=0.25)

R_conv_S=[Rconv1,Rconv2]

Re_total2=0
for any_RS in R_conv_S:
    print("here is the new resistance ")
    print (any_RS)
    A_any_RS=any_RS[0]
    h_any_RS=any_RS[1]
    Rconv_any_RS= 1/(A_any_RS*h_any_RS)
    Re_total2=Re_total2+Rconv_any_RS
    print ("the calculated resistance is "+str(Rconv_any_RS)) 
    print("******")
print("so the total resistance for convection is "+str(Re_total2))

#Conduction resistances in parallel

Rbp1=[0.015,0.16,0.22]    # plastic-brick1 Conductive resistance (A=0.015;L=0.16;k=0.22)
Rb=[0.22,0.16,0.72]       # Brick Conductive resistance (A=0.22;L=0.16;k=0.72)
Rbp2=[0.015,0.16,0.22]    # plastic-brick2 Conductive resistance (A=0.015;L=0.16;k=0.22)


R_Cond_P=[Rbp1,Rb,Rbp2]

Re_total3=0
for any_Rp in R_Cond_P:
    print("here is the new resistance ")
    print (any_Rp)
    L_any_Rp=any_Rp[1]
    A_any_Rp=any_Rp[0]
    k_any_Rp=any_Rp[2]
    R_cond_any_RP=1/((L_any_Rp/(A_any_Rp*k_any_Rp)))
    Re_total3=Re_total3+R_cond_any_RP
    Re_total3p=1/Re_total3
    print ("the calculated resistance is "+str(R_cond_any_RP)) 
    print("******")
print("so the total resistance for conduction in parallel is "+str(Re_total3p))

H_wall = 3             # height of foam in m
A_unit=0.25*1            # Area of the wall per unit width 
W_wall =5                # width of wall in m 
A_wall=H_wall*W_wall     #Total area of wall 

T1 = 20     # Indoor temp of wall in degree C
T2 =-10.0  # outdoor temp of wall in degree C



R_total =Re_total1+Re_total3p+Re_total2
print("***************")
print("total resistance of the system is "+str(R_total))

Q_unit=(T1-T2)/R_total


Q_tot=Q_unit*(A_wall/A_unit)

print("************")
print (  "the total heat transfer through the wall is  " + str (Q_tot)+ " W" )




