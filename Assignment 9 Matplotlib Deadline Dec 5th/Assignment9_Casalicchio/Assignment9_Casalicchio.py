# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HeatingLoadValues=[1163.1,1240.0,92.5]
CoolingLoadValues=[550.1,514.6,43.0]
labels=["WALLS","ROOF","DOOR"]

# 1. A pie chart showing the share of each component in the total heating load (opaque)

cols = ["blue","violet","green"]  
plt.figure()
plt.pie(HeatingLoadValues, labels = labels, colors = cols, startangle = 90, explode = (0.01,0.01,0.01), autopct = '%1.1f%%')

# 2. A pie chart showing the share of each component in the total cooling load (opaque)

cols = ["red","orange","yellow"] 
plt.figure()
plt.pie(CoolingLoadValues, labels = labels, colors = cols, startangle = 90, explode = (0.01,0.01,0.01), autopct = '%1.1f%%')

# 3. A 2D plot which shows the effect of changing only the U value of the external wall on the overall heating load (opaque), 
#    The range of change in U value is arbitrary.

Delta_T = 24.8 # K
Area = 105.8 #m2
Q_door=92.5 #W
Q_roof=1240.0 #W
U_wall = np.arange(0.24,0.44,0.04)
Q_wall = U_wall*Area*Delta_T
Q_tot = Q_wall + Q_door + Q_roof

plt.figure()
plt.plot(U_wall,Q_tot)
plt.xlabel("U value of the external wall")  
plt.ylabel("overall heating load")
plt.show()