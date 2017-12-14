import pandas as pd
import matplotlib.pyplot as plt


opaque_components = ["wall","ceiling","door"]
cooling_load = [547.5,514.6,43]
heating_load = [1149.2,1240,92.5]

cols = ["c","mediumseagreen","b"]


#pie chart with cooling load shares
plt.figure()
plt.pie(cooling_load,labels=opaque_components,colors = cols,startangle=90,explode=(0.1,0.1,0),autopct='%1.1f%%')
plt.title("cooling load shares")
plt.show()

#pie chart with heating load shares
cols = ["g","r","b"]
plt.figure()
plt.pie(heating_load,labels=opaque_components,colors = cols,startangle=90,explode=(0.1,0.1,0),autopct='%1.1f%%')
plt.title("heating load shares")
plt.show()

#U values of the wall
wall_area = 105.8

u_range = range(400,501)
u_series = pd.Series(u_range)/1000
dt = 24.8

HF = u_series*dt
Q_wall = HF*wall_area

Q_wo_wall = 2483-1149.2

Q_tot = Q_wo_wall+Q_wall

plt.plot(u_series,Q_tot)
plt.title("U range")
plt.show()