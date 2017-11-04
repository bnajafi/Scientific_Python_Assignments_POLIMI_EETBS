Layers={"inside":0.12,"gypsum":0.079,
"woodfiber":0.23,"woodbevel":0.14,"outside":0.03,
"woodstud":0.63,"glass":2.45
}

Studs=["inside","gypsum",
"woodfiber","woodbevel","outside",
"glass"
]

No_studs=["inside","gypsum",
"woodfiber","woodbevel","outside",
"woodstud"
]
Sides=[No_studs,Studs]
print Sides
area_ratio=0.75

def addR(lista_de_partes,ratio):
    R={}
    
    y=0
    for part in lista_de_partes:
        z=0
        
        for anylayer in part:
            
            z=z+Layers[anylayer]
            T={anylayer:Layers[anylayer]}
            R.update(T)
            print z
        if y==0:
            P={"No_studs":z}
        else:
            P={"Studs":z}
        
        R.update(P)
        y=y+1
        print R
    Uover=(1-ratio)/(R["No_studs"])+ratio/R["Studs"]
    Q={"Uoverall":Uover}
    R.update(Q)
    return R

Rvalue=addR(Sides,area_ratio)

A=50*2.5*0.8
T1=22
T2=-2
Qflux=Rvalue["Uoverall"]*A*(T1-T2)

print "The value of the resistances in both parts(insulated and studs) is the following: ["+ str(Rvalue["No_studs"])+" , "+str(Rvalue["Studs"])+"]"
print "The total value of U is: "+str(Rvalue["Uoverall"])
print "The total heat flux is: "+str(Qflux)