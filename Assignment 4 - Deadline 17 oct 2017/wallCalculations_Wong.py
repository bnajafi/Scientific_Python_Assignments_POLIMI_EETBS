

def wallCalc_withParallel(x,L):
    Uvalue=[]
    for part in x:
        z=0
        for anylayer in part:
            z=z+L[anylayer]
            
        Uvalue.append(1/z)
    Uwinter=0.7*Uvalue[0]+0.3*Uvalue[1]
    return Uwinter
    
def wallCalc_OnlyInSeries(x,L):
    Uvalue=[]
    for part in x:
        z=0
        for anylayer in part:
            z=z+L[anylayer]
            
        Uvalue.append(1/z)
    return Uvalue
 
