def wallCalc_withParallel(jointLayer,jointR,parLayer,parR,ratio):
    
    Utot=((ratio/(jointR.sum()+parR[parLayer=="glassfiberinsulation"])+(1-ratio)/(jointR.sum()+parR[parLayer=="woodstud"])))
    return(float(Utot))
    
def wallCalc_onlyInSeries(L1):
    Utot=L1.sum()
    return(1/Utot)
        










