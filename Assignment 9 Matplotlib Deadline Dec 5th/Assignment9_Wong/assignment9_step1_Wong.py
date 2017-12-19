import pandas as pd
import matplotlib.pyplot as plt

Layers={"inside":0.12,"gypsum":0.079,
"woodfiber":0.23,"woodbevel":0.14,"outside":0.03,
"woodstud":0.63,"glass":2.45,"brick":0.12,"wood":0.22*50/25,"outsidesumm":0.044
}

Studs=["inside","gypsum",
"woodfiber","woodbevel","outsidesumm",
"glass"
]

No_studs=["inside","gypsum",
"woodfiber","woodbevel","outsidesumm",
"woodstud"
]

Studsw=["inside","gypsum",
"woodfiber","woodbevel","outside",
"glass"
]

No_studsw=["inside","gypsum",
"woodfiber","woodbevel","outside",
"woodstud"
]

Door=["inside","wood","outsidesumm"
]

Doorw=["inside","wood","outside"
]
Sides=[No_studs,Studs,No_studsw,Studsw, Door, Doorw]



Rvalue=[]
for part in Sides:
    z=0
    for anylayer in part:
        z=z+Layers[anylayer]
    Rvalue.append(z)
    print Rvalue
 
Opaquesummer=[]
Opaquewinter=[]
Usummer=0.3/Rvalue[0]+0.7/Rvalue[1]
Uwinter=0.3/Rvalue[2]+0.7/Rvalue[3]

Opaquewinter.append(Uwinter)
Opaquewinter.append(0.25)
Opaquewinter.append(1/Rvalue[5])

Opaquesummer.append(Usummer)
Opaquesummer.append(0.25)
Opaquesummer.append(1/Rvalue[4])
print Opaquewinter
print Opaquesummer
Areas=[(40+20)*2.4-(5*4*1.8)-(1*2.2),20*10,1*2.2]
Tcool=7.9
Theat=24.8

QH=[]
i=0
for part in Opaquewinter:
    QH.append(Opaquewinter[i]*Areas[i]*Theat)
    i=i+1

print QH

items = [1,2,3]
labels = ["wall","roof","door"]
HeatingLoadValues = QH
cols=["r","b","g"]

# How to plot a pie chart !
plt.close("all")
plt.figure()
plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.title("Heating Load")

DR=11.9
OF=[1*Tcool+8.2-0.36*DR,0.62*Tcool+(14.3*0.85-4.5)-0.19*DR,1*Tcool+8.2-0.36*DR]
QC=[]

i=0
for part in Opaquesummer:
    QC.append(Opaquesummer[i]*Areas[i]*OF[i])
    i=i+1

print QC

items = [1,2,3]
labels = ["wall","roof","door"]
CoolingLoadValues = QC
cols=["r","b","g"]

plt.figure()
plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.title("Cooling Load")

NewUs=[Uwinter,0.7]

QHnew=[]
i=0
for part in NewUs:
    QHnew.append(NewUs[i]*Areas[i]*Theat)
    i=i+1

print QHnew

items = [1,2]
labels = ["oldwall","newwall"]
NewHeatValues = QHnew 

plt.figure()
plt.bar(items,NewHeatValues,color="g")
plt.xticks(items,labels,color="r")
