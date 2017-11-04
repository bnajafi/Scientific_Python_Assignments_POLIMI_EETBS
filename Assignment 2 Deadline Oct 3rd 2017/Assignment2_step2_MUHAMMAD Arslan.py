# 01/10/17
#  ----------------Assignment-2--Step-2--------------------
#  ---Example-D (Calculation of Heat transfer through multi-layer wall)----

# ------------------MUHAMMAD ARSLAN--------------------


# What I have done here, Rin & Rout taken as Rconv; Rcond is sum of Rplasters & Rfoam; Rpp accounts for parallel plaster resistance; Rb is brick resistance
# Assume width of wall is 1meter

# Given data:

Rc1= {"Area":0.25,"length":0.02,"k":0.22}    
Rc2= {"Area":0.25,"length":0.02,"k":0.22}
Rf=  {"Area":0.25,"length":0.03,"k":0.026}

Ri=   {"Area":0.25,"h":10}
Ro=   {"Area":0.25,"h":25}

Rp1=   {"Area":0.015,"length":0.16,"k":0.22}
Rp2=   {"Area":0.015,"length":0.16,"k":0.22}
Rb=    {"Area":0.22,"length":0.16,"k":0.72}


#-----------------By Using Dictionaries---------------------------------------------#

Res_SCn= [Rc1,Rc2,Rf] #Conductive resistances in series

Res_PCn= [Rp1,Rp2,Rb] #Conductive resistances in parallel

Res_SCv= [Ri,Ro]      #Convective resistances in series



    
#-----------For-Rconduction----------#    #Series Resistances

TotalResValueSC=0
for anyRes in Res_SCn: 
    print "here is new resistance:"
    print anyRes
    
    RValue_RSC= anyRes["length"]/(anyRes["Area"]*anyRes["k"])
    print"  so the calculated resistance is " +str(RValue_RSC)
    print" ***********"
    TotalResValueSC = TotalResValueSC+RValue_RSC
    print"  so the total conduction resistance in series is " +str(TotalResValueSC)
    print"  **************************"
    
  

#-----------For-Rparallel----------#        #Conduction Resistances


TotalResValuePC=2
for anyRes in Res_PCn: 
    print "here is new resistance:"
    print anyRes

    RValue_RPC= anyRes["length"]/(anyRes["Area"]*anyRes["k"])
    print"  so the calculated resistance is " +str(RValue_RPC)
    print" ***********"
    TotalResValuePC = 1/((1/TotalResValuePC)+(1/RValue_RPC))
    print"  so the total conduction resistance in Parallel is " +str(TotalResValuePC)
    print"  **************************"
      



#-----------For-Rconvection----------#        #Series Resistances

TotalResValueSCv=0
for anyRes in Res_SCv: 
    print "here is new resistance:"
    print anyRes

    RValue_RSCv= (1/(anyRes["h"]*anyRes["Area"]))
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
print "Thus, the change in temperature is "+str(Dt)+ "(kelvin)"
print "***************************************"


Qunit= Dt/Rtotal          #Heat transfer per unit in watt
print "Thus, the heat transfer through unit is "+str(Qunit)+ "(watt)"
print "***************************************"

Qwall= Qunit*Tunit      #Total heat transfer through wall
print "Thus, Total heat transfer through wall is "+str(Qwall)+ "(watt)"
print "***************************************"