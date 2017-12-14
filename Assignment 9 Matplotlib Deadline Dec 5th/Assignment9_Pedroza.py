import pandas as pd
import matplotlib.pyplot as plt

items = [1,2,3]
labels = ["wall","ceiling","door"]
HeatingLoadValues = [1149.2,1240,92.5]

#Pie Chart for heating load
cols=["r","b","g"]
plt.figure()
fig1=plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.title("Heating load distribution for opaque surfaces")

#Pie Chart for cooling load
CoolingLoadValues=[547.5,514.6,43]
plt.figure()
fig2=plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.title("Cooling load distribution for opaque surfaces")

#Change of Q with respect to U
U_Wall = pd.Series([0.3, 0.32, 0,34, 0.36, 0.38, 0.40, 0.42, 0.44])

def Q_cal(U):
    A=105.8
    DT=24.8
    Q_value = DT*A*U
    Q_door = 92.5
    Q_ceiling = 1240
    Q_total = Q_value+Q_door+Q_ceiling
    return Q_total
    

Q_values = U_Wall.apply(Q_cal)

#Plotting
plt.figure()
fig3=plt.plot(U_Wall,Q_values)
plt.xlabel("U wall")
plt.ylabel("Heating Load values")   
plt.title ("Overall heating load vs. U value of the external wall")
plt.show(fig3)