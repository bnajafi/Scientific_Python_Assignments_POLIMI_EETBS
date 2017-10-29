h1=10; #convection heat transfer coefficient on the inner side
h2=25; #convection heat transfer coefficient on the outer side
Tin=20; #indooor temperature
Tout=-10; #outdoor temperature
A=(1.5+1.5+22)*0.01
#foam
Lfoam=0.03;
Kfoam=0.026;
#plaster
Lplaster=0.02;
Kplaster=0.22;
Aceiling=0.015;
#brick
Lbrick=0.16;
Kbrick=0.72;
Abrick=0.22;
#wall
Lwall=5;
Hwall=3;
Awall=Lwall*Hwall;

Rconv1=(1/(h1*A));
Rfoam=(Lfoam/(Kfoam*A));
Rplaster=(Lplaster/(Kplaster*A));
Rceiling=(Lbrick/(Kplaster*Aceiling))
Rbrick=(Lbrick/(Kbrick*Abrick));
Rceilingtot=((Rceiling*Rceiling)/(2*Rceiling))
Rparallel=((Rceilingtot*Rbrick)/(Rceilingtot+Rbrick))
Rconv2=(1/(h2*A))
Rtot =Rconv1+Rfoam+Rplaster+Rparallel+Rplaster+Rconv2
Q=(Tin-Tout)/Rtot
Qtot=Q*(Awall/A)
print("The total thermal resistance is: "+str(Rtot)+" degC/W") 
print("The rate of heat transfer through the wall is : "+str(Qtot)+" W") 