import pandas as pd
import matplotlib.pyplot as plt


opaque_surface=["wall","ceiling","door"]
heating_load=[1149.2,1240,92.5]
cooling_load=[547.5,514.6,43]

colors=["y","r","b"]

plt.figure()
plt.pie(cooling_load,labels=opaque_surface,colors=colors, startangle=90,explode=(0.1,0.1,0),autopct='%1.1f%%')
plt.title("cooling load")
plt.show()

colors=["g","r","b"]
plt.figure()
plt.pie(heating_load,labels=opaque_surface,colors=colors, startangle=90,explode=(0.1,0.1,0),autopct='%1.1f%%')
plt.title("heating load")
plt.show()

plt.close()

area_wall=105.8

U_range=range(400,501)
U_series=pd.Series(U_range)/1000
deltaT=24.8

HF=U_series*area_wall
Q_wall=HF*area_wall

Q_w_wall= 2483-1149.2

Q_tot=Q_wall+Q_w_wall

plt.plot(U_series,Q_tot)
plt.title("U_range")
plt.show()