L1=["outsidesurface","gypsumwallboard","woodfiber","woodbevellapped","insidesurface"]
L2=["glassfiberinsulation","woodstud"]
Material_Library={"outsidesurface":{"Rvalue":0.03},"glassfiberinsulation":{"Rvalue":0.7*90/25,"length":25},"gypsumwallboard":{"Rvalue":0.079,"length":13},"woodstud":{"Rvalue":0.63},"woodfiber":{"Rvalue":0.23,"length":13},"woodbevellapped":{"Rvalue":0.14},"insidesurface":{"Rvalue":0.12}}

def X(L1,L2,ratio,Library):
    Utot=0
    for i in L2:
        Rtot=0
        for x in L1:
            Rtot+=Library[x]["Rvalue"]
        if i=="glassfiberinsulation":
            Utot+=ratio/(Rtot+Material_Library[i]["Rvalue"])
        elif i=="woodstud":
            Utot+=(1-ratio)/(Rtot+Material_Library[i]["Rvalue"])
    return(Utot)

Utot=X(L1,L2,0.75,Material_Library)
Rfinal=1/Utot

Q=int(0.8*50*2.5*24*Utot)
print "Total Heat Transfer Coefficient is " +str(Utot)+" W/m2.degreeC"
print "Total Heat Resistance is " +str(Rfinal)+" m2.degreeC/W"
print "Total Heat Transfered through the Wall is " +str(Q)+" W"
    
    
    