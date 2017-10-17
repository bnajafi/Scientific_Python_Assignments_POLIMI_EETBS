h1= float(raw_input("Please input the convection heat transfer coefficient on the inner side in W/m2 "))
h2= float(raw_input("Please input the convection heat transfer coefficient on the outer side in W/m2 "))

Tin= float(raw_input("Please input the indoor temperature in degC "))
Tout= float(raw_input("Please input the outdoor temperature in degC "))

Kfoam= float(raw_input("Please input the the conduction coefficient of foam in W/mK"))
Kplaster= float(raw_input("Please input the the conduction coefficient of plaster in W/mK"))
Kbrick= float(raw_input("Please input the the conduction coefficient of brick in W/mK"))

Heightwall=float(raw_input("Please input the the height of wall in m"))
Widewall=float(raw_input("Please input the the wide of wall in m"))
Awall=Heightwall*Widewall;

Heightunit=float(raw_input("Please input the the height of unit portion of wall in m"))
wideunit=float(raw_input("Please input the the wide of unit portion of wall in m"))
Aunit=Heightunit*wideunit;

Heightceiling=float(raw_input("Please input the the height of ceiling in m"))
Wideceiling=float(raw_input("Please input the the wide of ceiling in m"))
Aceiling=Heightceiling*Wideceiling;

Hbrick=float(raw_input('height of brick in m '))
Wbrick=float(raw_input('Wide of brick in m '))
Abrick=Hbrick*Wbrick;

Lfoam=float(raw_input('Thickness of foam in m '))
Lplaster=float(raw_input('Thickness of plaster in m '))
Lbrick=float(raw_input('Thickness of brick in m '))


Rconv1=(1/(h1*Aunit));
Rfoam=(Lfoam/(Kfoam*Aunit));
Rplaster=(Lplaster/(Kplaster*Aunit));
Rceiling=(Lbrick/(Kplaster*Aceiling))
Rbrick=(Lbrick/(Kbrick*Abrick));
Rceilingtot=((Rceiling*Rceiling)/(2*Rceiling))
Rparallel=((Rceilingtot*Rbrick)/(Rceilingtot+Rbrick))
Rconv2=(1/(h2*Aunit))
Rtot =Rconv1+Rfoam+Rplaster+Rparallel+Rplaster+Rconv2
Q=(Tin-Tout)/Rtot
Qtot=Q*(Awall/Aunit)
print("The total thermal resistance is: "+str(Rtot)+" degC/W") 
print("The rate of heat transfer through the wall is : "+str(Qtot)+" W") 