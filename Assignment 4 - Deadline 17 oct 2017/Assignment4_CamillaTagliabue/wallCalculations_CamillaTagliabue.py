#wallcalculations 
wallcomposition={"Gypsumwallboard":{"L":0.013,"R":0.079},
"Glassfiberinsulation":{"L":0.090,"R":2.45},
"CommonBrick":{"L":0.10, "R": 0.12} ,
"Woodfiberboard":{"L":0.013,"R":0.23} ,
"Woodbevellappedsiding":{"L":0.20, "R": 0.14},
"woodstud":{"L":0.090,"R": 0.63},
"Wood":{"L":0.050,"R":0.44},
"out":{"R":0.03},
"in":{"R":0.12}}

def wallCalc_withParallel (listA,listB,composition):  #U of the wall 
    r1=r2=0.0
    for i in listA:
        r1=r1+wallcomposition[i]["R"]
    for j in listB:
        r2=1/(1/r2+1/wallcomposition[j]["R"])
    ratio=0.70
    U=ratio*(1/r1)+(1-ratio)+(1/r2)
    return U

def wallCalc_onlyInSeries(listseriedoor,wallcomposition):
    #U of roof and door 
    res=0.0
    for anyresistance in listseriedoor:
        res=res+wallcomposition[anyresistance]["R"]
    Ud=1/res
    return Ud
    

