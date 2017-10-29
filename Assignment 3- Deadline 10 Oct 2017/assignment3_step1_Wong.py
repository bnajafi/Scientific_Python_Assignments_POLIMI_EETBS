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


Rvalue=[]
for part in Sides:
    z=0
    for anylayer in part:
        z=z+Layers[anylayer]
        print z
    Rvalue.append(z)
    print Rvalue
 

Uover=0.25/Rvalue[0]+0.75/Rvalue[1]
A=50*2.5*0.8
T1=22
T2=-2
Q=Uover*A*(T1-T2)

print "The value of the resistances in both parts(insulated and studs) is the following: "+ str(Rvalue)
print "The total value of U is: "+str(Uover)
print "The total heat flux is: "+str(Q)