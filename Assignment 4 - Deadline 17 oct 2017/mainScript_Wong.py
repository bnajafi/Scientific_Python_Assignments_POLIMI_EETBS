import wallCalculations_Wong as wc

glass=0.7*90/25
wood=0.22*50/25


Layers={"inside":0.12,"gypsum":0.079,
"woodfiber":0.23,"woodbevel":0.14,"winter":0.03,
"woodstud":0.63,"glass":glass,"brick":0.12,"summer":0.044,
"wood":wood,"asphalt":0.077,"plywood":0.11
}

No_studs=["inside","gypsum",
"woodfiber","woodbevel","winter",
"glass","brick"
]

Studs=["inside","gypsum",
"woodfiber","woodbevel","winter",
"woodstud","brick"
]
Roof=["inside","glass",
"plywood","asphalt","winter"
]
Door=["winter","wood","inside"]

Measurements_walls={"LwallNS":10,"LwallEW":20,"LwindowS":4,"LwindowE":4,"LwindowW":8,"Hwindow":1.8, "Ldoor":1,"Hdoor":2.2}

Tdwinter=-4.8

SidesPara=[No_studs,Studs]
SidesSerie=[Roof,Door]

Uwall= wc.wallCalc_withParallel(SidesPara,Layers)
Urd=wc.wallCalc_OnlyInSeries(SidesSerie,Layers)


dheating= 20-Tdwinter

DBrange=11.9
Aroof=Measurements_walls["LwallNS"]*Measurements_walls["LwallEW"]


Hbuilding=2.4
Awalls=Hbuilding*(Measurements_walls["LwallNS"]+Measurements_walls["LwallEW"])*2

AwinW=Measurements_walls["LwindowW"]*Measurements_walls["Hwindow"]
AwinE=Measurements_walls["LwindowE"]*Measurements_walls["Hwindow"]
AwinS=Measurements_walls["LwindowS"]*Measurements_walls["Hwindow"]
AwinSF=0.5*AwinS
AwinSO=AwinS-AwinSF
Adoor=Measurements_walls["Ldoor"]*Measurements_walls["Hdoor"]
Anetwall=Awalls-(AwinW+2*AwinE+AwinS+Adoor)

Areas={"walls":Anetwall, "ceiling":Aroof,"door":Adoor}
Uheating={"walls":Uwall,"ceiling":Urd[0],"door":Urd[1]}


rows=["walls","ceiling","door"]

def HF(parts,U,delta):
    F=[]
    for part in parts:
        MF=U[part]*delta
        F.append(MF)
    return F
HF=HF(rows,Uheating,dheating)



Qh={"Qwalls": HF[0]*Areas["walls"],"Qceiling": HF[1]*Areas["ceiling"],"Qdoor": HF[2]*Areas["door"]}

print "The heat in the layers is as follows: "+ str(Qh)
Qtotal=Qh["Qwalls"]+Qh["Qceiling"]+Qh["Qdoor"]
print "The total heat flux is " + str(Qtotal)

