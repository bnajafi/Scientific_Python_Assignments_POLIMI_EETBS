import matplotlib.pyplot as plt
import pandas as pd

#heating
plt.figure()
U_wall=0.438
U_ceiling=0.25
U_door=1.694
Delta_T=24.8
A_wall=105.8
A_ceiling=200
A_door=2.2
Q_wall=Delta_T*A_wall*U_wall
Q_ceiling=Delta_T*A_ceiling*U_ceiling
Q_door=Delta_T*A_door*U_door
Q_heating=[Q_wall,Q_ceiling,Q_door]
labels=["wall","roof","door"]
cols=["b","y","r"]
plt.pie(Q_heating,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title("Q heating")

#cooling
plt.figure()
Q_cooling=[547.5,514.6,43]
labels=["wall","roof","door"]
cols=["g","b","r"]
plt.pie(Q_cooling,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1),autopct='%1.1f%%')
plt.title("Q cooling")

#changing u values
u=[0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9]
q=[]
for anyu in u:
    uValue=anyu
    Q=Delta_T*A_wall*uValue
    q.append(Q)

plt.figure()
plt.plot(u,q)
plt.xlabel("u")
plt.title("Q=f(u)")
plt.ylabel("Q")       
    