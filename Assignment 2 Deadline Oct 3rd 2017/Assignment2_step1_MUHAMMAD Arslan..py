# 30/09/17
#  ----------------Assignment-2--Step-1--------------------
#  ---Example-D (Calculation of Heat transfer through multi-layer wall)----

# ------------------MUHAMMAD ARSLAN--------------------


# What I have done here, Rin & Rout taken as Rconv; Rcond is sum of Rplasters & Rfoam; Rpp accounts for parallel plaster resistance; Rb is brick resistance

Rc1= [0.25,0.02,0.22]    # Area;0,Length;1,plaster conductivity;2
Rc2= [0.25,0.02,0.22]    # Area;0,Length;1,plaster conductivity;2
Rf=  [0.25,0.03,0.026]   # Area;0,Length;1,foam conductivity;2

Ri=   [0.25,10]           # Area;0,Inner convective co-efficient;1
Ro=   [0.25,25]           # Area;0,Outer convective co-efficient;1

Rp1=   [0.015,0.16,0.22]   # Area;0,Length;1,conductivity;2
Rp2=   [0.015,0.16,0.22]   # Area;0,Length;1,conductivity;2
Rb=    [0.22,0.16,0.72]    # Area;0,Length;1,conductivity;2


#-----------------By Using List---------------------------------------------#

ListOfResistances1= [Rc1,Rc2,Rf] #Conductive resistances in series

ListOfResistances2= [Rp1,Rp2,Rb] #Conductive resistances in parallel

ListOfResistances3= [Ri,Ro] #Convective resistances in series



    
#-----------For-Rconduction----------#    #Series Resistances

TotalResValueSC=0
for anyRes in ListOfResistances1: 
    print "here is new resistance:"
    print anyRes
    L_SC= anyRes[1]
    A_SC= anyRes[0]
    k_SC= anyRes[2]
    RValue_RSC= L_SC/(A_SC*k_SC)
    print"  so the calculated resistance is " +str(RValue_RSC)
    print" ***********"
    TotalResValueSC = TotalResValueSC+RValue_RSC
    print"  so the total conduction resistance in series is " +str(TotalResValueSC)
    print"  **************************"
    
  

#-----------For-Rparallel----------#        #Conduction Resistances


TotalResValuePC=2
for anyRes in ListOfResistances2: 
    print "here is new resistance:"
    print anyRes
    L_PC= anyRes[1]
    A_PC= anyRes[0]
    k_PC= anyRes[2]
    RValue_RPC= L_PC/(A_PC*k_PC)
    print"  so the calculated resistance is " +str(RValue_RPC)
    print" ***********"
    TotalResValuePC = 1/((1/TotalResValuePC)+(1/RValue_RPC))
    print"  so the total conduction resistance in Parallel is " +str(TotalResValuePC)
    print"  **************************"
      



#-----------For-Rconvection----------#        #Series Resistances

TotalResValueSCv=0
for anyRes in ListOfResistances3: 
    print "here is new resistance:"
    print anyRes
    A_SCv= anyRes[0]
    h_SCv= anyRes[1]
    RValue_RSCv= (1/(h_SCv*A_SCv))
    print"  so the calculated resistance is " +str(RValue_RSCv)
    print" ***********"
    TotalResValueSCv = TotalResValueSCv+RValue_RSCv
    print"  so the total convection resistance in series is " +str(TotalResValueSCv)
    print"  **************************"
 

#-----------------------------------------#
# calculated total resistance for heat transfer

Rtotal= TotalResValueSC+TotalResValuePC+TotalResValueSCv # Sum of the all type of resistances
print "The total resistance to heat transfer is "+str(Rtotal)+ "(deg C/W)"

#-----------Let's calculate Heat Transfer--------------#

Aw=15                    #Area of wall in sq.meters
Au=0.25                  #Area of unit in sq.meters
Tunit= Aw/Au

Ti=273+20                #Inner temperature in K
To=273-10                #Outer temperature in K

Dt=Ti-To

Qunit= Dt/Rtotal          #Heat transfer per unit in watt

Qwall= Qunit*Tunit      #Total heat transfer through wall
print "Thus, Total heat transfer is "+str(Qwall)+ "(watt)"