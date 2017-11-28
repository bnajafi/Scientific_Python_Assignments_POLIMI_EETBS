#ASSIGNMENT 2 PART 2
#use of dictonaries 
A=3*5
Ap=(3/0.25*0.03)*5
Ab=(3/0.25*0.22)*5
RValue1=RValue2=RValue3=RValue4=0
Ti=20
To=10
v1=v2=v3=v4=v0=v5=0
R1={"name": "resistance1(foam)","area":A,"lenght":0.03,"k":0.026,"value":v1}
R2={"name": "resistance2(plaster V)","area":A,"lenght":0.04,"k":0.22,"value":v2}
R3={"name": "resistance3(plaster Htot)","area":Ap,"lenght":0.16,"k":0.22,"value":v3}
R4={"name": "resistance4(brick)","area":Ab,"lenght":0.16,"k":0.72,"value":v4}
R0={"name": "resistance0(indoor)","area":A,"lenght":1,"k":10,"value":v0}
R5={"name": "resistance5(outdoor)","area":A,"lenght":1,"k":25,"value":v5}
CPR=[R4,R3]#list of parallel conductive resistances
CVR=[R0,R5]#list of convective resistances
CSR= [R1,R2] #conductive series resistances
Allres=[R1,R2,R3,R4,R0,R5]
for res in Allres:
    res["value"]=res["lenght"]/(res["area"]*res["k"])
    print (res
    )
gp=0
for r in CPR:
    gp=1/r["value"]+gp
rp=1/gp
print ("The equivalent parallel resistance is Req=", rp)
#series
for anyres in CSR:
    rp=rp+ anyres["value"]
for anyRes in CVR:
    rp=rp+anyRes["value"]
print ("The equivalent total resistance is Rp=",rp)
Q=(Ti-To)/rp
print ("The rate of heat transfer is Q=", Q)