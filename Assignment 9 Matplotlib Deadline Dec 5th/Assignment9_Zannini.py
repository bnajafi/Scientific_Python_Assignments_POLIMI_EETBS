import pandas as pd
import matplotlib.pyplot as plt

index=["walls","roof","door"]

U_heating=[0.438,0.25,1.694]
U_cooling=[0.435,0.25,1.655]
Q_heating=[1149.2,1240,92.5]
Q_cooling=[547,541.6,43]

Matrix=pd.DataFrame([U_heating,U_cooling,Q_heating,Q_cooling],["U_heating","U_cooling","Q_heating","Q_cooling"],index)

fig1 = plt.figure()
plt.pie(Matrix.loc["Q_heating"],labels=labels,colors=cols,startangle=90,explode=(0,0,0),autopct='%1.1f%%')
fig2 =plt.figure()
plt.pie(Matrix.loc["Q_cooling"],labels=labels,colors=cols,startangle=90,explode=(0,0,0),autopct='%1.1f%%')

fig3= plt.figure()
Uvalues=[0.438,0.450,0.460,0.470,0.480,0.490,0.5]
Qvalues_tot=[]

for U in Uvalues:
    Qvalue=((Matrix["walls"]["Q_heating"]*U)/Uvalues[0])+(Matrix["roof"]["Q_heating"]+Matrix["door"]["Q_heating"])
    Qvalues_tot.append(Qvalue)

plt.scatter(Uvalues,Qvalues_tot,color="g",marker="*",s=50)   
plt.xlabel("U of walls")
plt.ylabel("Q Heating Opaque")
plt.title("Q vs U")