import numpy as np
Rser =np.array([])
Lser=np.array([0.03,0.02,0.02])
Kser=np.array([0.026,0.22,0.22])
Aser=0.25
Rser=Lser/(Kser)
RserTOT=sum(Rser)/Aser

Rpara=np.array([])
Lpara=np.array([0.16,0.16,0.16])
Kpara=np.array ([0.22,0.72,0.22])
Apara=np.array([0.015,0.22,0.015])
Rpara=1/(Lpara/(Kpara*Apara))
RparaTOT=1/sum(Rpara)/Apara

Rconv=np.array([])
Ccof=np.array([10.0,25.0])
ConvR=1/Ccof
CRtot=(sum(ConvR))/Aser
Restot=CRtot+RserTOT+RparaTOT
