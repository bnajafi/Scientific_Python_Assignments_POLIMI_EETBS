import numpy as np

Resistanceinseries=np.array([])
Longinseries=np.array([0.03,0.02,0.02])
Kinseries=np.array([0.026,0.22,0.22])
Ainseries=0.25
Resistanceinseries=Longinseries/(Kinseries)
TotResistanceinseries=(sum(Resistanceinseries))/Ainseries

Resistanceinparallel=np.array([])
RecResistanceinparallel=np.array([])
Longinparallel=np.array([0.16,0.16,0.16])
Kinparallel=np.array([0.22,0.72,0.22])
Ainparallel=np.array([0.015,0.22,0.015])
Resistanceinparallel=Longinparallel/(Ainparallel*Kinparallel)
RecResistanceinparallel=1/Resistanceinparallel
TotResistanceinparallel=1/sum(RecResistanceinparallel)

ConvectiveResistance=np.array([])
ConvectiveCoefficient=np.array([10.0,25.0])
ConvectiveResistance=1/ConvectiveCoefficient
TotConvectiveResistance=(sum(ConvectiveResistance))/Ainseries

ResTot=TotConvectiveResistance+TotResistanceinparallel+TotResistanceinseries

