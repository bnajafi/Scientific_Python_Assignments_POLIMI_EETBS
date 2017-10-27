# -*- coding: utf-8 -*-
"""

EETBS 2017/2018 - Assignment 6 - Redoing assignment 2 using pandas module

Giorgio Moretti (10433550)

"""
import pandas as pd

# The lists are made using this order: [type, length, k, h, area, R value]

resistances_names = ["indoor","outdoor","foam","side plaster","center plaster","brick"]
resistances_indices = ["type","L","k","h","A","R"]

R1 = ["conv", None, None, 10, 0.25, 0]
R2 = ["conv", None, None, 25, 0.25, 0]
R3 = ["cond", 0.03, 0.026, None, 0.25, 0]
R4 = ["cond", 0.02, 0.22, None, 0.25, 0]
R5 = ["cond", 0.16, 0.22, None, 0.015, 0]
R6 = ["cond", 0.16, 0.72, None, 0.22, 0]

resistances = [R1,R2,R3,R4,R5,R6]

R_dataframe = pd.DataFrame(resistances,resistances_names,resistances_indices)

R_dataframe.loc[:,"R"][R_dataframe.loc[:,"type"] == "conv"] = 1.0/(R_dataframe.loc[:,"h"][R_dataframe.loc[:,"type"] == "conv"]*R_dataframe.loc[:,"A"][R_dataframe.loc[:,"type"] == "conv"])
R_dataframe.loc[:,"R"][R_dataframe.loc[:,"type"] == "cond"] = R_dataframe.loc[:,"L"][R_dataframe.loc[:,"type"] == "cond"]/(R_dataframe.loc[:,"k"][R_dataframe.loc[:,"type"] == "cond"]*R_dataframe.loc[:,"A"][R_dataframe.loc[:,"type"] == "cond"])

print R_dataframe 

R_series = R_dataframe.loc["indoor","R"] +  R_dataframe.loc["outdoor","R"] +  R_dataframe.loc["foam","R"] + 2*R_dataframe.loc["side plaster","R"]
R_parallel =  1/(2/R_dataframe.loc["center plaster","R"] + 1/ R_dataframe.loc["brick","R"])

R_TOT = round(R_series + R_parallel,4)

T_in = 20  # [°C]
T_out = -10  # [°C]

A_unit = 1*0.25  # [m^2]
Qdot_unit = round((T_in - T_out)/R_TOT,4)  # unit heat transfer rate [W]

A_wall = 3*5  # [m^2]
Qdot_wall =  round(Qdot_unit * (A_wall/A_unit),4)  # [W]

print "\n ********** RESULTS **********"
print "\n The total resistance of the wall is: R_WALL_TOT = " + str(R_TOT) + " °C/W"
print "\n The unit heat transfer rate is: Qdot_UNIT = " + str(Qdot_unit) + " W"
print "\n The heat transfer rate through the wall is: Qdot_WALL = " + str(Qdot_wall) + " W"